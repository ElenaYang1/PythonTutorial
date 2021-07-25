def trip_planner_welcome(name):
    print("Welcome to trip planner v1.0 {}".format(name))

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
    print("Your trip starts off in {}".format(origin))
    print("And you are travelling to {}".format(destination))
    print("And you will be travelling by {}".format(mode_of_transport))
    print("It will take approximately {} hours".format(estimated_time))

def estimated_time_rounded(estimated_time):
    rounder_time = round(estimated_time)
    return rounder_time

trip_planner_welcome("Elena")

estimate = estimated_time_rounded(12.5)

destination_setup("Toronto", "Tim Hortons", estimate)
