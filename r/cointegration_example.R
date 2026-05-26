# Optional R reference — cointegration / pairs (Phase III SIG-004)
# Run: Rscript r/cointegration_example.R

set.seed(42)
n <- 500
x <- cumsum(rnorm(n))
y <- 0.8 * x + rnorm(n, sd = 0.5)
spread <- y - 0.8 * x
cat("Spread sd:", sd(spread), "\n")
cat("Mean reversion proxy (ACF lag-1):", cor(spread[-1], spread[-length(spread)]), "\n")
