#dictonary = {key:value, key2:value2}

schedule = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"", 17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:""}

def activityPlanner(activity_name, amt_of_time, start_time):
    schedule[start_time] = activity_name
    while amt_of_time > 1:
        start_time++
        schedule[start_time] = activity name
        amt_of_time--
    
    
    
    
