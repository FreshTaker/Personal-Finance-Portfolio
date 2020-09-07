# Personal-Finance-Portfolio
Collection of Scripts and results

## loanCalculator.py
This script calculates:

    * number of monthly payments
    * annuity monthly payment amount
    * credit principal
    * differentiated payments (constant pay down of principal)
This script was made following the "CreditCalc" tutorial on http://hyperskills.org.
I have added my own additions to this script to run with & without arguments.

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


## cashFlowProjector
This script uses inputs like weekly income and estimated expenses to project your cash flow.  



