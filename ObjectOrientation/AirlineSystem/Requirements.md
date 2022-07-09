# Airline System

# Requirements
- Customers can book flights to/from destinations
- Customers can cancel flights
- Customers can search for flights for given date/source/dest
- Customers can book multiple seats per booking
- Airlines have a number of scheduled flights available
- Airlines carry/hire aircraft for flights
- Admins can create/remove flights
- System should assign crew/pilots per flight
- System should handle payments/bookings
- System should send notifications

# Classes/Entities
- Account
- Passenger : Account
- Employee : Account

- Pilot : Employee
- Admins : Employee
- Attendants : Employee

- Crew
- Crews HAVE Pilots and Attendants

- Airlines
- Aircraft
- Seat
- Airlines HAVE Aircrafts
- Aircrafts HAVE Seats

- Flights
- Schedule
- Schedules HAVE source, destination, date/time
- Flights HAVE Airline, Aircraft, Crew, Schedule, Passengers

- AirlineSystem
- PaymentSystem
- BookingSystem
- SearchSystem
- SchedulingSystem