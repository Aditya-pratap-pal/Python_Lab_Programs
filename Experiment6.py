# To use dictinary and make a dictionary of faculty and students and store them seprately in lists.
dict1=dict()
def additemsindict(a,b,c):
    dict1[a]={"Faculty":b,"Student":c}

while 1==1:
    deptname=input("Enter the name of department : ")
    fname=input("Enter the name of the faculty : ")
    sname=input("Enter the name of the student : ")
    additemsindict(deptname,fname,sname)
    choice=int(input("are you done(1 for yes,0 for no) : "))
    if(choice==1):
        break
    else:
        pass
print(dict1)

student_list=[]
faculty_list=[]

for i in dict1.keys():
    student_list.append(dict1[i]["Student"])
    faculty_list.append(dict1[i]["Faculty"])

print(student_list)
print(faculty_list)
