d={}
while True:
    print("1.ADD")
    print("2.DIPLAY")
    print("3.UPDATE")
    print("4.DELETE")
    print("5.EXIT")
    num=int(input("Enter the choice as a number :"))
    if(num==1):
        size=int(input("How many student details you want add :"))
        for i in range(0,size):
            key=int(input("Enter the rollno:"))
            name=input("Enter the name:")
            mark=int(input("Enter the mark:"))
            d[key]=name,mark
    
    elif(num==2):
        print(d)

    elif(num==3):
        print(d)
        change=int(input("which roll no details want to change :"))
        name1=input("Enter the modify name :")
        mark1=int(input("Enter the modify mark :"))
        d[change]=name1,mark1
    
    elif(num==4):
        print(d)
        n=int(input("which roll no you want to delete :"))
        d.pop(n)

    elif(num==5):
        print("Exited Succesfully")
        break
    else:
        print("/* Inavlid Choice */")

#commmit