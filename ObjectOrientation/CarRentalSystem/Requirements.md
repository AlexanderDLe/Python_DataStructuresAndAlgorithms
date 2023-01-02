# Design Car Rental System

##### Controller/Management Classes

# CarRentalSystem Requirements
- Allow users to rent and return vehicles
- Allow users to cancel reservations
- Create/manage customer transactions
- Notify customers of incoming due dates

# CarCollections Requirements
- Manage the collection of cars in the system
- Add/Remove/Update vehicles
- Allow customers to query for cars
- Each rental is associated with a customer when rented

# SearchSystem Requirements
- Use CarCollections to query for cars by specific make/models/etc.

# Notification System
- Tracks events/upcoming dates to notify customers


##### Data Object Classes

# Customer Requirements
- Customer classes contains data about the customer, history, etc.
- Customer information (name, phone, email, ID) is stored
- Customers can make multiple rentals/reservations

# Admin Requirements
- Admins have authorization to add/remove/update vehicles

# Car Requirements
- Car is associated with a unique ID
- Car is associated with a make/model
- Car is associated with a parking spot for location
- Car information (year, mileage, color, etc.) is stored