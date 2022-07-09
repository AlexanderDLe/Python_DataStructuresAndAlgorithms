# Design a Movie Ticket Booking System

# Requirements

# Users
-Users can book/purchase tickets at a specific theater
-Users can browser movies and based on title, category, genre, city
-Users should be able to pay with credit cards
-Users Admins can create/delete shows

# Theaters
-Booking a ticket reserves a seat at a particular theater
-A theater keeps track of its available seats and will not allow
 rebooking a seat that has already been reserved
-Theaters have a defined number of seats per room
-Theaters have various number of shows playing, 

# System
-System should be able to send notifcations, coordinate booings, cancellations


# Actors
Guest
Members
Order
Cinema
Showing
Seat
Movie
Admin


# Functions
bookTickets([arrayOfSeats])
createOrder(order)
cancelOrder(orderID)
makePayment()
searchMovies(query)



# Data Modeling

MEMBER TABLE
memberID: UUID
username: string
dateCreated: timestamp
email: string
address: string


THEATER TABLE
theaterID: UUID
theaterName: string
dateCreated: timestamp
address: string
rooms: references to NoSQL data objects


ROOM OBJECT MODELING
theaterID: {
  roomID: {
    totalSeats: int,
    availableSeats: {}
  },
  ...
}

ORDER TABLE
OrderID: UUID
total: float
theater: theaterName
status: string
