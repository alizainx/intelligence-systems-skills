compute_trimmed_zscores <- function(x, na_rm = TRUE) {
  if (!is.numeric(x)) stop("x must be a numeric vector", call. = FALSE)
  if (!is.logical(na_rm) || length(na_rm) != 1L || is.na(na_rm)) {
    stop("na_rm must be a scalar logical", call. = FALSE)
  }
  vals <- if (na_rm) x[!is.na(x)] else x
  n <- length(vals)
  if (n < 2L) return(rep(NA_real_, length(x)))
  mu <- sum(vals) / n
  sd_val <- sqrt(sum((vals - mu)^2) / (n - 1L))
  if (sd_val == 0.0) return(rep(0.0, length(x)))
  (x - mu) / sd_val
}
