from tkinter import *

class MyFirstGUI:
    
    def __init__(self, master):
        self.activities = []
        self.assignments = []
        self.master = master
        master.title("Sketchy Schedule")

        self.num_days_label = Label(master, text = "Number of Days").grid(row = 0)
        self.act_label = Label(master, text="Activity Name").grid(row=1)
        self.start_label = Label(master, text="Starting Time").grid(row=2)
        self.dur_label = Label(master, text="Duration").grid(row=3)
        self.stype_label = Label(master, text = "Type").grid(row=7)
        self.repeat_label = Label(master, text = "Days in Between Repeating").grid(row = 4)
        self.whichday_label = Label(master, text = "Which Day").grid(row = 5)
        self.duedate_label = Label(master, text = "Due date?").grid(row = 6)
        
        self.num_days_entry = Entry(master)
        self.act_entry = Entry(master)
        self.start_entry = Entry(master)
        self.dur_entry = Entry(master)
        self.type_value = IntVar()
        self.repeat_entry = Entry(master)
        self.whichday_entry = Entry(master)
        self.duedate_entry = Entry(master)

        
        self.num_days_entry.grid(row =0, column = 1)
        self.act_entry.grid(row=1, column=1)
        self.start_entry.grid(row=2, column=1)
        self.dur_entry.grid(row=3, column=1)
        self.repeat_entry.grid(row = 4, column = 1)
        self.whichday_entry.grid(row = 5, column = 1)
        self.duedate_entry.grid(row = 6, column = 1)
        
        for i, v in enumerate(["Activity", "Assignment"]):
            r = Radiobutton(self.master,
                           text = v,
                           padx = 20,
                           variable = self.type_value,
                           value = i)

            r.grid(row = 7 + i, column = 1)
            

        self.save_button = Button(master, text="Save", command=self.save)
        self.save_button.grid(row=9, column=0, sticky=W, pady=4)

        self.close_button = Button(master, text="Close", command=self.close)
        self.close_button.grid(row=9, column=1, sticky=W, pady=4)
    def save(self):
        activity_name = self.act_entry.get()
        start = int(self.start_entry.get())
        dur = int(self.dur_entry.get())
        repeat = int(self.repeat_entry.get())
        whichday = int(self.whichday_entry.get())
        duedate = int(self.duedate_entry.get())
        num_days = int(self.num_days_entry.get())

        is_assignment = self.type_value == 1
        if not is_assignment:
            to_save = (activity_name, start, dur, repeat, whichday, duedate)
            (self.activities).append(to_save)
        else:
            to_save = (activity_name, dur)
            self.assignments.append(to_save) 

        for e in (self.act_entry, self.start_entry, self.dur_entry, self.repeat_entry, self.whichday_entry, self.duedate):
            e.delete(0, "end")

        

        
    def close(self):
        for activity_name, start, dur, repeat, whichday, duedate in self.activities:
            print(activity_name, start, dur, repeat, whichday, duedate)

        for activity_name, dur in self.assignments:
            print(activity_name, dur)

        
        self.master.quit()
        self.master.destroy()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


