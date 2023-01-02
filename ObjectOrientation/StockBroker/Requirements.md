# Design an Online Stock Brokerage System

# Requirements

# Members
- Users can trade (buy/sell) stocks online
- Users can have multiple 'lots' of the same type
  If a user buys the same stock multiple times, the system should
  be able to differentiate between different lots of the same stock.
- Keep track of user transactions (history)
- Keep track of user portfolio
- Alert users of predefined level changes

# Admin
- Create/Remove companies
- Block/unblock members

# Company
- Company contains company information
- Companies contain performance history

# Performance Charts
- Show performance charts for each user

# Stock
- Contains stock count, returns, value, etc.

# Alert
- Contains relation of company, user, and threshold.

# Brokerage System
- Orchestrates actions of members and companies
- Notifies members of various alerts, etc.