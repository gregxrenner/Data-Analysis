# THe purpose of this script is to map the value of rental properties accross the US. The initial
# look will be at (median home price)/(median home value). The data is collected from zillow
# and uses the Zillow Rent Index (ZRI) and Zillow Home Value Index (ZHVI). The methodology for 
# these indexes can be found at:
# https://www.zillow.com/research/zhvi-methodology-6032/
# https://www.zillow.com/research/zillow-rent-index-methodology-2393/
# for ZHVI and ZRI respectively. The specific reports used here are the 'ZHVI All Homes (SFR, Condo/Co-op) Time Series ($)'
# and 'ZRI Summary: Multifamily, SFR, Condo/Co-op (Current Month)'.

#load home rents
rents <- read.csv2('C:/Users/Gregory.Renner/Documents/Personal/Programs/Data-Analysis/Real Estate Market Analysis/Zip_Zhvi_Summary_AllHomes.csv', header = TRUE, sep=",")
head(rents, n=5)

#load home values
values <- read.csv2('C:/Users/Gregory.Renner/Documents/Personal/Programs/Data-Analysis/Real Estate Market Analysis/Zip_Zri_AllHomesPlusMultifamily_Summary.csv', header = TRUE, sep=",")
head(values, n=5)


