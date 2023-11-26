import sqlite3
import tkinter as tk
from tkinter import ttk


class profile():
    def __init__(self, nName, nColl, nCourse, nInterests):
        self.userName = nName
        self.userColl = nColl
        self.userCourse = nCourse
        self.userInterests = nInterests



def instantiate_profiles():
    profile_array = []
    file = open('usersLUFU.txt', 'r')
    file.readlines()
    end_of_file = file.tell()

    file.close()
    file = open('usersLUFU.txt', 'r')
    while file.tell() != end_of_file:
        name = file.readline()
        course = file.readline()
        school = file.readline()
        interests = file.readline()
        person = profile(name, course, school, interests)
        profile_array.append(person)
        file.readline()
    return(profile_array)

def profileDBEntry (profile_obj):
    usersFile = open('usersLUFU.txt', 'a')
    usersFile.write(str(profile_obj.userName)+ '\n')
    usersFile.write(str(profile_obj.userColl)+ '\n')
    usersFile.write(str(profile_obj.userCourse)+ '\n')
    usersFile.write(str(profile_obj.userInterests)+ '\n')
    usersFile.write('-----\n')
    usersFile.close()

def makeMatch(filter, profile_array):
    if filter == 'College':
        for acc in profile_array:
            if acc.userColl == Currentuser.userColl + '\n' and acc.userName != Currentuser.userName + '\n':

                return(acc)
    elif filter == 'Course':
        for acc in profile_array:
            if acc.userCourse == Currentuser.userCourse + '\n' and acc.userName != Currentuser.userName + '\n':
                print(Currentuser.userName)
                print(acc.userName)

                return(acc)
    elif filter == 'Interest':
        for acc in profile_array:

            if acc.userInterests[0] == Currentuser.userInterests[0] and acc.userName != Currentuser.userName + '\n':

                return(acc)
    else:
        return('Y')
     


def data_submitted(t):
    global Currentuser 
    Currentuser = profile(name_box.get(), coll_box.get(), dept_box.get(), intr_box.get().split(", "))
    global filter
    filter = filter_box.get()
    
    return(Currentuser)

def show_match(show_profile):
    root = tk.Tk()
    root.geometry("1000x1000")
    root.maxsize(1000, 1000)
    root.title('Lancaster University Frienship Union')
    root.configure(background = '#A4343A')
    title_label = tk.Label(root, text= 'Lancaster University Friendship Union',bg = '#A4343A', fg = '#FFFFFF', font =('Roman', 20, 'bold'))
    title_label.place(x = xy * 0.4, y =0)


    text_string = 'You matched with ' + show_profile.userName + '. They are a student at ' +show_profile.userColl + ' college of Lancaster University. They study at the ' + show_profile.userCourse + 'school and have an interest in ' + show_profile.userInterests[0] + '.'
    displayLabel = tk.Label(root, text = text_string, bg = '#A4343A', fg = '#FFFFFF', font =('Roman', 20, 'bold'))
    displayLabel.place(x= xy* 0.2, y = 0.5*xy)
    root.mainloop()



    
#Drawing the Details screen  
xy = 500

root = tk.Tk()
root.geometry("1000x1000")
root.maxsize(1000, 1000)
root.title('Lancaster University Frienship Union')
root.configure(background = '#A4343A')
title_label = tk.Label(root, text= 'Lancaster University Friendship Union',bg = '#A4343A', fg = '#FFFFFF', font =('Roman', 20, 'bold'))
title_label.place(x = xy * 0.4, y =0)
subtitle_label = tk.Label(root, text= 'Your Match is...', bg = '#A4343A', fg = "#FFFFFF", font =('Roman', 20, 'bold'))
subtitle_label.place(x = xy * 0.6, y= xy*0.7)

#Create Details area
name_label = tk.Label(root, text = "Name: ", font = ('Arial', 15, 'bold', ), bg = '#A4343A', fg = '#FFFFFF')
name_label.place(x = xy*0.05, y = xy*0.2)
name_box = tk.Entry(root, width = 20)
name_box.place(x = xy*0.2, y = xy*0.2)

coll_label = tk.Label(root, text = "College: ", font = ('Arial', 15, 'bold', ), bg = '#A4343A', fg = '#FFFFFF')
coll_label.place(x= xy*0.05, y = xy*0.3)
coll_box = tk.Entry(root, width = 20)
coll_box.place(x = xy*0.225, y = xy*0.31)

dept_label = tk.Label(root, text = "Department/School: " + str(name_box.get()), font = ('Arial', 15, 'bold', ), bg = '#A4343A', fg = '#FFFFFF')
dept_label.place(x= xy*0.05, y = xy*0.4)
dept_box = tk.Entry(root, width = 30)
dept_box.place(x = xy*0.45, y = xy*0.41)

intr_label = tk.Label(root, text = "Interests: ", font = ('Arial', 15, 'bold', ), bg = '#A4343A', fg = '#FFFFFF')
intr_label.place(x= xy*0.05, y = xy*0.5)
intr_box = tk.Entry(root, width = 40)
intr_box.place(x = xy*0.25, y = xy*0.51)


filter_label = tk.Label(root, text = 'Filter by: ', font = ('Arial', 15, 'bold', ), bg = '#A4343A', fg = '#FFFFFF')
filter_label.place(x = xy*1.25, y = xy*0.4)
filter_box = ttk.Combobox(state= 'readonly', values= ['College', 'Course', 'Interest'])
filter_box.place(x = xy*1.25, y = xy*0.5)

submit = tk.Button(root, text = 'Match', command = lambda t= 'button1 clicked': data_submitted(t))
submit.place(x = xy* 0.9, y = xy*0.6)


#Your match section
filter_label = tk.Label(root, text = 'Filter by: ', font = ('Arial', 15, 'bold', ), bg = '#A4343A', fg = '#FFFFFF')
filter_label.place(x = xy*1.25, y = xy*0.4)


    
root.mainloop()


#Backend driver
profileDBEntry(Currentuser)
profiles = instantiate_profiles()
profile_for_show = makeMatch(filter, profiles)
show_match(profile_for_show)







#Your match section











