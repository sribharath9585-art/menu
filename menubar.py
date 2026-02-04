d={}
l=[]
while True:
    print("======= Student Management System ======")
    print("1.Add a New Student")
    print("2.View All Student")
    print("3.Update Student Details")
    print("4.Delete a Student")
    print("5.Exit")
    print("========================================")
    choice=int(input("Enter your choice :"))

#adding details

    if(choice==1):
        add=int(input("How many details you want to add :"))
        for i in range(0,add):
            id=int(input("Enter Student ID :"))
            a=0
            t=True
            length=len(l)
            for j in range(0,length):
                if(id==l[a]):
                    print("Error : Student ID already exists!")
                    t=False                             
            if(t==True):
                name=input("Enter Name :")
                age=int(input("Enter Age :"))
                course=input("Enter Courses :")
                marks=input("Enter Marks :")
                d[id]=[name,age,course,marks]
                print("Student added successfully")
                print("-------------------------------")
                l.append(id)

 
 #display

    elif(choice==2):
        k=0
        v=True
        lent=len(l)
        a1=0
        for i in range(0,lent):
            value=d.get(l[a1])
            if(a1==0):
                print("-------- Student details --------")
            print("ID:",l[a1])
            print("Name:",value[k])  
            print("Age:",value[k+1]) 
            print("Course:",value[k+2]) 
            print("Mark:",value[k+3]) 
            print("----------------------------------")
            a1=a1+1
            v=False
        if(v==True):
            print("No student record found!")
          
#update

    elif(choice==3):
        f=True        
        no=True  
        for key,value in d.items():
            print(key,":",value)       
        le=len(l)
        mum=0
        while no==True:
            m=int(input("Student id to update :")) 
            if m not in d:
                print("Error : Student not found!")
            if m in d:
                for i in range(0,le):                    
                    if(l[mum]==m):
                        no=False
                        x=d.get(m)
                        while(f==True):
                            user=input("What you want to change?(name/age/course/mark) :")
                            user = user.lower()
                            if(user=="name"):
                                name1=input("Enter new name :")
                                x[0]=name1
                                f=False

                            elif(user=="age"):
                                age1=int(input("Enter new age:"))
                                x[1]=age1
                                f=False

                            elif(user=="course"):
                                course1=input("Enter new course:")
                                x[2]=course1
                                f=False

                            elif(user=="mark"):
                                marks1=int(input("Enter new marks:"))
                                x[3]=marks1
                                f=False

                            else:
                                print("Error : Invalid Choice!")
                    else:
                        mum=mum+1
            

#delete

    elif(choice==4):
        for key,value in d.items():
            print(key,":",value)
        
        hi=True
        while hi==True:

            n=int(input("Enter Student ID to Delete :"))
            if n in d:
                d.pop(n)
                l.remove(n)
                print("Record Deleted Successfully!")
                hi=False
            else:
                print("Error : Student not found!")

#exit

    elif(choice==5):
        print("----------------------------------------------")
        print("Thank you for using student management system!")
        print("Good boy 👋")
        break

    else:
        print("Invalid choice! Please try again")