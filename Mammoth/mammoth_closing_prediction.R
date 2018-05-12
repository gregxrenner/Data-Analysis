# The purpose of this script is to estimate Mammouth Mountains closing day based on current seasonal snowfall.

# Load the data.
#dataPath <- "C:/Users/Gregory.Renner/Documents/Personal/Programs/Data-Analysis/Mammoth/Mammoth_Historcial_Data.csv"
dataPath <- "C:/Users/Gregory/Documents/Personal/git/Data-Analysis/Mammoth/Mammoth_Historcial_Data.csv"
mammoth <- read.csv2(dataPath, header = TRUE, sep=",")


# Convert snowfall variables to numeric.
mammoth[, 4:15] <- sapply(sapply(mammoth[, 4:15], as.character), as.numeric) #first convert to char to deal with factors


# Convert date variables to date type.
mammoth$Opening <- as.Date(mammoth$Opening, "%m/%d/%Y")
mammoth$Closing <- as.Date(mammoth$Closing, "%m/%d/%Y")


# Calculate season length and the number of days between Jan 1 and closing day. Make sure both are type numeric.
mammoth$season.length <-  as.numeric(mammoth$Closing - mammoth$Opening)
mammoth$closing_day <- as.numeric(mammoth$Closing - as.Date(paste(1, 1, format(mammoth$Closing, "%Y")), "%m %d %Y"))

# Examine the relationship between total snowfall and closing date.
plot(mammoth$Total, mammoth$closing_day)
                                           
# Start with a univariate least squares regression.
mod1 <- lm(closing_day ~ Total, data = mammoth)
mod1.predict <- predict(mod1, data.frame(Total=c(260)), interval = "predict", level = 0.9)
cat("The estimated closing day is ", predict(mod1, data.frame(Total=c(260)))[1])
cat("With 90% confidence we estimate the closing day to be between ", mod1.predict[2], " and ", mod1.predict[3])
summary(mod1)

# Check that error assumptions hold with a QQ plot
mod1.stdres <- rstandard(mod1)
qqnorm(mod1.stdres, 
       ylab = "Standardized Residuals", 
       xlab = "Normal Scores", 
       main = "The 'steps' can be attributed to closing dates\n occuring at the end or beginning of the month.")
qqline(mod1.stdres)

# Now predict closing date using each months snowfall as a separate explanatory variable.
mod2 <- lm(closing_day ~ Pre.Oct + Oct + Nov + Dec + Jan + Feb + Mar + Apr + May, data = mammoth)
mod2.predict.data <- mammoth[49, 4:14]
mod2.predict <- predict(mod2, mod2.predict.data, interval = "predict", level = 0.9)
cat("With 90% confidence we estimate the closing day to be between", mod2.predict[2], " and ", mod2.predict[3])
# Lower prediction bound.
print(as.Date("2018/01/01") + as.difftime(mod2.predict[2], unit = "days"))
# Upper prediction bound.
print(as.Date("2018/01/01") + as.difftime(mod2.predict[3], unit = "days"))
summary(mod2)

# The prediction interval is very wide which is likely an effect of the model's low R-squaed.
#   Investigate the relationships between each explanatory variable and the response variable.
pairs(~closing_day+Pre.Oct+Oct+Nov+Dec+Jan+Feb+Mar+Apr+May, data=mammoth)
