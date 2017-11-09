# THe purpose of this script is to map the value of rental properties accross the US. The initial
# look will be at (median home price)/(median home value). The data is collected from zillow
# and uses the Zillow Rent Index (ZRI) and Zillow Home Value Index (ZHVI). The methodology for 
# these indexes can be found at:
# https://www.zillow.com/research/zhvi-methodology-6032/
# https://www.zillow.com/research/zillow-rent-index-methodology-2393/
# for ZHVI and ZRI respectively. The specific reports used here are the 'ZHVI All Homes (SFR, Condo/Co-op) Time Series ($)'
# and 'ZRI Summary: Multifamily, SFR, Condo/Co-op (Current Month)'.

#load home rents
rentPath <- '/home/greg/Documents/Projects/Data-Analysis/Real Estate Market Analysis/Zip_Zri_AllHomesPlusMultifamily_Summary.csv'
rents <- read.csv2(rentPath, header = TRUE, sep=",")
head(rents, n=5)
#note that I originally thought ZRI's>5000 were errors but it appears those are accurate. Most of those areas are in LA, 
  # Silicon Valley and NYC

#load home values
valuePath <- '/home/greg/Documents/Projects/Data-Analysis/Real Estate Market Analysis/Zip_Zhvi_Summary_AllHomes.csv'
values <- read.csv2(valuePath, header = TRUE, sep=",")
head(values, n=5)

#create a single dataset, remove redundent variables before doing so
rents <- rents[c("RegionName", "SizeRank", "Zri", "MoM", "QoQ", "YoY", "ZriRecordCnt")]
homeData <- merge(rents, values, by = "RegionName")
colnames(homeData)[colnames(homeData)=="RegionName"] <- "ZipCode"

#for a first cut, look at markets with high median rents compared to median values
homeData$heatIndex <- homeData$Zri/homeData$Zhvi
hist(homeData$heatIndex)

#install zipcode package before continuing
library(zipcode)
library(ggplot2)
data(zipcode)
colnames(zipcode)[colnames(zipcode)=="zip"] <- "ZipCode"
homeData <- merge(homeData, zipcode, by.x='ZipCode', by.y='ZipCode')
homeData$region <- substr(homeData$ZipCode, 1, 1)

plotUS <- function(data, color){
  g <- ggplot(data=data) + geom_point(aes(x=longitude, y=latitude, colour=(color))) + scale_colour_gradientn(colours=rev(rainbow(4)))
  
  # simplify display and limit to the "lower 48"
  g = g + theme_bw() + scale_x_continuous(limits = c(-125,-66), breaks = NULL)
  g = g + scale_y_continuous(limits = c(25,50), breaks = NULL)
  
  # don't need axis labels
  g = g + labs(x=NULL, y=NULL)
  
  print(g)
}

plotUS(homeData, homeData$heatIndex)

#sort the dataset by heat index to look for the best potential markets
homeData <- homeData[order(homeData$heatIndex, decreasing = TRUE), ]

#Baltimore and Philly look hot
Baltimore <- homeData[which(homeData$City == "Baltimore"), ]
