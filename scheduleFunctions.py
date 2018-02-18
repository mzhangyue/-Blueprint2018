#dictonary = {key:value, key2:value2}

schedule = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"", 17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:""}

def activityPlanner(activity_name, amt_of_time, start_time):
    if schedule[start_time] != "":
            print ("You can't do two activities at once.")
    schedule[start_time] = activity_name
    while amt_of_time > 1:
        start_time +=  1
        if schedule[start_time] != "":
            print ("You can't do two activities at once.")
            break
        schedule[start_time] = activity_name
        amt_of_time -= 1
    print (schedule)
    
user_input = input("Do you want to enter an activity? y/n ")
while user_input != "n":
    activity_name = input("What is the name of your activity? ") # Sleep
    time = input("How long does it take in hours? ") # In hours
    start = input("When does it start? ") # Military time
    activityPlanner(activity_name, int(time), int(start))
    #interval = input("How many days between each activity? ") # In days
    user_input = input("Do you want to enter an activity? y/n ")
    
'''for start_time in activities:
    print(activities[start_time])'''


    
    
    
