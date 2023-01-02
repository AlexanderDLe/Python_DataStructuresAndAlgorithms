# Requirements

# Customers:
1. Customers can buy goods
2. Customers can return goods
3. Customers can add/remove/edit items into shopping carts
4. Customers can checkout items
5. Customers can view products
6. Customers can review/rate items
7. Customers can search for products to buy by name/category
8. Users can search/view products, but must be registered to buy
9. Users can create and cancel orders (if item hasn't been shipped)
10. Users should get notifications whenever there is a change in order/shipping status

# Admin/Sellers:
1. Sellers can add products to sell on their page
2. Sellers can set inventory amount
3. Sellers can sell items



# Actors:
Admin: Manage seller accounts. Add/remove products, etc. 
Guest: Can search and view items - but have restricted access
Member: Have access to purchase, review, rate, etc.
System: Notifying members of orders, etc.


# Classes
System
Admin
Member
Guest
ShoppingCart
Product
Item
Order
Notification
