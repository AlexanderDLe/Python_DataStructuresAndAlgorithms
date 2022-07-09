# Design an Online Stock Brokerage System

# Requirements
- Users can trade (buy/sell) stocks online
- Users can have multiple 'lots' of the same type
  If a user buys the same stock multiple times, the system should
  be able to differentiate between different lots of the same stock.
- Keep track of user transactions (history)
- Keep track of user portfolio
- Show performance charts for each user
- Alert users of predefined level changes

# Classes
- Account
- Member : Account
- Admin : Account
- Company : Account

- Company has StockHistory
- PerformanceChart has Company
