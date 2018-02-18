#dictonary = {key:value, key2:value2}

#schedule = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"", 17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:""}
schedule = []
for day in range(168):
    schedule.append("")

def activityPlanner(activity_name, amt_of_time, start_time, start_day): # Plans activity
    can_schedule = True
    temp = start_time
    for hour in range(amt_of_time):
        if temp >= len(schedule[0]):
            print("There's only so many hours in the day")
            can_schedule = False
            break
        elif schedule[temp] != "":
            print ("You can't do two activities at once.")
            can_schedule = False
            break
        temp += 1
    for hour in range(amt_of_time):
        if can_schedule != False:
            schedule[start_time] = activity_name
            start_time += 1
        amt_of_time -= 1
    print (schedule)
        
'''
If not enough time then return fail
Analayze how much time between activities and assign homework
'''
def eventPlanner(event_name, amt_of_time):
    count_empty = 0
    for hour in range(len(schedule)):
        if schedule[hour] == "":
            count_empty += 1
    if amt_of_time > count_empty:
        print("Do you have a time turner?")
    else:
        count = 0
        first_hour = 0
        for hour in range(len(schedule)):
            if schedule[hour] == "":
                count += 1
            else:
                count = 0
            if count == amt_of_time:
                first_hour = hour-amt_of_time+1
                break
        # activityPlanner(event_name, amt_of_time, first_hour)
        for i in range(amt_of_time):
            schedule[first_hour] = event_name
            first_hour += 1
        print(schedule)
    
# Main method
user_input = input("Do you want to enter an activity? y/n ")
while user_input != "n":
    activity_name = input("What is the name of your activity? ") # Sleep
    start = input("When does it start? ") # Military time
    time = input("How long does it take in hours? ") # In hours
    start_day = input("What day is it? ")
    repeat = input("Does it repeat? y/n")
    if time.isdigit() and start.isdigit() and activity_name != "" and start_day.isdigit():
        activityPlanner(activity_name, int(time), int(start), int(start_day))
    else:
        print("Say something I'm giving up on you")
    #interval = input("How many days between each activity? ") # In days
    #activities.update({time: [activity_name, start, interval]})
 #   time_paradox_check(activities)
 #   activities.update({start: [activity_name, time]})
    user_input = input("Do you want to enter an activity? y/n ")

user_input = input("Do you have any events to plan? y/n ")
while user_input != "n":
    assignment = input("Please say which event you need to add. ") #adding assignment name
    event_time = input("Please say how many hours the event takes. ") #setting the time it takes
    if assignment != "" and event_time.isdigit():
        eventPlanner(assignment, int(event_time))
    else:
        print("Say something I'm giving up on you")
    # homework.update({assignment: [homeworktime]})
    user_input = input("Do you have any more homework assignments? y/n ") #sees whether to loop back or not

print()
for key in range(len(schedule)):
    if schedule[key]=="":
        print("For hour " + str(key) + " you have free time.")    
    else:
        print("For hour " + str(key) + " you will be doing " + schedule[key])
