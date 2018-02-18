homework = {} #dictionary
user_input = input("Do you have any homework? y/n ")
while user_input != "n":
    assignment = input("Please say which assignment you need to add. ") #adding assignment name
    homeworktime = input("Please say how many hours the assignment takes. ") #setting the time it takes
    homework.update({assignment: [homeworktime]})
    user_input = input("Do you have any more homework assignments? y/n ") #sees whether to loop back or not 
    
