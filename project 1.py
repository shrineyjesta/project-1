import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["name","age","contact number","email id:"])
        writer.writerow(info_list)
if __name__=='__main__':

    condition=True
    students=1
    while(condition):
        student_info=input("enter a information of a student {} in order name age number emailid".format(students))
        student=student_info.split(' ')
        print("splitup"+str(student))
        print("the entered info is \nname:{}\nage:{}\ncontactno:{}\nemailid:{}".format(student[0],student[1],student[2],student[3]))
        choice=input("do you want to edit this say yes or no")
        if(choice=="no"):
            write_into_csv(student)
        
            check=input("enter yes/no if youwant to enter another info")
            if(check=="yes"):
                condition=True
                students=students+1
            elif(check=="no"):
                condition=False
        elif choice=="yes":
            print("please reenter the info")
