import datetime
import calendar

def bill_for(month, active_subscription, users):
  # If no users were ever active, no fees should be charged.
  if not users: return 0

  # If no active subscription, then no feeds charged.
  if not active_subscription: return 0
  
  # If there are active subscriptions with users, then we should calculate bill for the month.  
  
  # 1. First, calculate the daily rate
  dailyRate = calculateDailyRate(month, active_subscription)
  
  # 2. Calculate the number of days that each user was active on the current month
  totalDaysActive = calculateTotalDaysActive(month, users)
  
  # 3. Calculate the number of days active by the daily rate
  totalCost = dailyRate * totalDaysActive
  
  return round(totalCost, 2)
  

####################
# Helper functions #
####################


def calculateTotalDaysActive(month, users):
  billingMonth = convertToDatetime(month)
  totalDaysActive = 0
  
  for user in users:
    startDate = user['activated_on']
    endDate = user['deactivated_on']
    
    # Do not calculate if end date occurs before billing month
    if endDate and endDate < billingMonth: continue
    
    # Set startdate to start of the month if it is <= billingMonth
    startDate = billingMonth if startDate <= billingMonth else startDate
    
    # Set enddate to end of month if no end date.
    endDate = endDate if endDate != None else last_day_of_month(billingMonth)
    
    # Add days active to result
    totalDaysActive += (endDate - startDate).days
  
  return totalDaysActive
    


def calculateDailyRate(month, active_subscription):
  # Get monthly fee
  monthlyFee = active_subscription['monthly_price_in_dollars']
  
  # Get number of days in current month
  year, month = month.split('-')
  year = int(year)
  month = int(month)
  numberOfDays = calendar.monthrange(year, month)
  
  # Calculate cost per day
  return monthlyFee / numberOfDays[1]

def convertToDatetime(dateStr):
  year, month = dateStr.split('-')
  return datetime.date(int(year), int(month), 1)

def first_day_of_month(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the first day of that month. For example:

  >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
  datetime.date(2019, 2, 1)                          # Feb 1

  Input type: datetime.date
  Output type: datetime.date
  """
  return date.replace(day=1)

def last_day_of_month(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the last day of that month. For example:

  >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
  datetime.date(2019, 2, 28)                        # Feb 28

  Input type: datetime.date
  Output type: datetime.date
  """
  last_day = calendar.monthrange(date.year, date.month)[1]
  return date.replace(day=last_day)

def next_day(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the next day. For example:

  >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
  datetime.date(2019, 2, 8)                 # Feb 8

  >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
  datetime.date(2019, 3, 1)                 # Mar  1

  Input type: datetime.date
  Output type: datetime.date
  """
  return date + datetime.timedelta(days=1)

def main():
  bill_for('2019-01', {
  'id': 1,
  'customer_id': 1,
  'monthly_price_in_dollars': 4
},
  [
  {
    'id': 1,
    'name': 'Employee #1',
    'activated_on': datetime.date(2018, 11, 4),
    'deactivated_on': None,
    'customer_id': 1,
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'activated_on': datetime.date(2018, 12, 4),
    'deactivated_on': None,
    'customer_id': 1,
  },
  {
    'id': 3,
    'name': 'Employee #3',
    'activated_on': datetime.date(2019, 1, 10),
    'deactivated_on': None,
    'customer_id': 1,
  },
])


main()