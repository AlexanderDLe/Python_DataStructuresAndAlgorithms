# Design Calendar App

# User Requirements
- User can add events
- User can remove events
- User gets notified of events from the system
- User can view all events
- User can have multiple calendars (personal and work)
- User has account

# Calendar Requirements
- Calendar is associated with accounts
- Calendar is associated with EventSystem
- Calendar is associated with Notifying users of events
- Calendar base class can be extended to other calendar types


# Event Requirements
- Events can be created by user
- Events are linked to calendars
- Events have title, description, etc.
- Events have a time frame

# EventFactory
- Creates events of different types

# EventSystem
- EventSystem contain, organize, and manage events
- EventSystem query for events

# Notification System
- As time progresses, calendar will check for events
- If event occurs, notification system will send user a notification