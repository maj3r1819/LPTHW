cars=100
space=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space
average_passengers_per_car=passengers/cars_driven
print("there are ",cars,"cars available.")
print("there are omly",drivers,"drvers available.")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today")
print("we have ",passengers,"to carpool today")
print("we need to put about",average_passengers_per_car,"in each car")
