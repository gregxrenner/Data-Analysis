# This file is code used to solve problems in the textbook Foundations and Applications
  # of Statistics - An Introduction Using R

# Ex: 3.1.1 Show that f is a pdf.
# define the pdf
  f <- function(x) {3 * x^2 * (0 <= x & x <=1)}
  integrate(f, 0, 1)
  integrate(f, 0, 0.5)$value # give the approximate  value
  require(MASS)              # fractions() function is in MASS
  fractions(integrate(f, 0, 0.5)$value) # convert the solution to a fraction

# Ex: 3.1.3 Integrate a uniform pdf
  x <- 5:15
  # typically we would define a pdf this way:
  tempf <- function(x) {0.1 * (0 <= x & x <= 10)}
  tempf(x)
  integrate(tempf,7,10)

runif(6,0,10) # generate 6 random values from a uniform dist [0,10]
dunif(5,0,10) # calculate density of unif dist at 5
punif(3,0,10) # calcualte prob(x<3) on unif dist
qunif(0.25,0,10) # calcuate x for the 25th quantile

# Ex: 3.1.11
# Simulate the timing of Poisson events using the exponential distribution to model 
  # the time between consecutive events.
  runs <- 8; size <- 40
  # randomly generate 8 runs of 40 exponentially distributed arrivals
  time <- replicate(runs, cumsum(rexp(size)))
  df <- data.frame(time = as.vector(time), run = rep(1:runs, each=size))
  # use the shortest run as the maximum run time
  stop <- min(apply(time, 2, max))
  stop <- 5 * trunc(stop/5)
  df <- df[time <= stop,]
  #graph the results
  require(graphics)
  myplot <- stripchart(run~time, df, pch=1, cex=0.7, col='black',
                      panel=function(x,y,...){
                        panel.abline(h=seq(1.5,7.5,by=1),col='gray60')
                        panel.abline(v=seq(0,stop,by=5),col='gray60')
                        panel.stripchart(x,y,...)
                      })