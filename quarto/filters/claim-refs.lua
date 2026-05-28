-- Resolve [[claim:CLM-YYYY-NNN]] to links into the evidence registry appendix.

local claims_map = nil
local unknown_ids = {}

local function claims_map_path()
  local src = debug.getinfo(1, "S").source
  if src:sub(1, 1) == "@" then
    src = src:sub(2)
  end
  local dir = pandoc.path.directory(src)
  return pandoc.path.join({ dir, "claims-map.json" })
end

local function load_claims()
  if claims_map then
    return claims_map
  end
  local path = claims_map_path()
  local f = io.open(path, "r")
  if not f then
    io.stderr:write("claim-refs.lua: cannot open " .. path .. "\n")
    claims_map = {}
    return claims_map
  end
  local raw = f:read("*a")
  f:close()
  claims_map = pandoc.json.decode(raw)
  return claims_map
end

local pattern = "%[%[claim:(CLM%-%d+%-%d+)%]%]"

-- Relative path to evidence registry HTML (no fragment). Same-page returns "".
local function registry_base()
  if not (quarto and quarto.doc and quarto.doc.input_file) then
    return ""
  end
  local input = quarto.doc.input_file:gsub("\\", "/")
  if input:match("appendices/evidence%-registry%.qmd$") then
    return ""
  end
  if input:match("^chapters/") or input:match("/chapters/")
      or input:match("^notebooks/") or input:match("/notebooks/") then
    return "../appendices/evidence-registry.html"
  end
  return "appendices/evidence-registry.html"
end

local function claim_href(cid)
  local base = registry_base()
  if base == "" then
    return "#claim-" .. cid
  end
  return base .. "#claim-" .. cid
end

local function replace_claims(text, map)
  return (text:gsub(pattern, function(cid)
    if map[cid] then
      return string.format("[%s](%s)", cid, claim_href(cid))
    end
    table.insert(unknown_ids, cid)
    return "[[" .. cid .. " MISSING]]"
  end))
end

local function markdown_to_inlines(md)
  local doc = pandoc.read(md, "markdown")
  if #doc.blocks == 0 then
    return { pandoc.Str(md) }
  end
  local b = doc.blocks[1]
  if b.t == "Para" then
    return b.content
  end
  if b.t == "Plain" then
    return b.content
  end
  return { pandoc.Str(md) }
end

local function transform_inlines(inlines, map)
  local text = pandoc.utils.stringify(inlines)
  if not text:find("[[claim:", 1, true) then
    return inlines
  end
  local newt = replace_claims(text, map)
  if newt == text then
    return inlines
  end
  return markdown_to_inlines(newt)
end

function Plain(el)
  local map = load_claims()
  return pandoc.Plain(transform_inlines(el.content, map))
end

function Para(el)
  local map = load_claims()
  return pandoc.Para(transform_inlines(el.content, map))
end

function Pandoc(doc)
  unknown_ids = {}
  load_claims()
  doc = doc:walk({
    Plain = Plain,
    Para = Para,
  })
  if #unknown_ids > 0 then
    local seen = {}
    local uniq = {}
    for _, id in ipairs(unknown_ids) do
      if not seen[id] then
        seen[id] = true
        table.insert(uniq, id)
      end
    end
    io.stderr:write("claim-refs.lua: unknown claim IDs: " .. table.concat(uniq, ", ") .. "\n")
    os.exit(1)
  end
  return doc
end
