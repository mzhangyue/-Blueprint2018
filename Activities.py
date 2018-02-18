def time_paradox_check(start, activities):
    for activity in activities: # For each activity (start: [activity_name, time])
        if

activities = {}
user_input = input("Do you want to enter an activity? y/n ")
while user_input != "n":
    activity_name = input("What is the name of your activity? ") # Sleep
    time = input("How long does it take in hours? ") # In hours
    start = input("When does it start? ") # Military time
    #interval = input("How many days between each activity? ") # In days
    #activities.update({time: [activity_name, start, interval]})
    time_paradox_check(start, activities)
    activities.update({start: [activity_name, time]})
    user_input = input("Do you want to enter an activity? y/n ")
'''for start_time in activities:
    print(activities[start_time])'''
