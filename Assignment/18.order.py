# Order Status Check:
#    - Create a Python program using the `match` statement to check the status of a given order. 
# If the order status is "Processing," print "Order in process"; if it's "Shipped," print "Order shipped"; 
# if it's "Delivered," print "Order delivered"; otherwise, print "Unknown status."

Order_status="Shipped"

match Order_status:
    
    case "Processing":
        print("Order in process")
    case "Shipped":
        print("Order shipped")
    case "Delivered":
        print("Order delivered")
    case _:
        print("Unknown status")
    