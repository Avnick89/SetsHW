#Lesson3 Assignment|Sets

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
def flight_destination(our_routes, competitor_routes):
    similar_flights = our_routes.intersection(competitor_routes) #find the similarities
    print(similar_flights)
    unique_flights = our_routes.difference(competitor_routes) #find the unique specific to our routes
    print(unique_flights)
    unshared_flights = our_routes.symmetric_difference(competitor_routes) # find the unique beween both routes
    print(unshared_flights)

flight_destination(our_routes, competitor_routes)

#Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]


def remove_dup(customer_ids):
    customer_ids_set = set(customer_ids) 
    print(customer_ids_set)
    customer_ids = sorted(customer_ids_set)
    print(customer_ids)

remove_dup(customer_ids)