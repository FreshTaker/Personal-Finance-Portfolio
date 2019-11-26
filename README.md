# Personal-Finance-Portfolio
Collection of Scripts and results


## stockTracker.py
This script takes the list of stocks and quantities that is in a portfolio and outputs graphs of various timetables.

1) Uses Yahoo Finance API to collect current price.
2) Analyze portfolio:
  2.1) get Short Name, market price
3) Uses pickle or sqlite to store and restore data for dynamic graphs (30-day, 90-day, 1-year).
4) Uses Matlabplot(?) to create plots.
5) Alerts user when dividend takes place (qty of stock may change and should be manually updated)
6) Pulls from multiple Portfolios (csv's?)


## houseValueEst.py
This script pulls from a variety of APIs to get an estimated home value.

1) Pull from Zillow, Redfin, MLS.
2) Use pickle to store and restore data for dynamic graphs.
3) Use Matlabplot(?) to create plots.


