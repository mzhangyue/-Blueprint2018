#dictonary = {key:value, key2:value2}

#schedule = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"", 17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:""}
def configure_days(days, schedule):
    for day in range(24*int(days)):
        schedule.append("")

def activityPlanner(activity_name, amt_of_time, start_time, start_day, schedule): # Plans activity
    can_schedule = True
    temp = start_time
    for hour in range(amt_of_time):
        if temp >= 24:
            print("There's only so many hours in the day")
            can_schedule = False
            break
        elif schedule[24*(start_day-1)+temp] != "":
            print ("You can't do two activities at once.")
            can_schedule = False
            break
        temp += 1
    for hour in range(amt_of_time):
        if can_schedule != False:
            schedule[start_time] = activity_name
            start_time += 1
        amt_of_time -= 1
    #print (schedule)

def repeated_activityPlanner(activity_name, amt_of_time, start_time, start_day, repeat_interval, schedule): # Plans activity
    can_schedule = True
    temp = start_time
    reset1 = temp
    reset2 = amt_of_time
    while start_day in range(len(schedule)//24):
        for hour in range(amt_of_time):
            if temp >= 24:
                print("There's only so many hours in the day")
                can_schedule = False
                break
            elif schedule[24*(start_day)+temp] != "":
                print ("You can't do two activities at once.")
                can_schedule = False
                break
            temp += 1
        for hour in range(amt_of_time):
            if can_schedule != False:
                schedule[24*(start_day-1)+start_time] = activity_name
                start_time += 1
            amt_of_time -= 1
        temp = reset1
        start_time = reset1
        amt_of_time = reset2
        can_schedule = True
        start_day += repeat_interval+1
    #print (schedule)
        
'''
If not enough time then return fail
Analayze how much time between activities and assign homework
'''
def eventPlanner(event_name, amt_of_time, schedule):
    count_empty = 0
    for hour in range(len(schedule)):
        if schedule[hour] == "":
            count_empty += 1
    if amt_of_time > count_empty:
        print("Do you have a time turner?")
    else:
        count = 0
        first_hour = -1
        for hour in range(len(schedule)):
            if schedule[hour] == "":
                count += 1
            else:
                count = 0
            if count == amt_of_time:
                first_hour = hour-amt_of_time+1
                break
        # activityPlanner(event_name, amt_of_time, first_hour)
        if first_hour != -1:
            for i in range(amt_of_time):
                schedule[first_hour] = event_name
                first_hour += 1
        else:
            count = 0
            while amt_of_time > 0:
                if schedule[count] == "":
                    schedule[count] = event_name
                    amt_of_time -= 1
                count += 1
        #print(schedule)

def due_eventPlanner(event_name, amt_of_time, due_date, schedule):
    count_empty = 0
    for hour in range(24*due_date):
        if schedule[hour] == "":
            count_empty += 1
    if amt_of_time > count_empty:
        print("Do you have a time turner?")
    else:
        count = 0
        first_hour = -1
        for hour in range(7*due_date):
            if schedule[hour] == "":
                count += 1
            else:
                count = 0
            if count == amt_of_time:
                first_hour = hour-amt_of_time+1
                break
        # activityPlanner(event_name, amt_of_time, first_hour)
        if first_hour != -1:
            for i in range(amt_of_time):
                schedule[first_hour] = event_name
                first_hour += 1
        else:
            count = 0
            while amt_of_time > 0:
                if schedule[count] == "":
                    schedule[count] = event_name
                    amt_of_time -= 1
                count += 1
       # print(schedule)
        
# Main method
schedule = []
days = input("For how many days do you want this schedule? ")
configure_days(days, schedule)
user_input = input("Do you want to enter an activity? y/n ")
while user_input != "n":
    activity_name = input("What is the name of your activity? ") # Sleep
    start = input("When does it start? ") # Military time
    time = input("How long does it take in hours? ") # In hours
    start_day = input("What day is it? ")
    repeat = input("Does it repeat? y/n ")
    if repeat == "n":   
        if time.isdigit() and start.isdigit() and activity_name != "" and start_day.isdigit() and int(start_day) <= int(days) and int(start_day) > 0:
            activityPlanner(activity_name, int(time), int(start), int(start_day), schedule)
        else:
            print("Say something I'm giving up on you")
    else:
        repeat_interval = input("How many days between when it repeats? ")
        if time.isdigit() and start.isdigit() and activity_name != "" and start_day.isdigit() and repeat_interval.isdigit():
            repeated_activityPlanner(activity_name, int(time), int(start), int(start_day), int(repeat_interval), schedule)
        else:
            print("Say something I'm giving up on you")
    user_input = input("Do you want to enter an activity? y/n ")
    

    
# Events
print("Put events in order of due date priority for best arrangement")
user_input = input("Do you have any events to plan? y/n ")
while user_input != "n":
    assignment = input("Please say which event you need to add. ") #adding assignment name
    event_time = input("Please say how many hours the event takes. ") #setting the time it takes
    due = input("Does it have a due date? ")
    if due == "n":
        if assignment != "" and event_time.isdigit():
            eventPlanner(assignment, int(event_time), schedule)
        else:
            print("Say something I'm giving up on you")
    else:
        due_date = input("What day is it due? ")
        if assignment != "" and event_time.isdigit() and due_date.isdigit() and int(due_date) > 0 and int(due_date) < 8:
            due_eventPlanner(assignment, int(event_time), int(due_date), schedule)
        else:
            print("Say something I'm giving up on you")
    # homework.update({assignment: [homeworktime]})
    user_input = input("Do you have any more homework assignments? y/n ") #sees whether to loop back or not

print()

'''
for key in range(len(schedule)):
    if schedule[key]=="":
        print("For hour " + str(key) + " you have free time.")    
    else:
        print("For hour " + str(key) + " you will be doing " + schedule[key])'''

for day in range(int(days)):
    for h in range(24):
        if schedule[day*24+h] == "":
            print("For day " + str(day+1) + " and hour " + str(h) + " you have free time.")
        else:
            print("For day "+str(day+1)+" and hour "+str(h)+" you will be doing "+schedule[day*24+h]+".")
