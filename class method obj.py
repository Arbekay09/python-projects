class Employee:
    def __init__(self,name,id,Department="Engineer"):
        self.name = name
        self.id= id
        self.Department=Department
    def empdetails(self):
        return ("Name: " +self.name +"  " +"ID: " +self.id +" " +"Department: " + self.Department)

emp1= Employee("Rahul","07")
emp2 = Employee("Rohit","08")
emp3 =Employee("viswa","09")
emp4 = Employee( "Anish","10")
emp5= Employee("Ashok","11")

# print("EMPLOYEE TIME DETAILS")
# print(emp1.empdetails() +"\n" + emp2.empdetails()+"\n"+ (emp3.empdetails() +"\n"+ (emp4.empdetails() +"\n"+(emp5.empdetails() )


# print(emp1.empdetails())
# print(emp2.empdetails())
# print(emp3.empdetails())
# print(emp4.empdetails())
# print(emp5.empdetails())

class part(Employee):
    def __init__(self,duration,salary):
        self.duration=duration
        self.salary=salary

    def par(self):
        return ("Duration" + self.duration+ " " +"Salary" + self.salary)
par1= part("3 hours ","23000")
par2= part("6 Hours","32000")


# print("PART TIME DETAILS")
#
# print( emp1.empdetails()+" " +par1.par() )
# print( emp2.empdetails()+" " +par2.par() )
#

class full(Employee):
    def __init__(self,manager,salary):
        self.manager= manager
        self.salary=salary
    def fulldetails(self):
        return("Manager: " + self.manager +"  "  +"Salary"+ self.salary)
full1= full("Gopi","40000")
full2= full("Gopi","40000")
full3= full("Arjun","45000")

# print("FULL TIME DETAILS")
# print(emp3.empdetails() +" " + full1.fulldetails())
# print(emp4.empdetails() +" " + full2.fulldetails())
# print(emp5.empdetails() +" " + full3.fulldetails())



#









































#
# class Employee(object):
#     def __init__(self,ID,Name,Department="Engineer",):
#         self.ID= ID
#         self.Name = Name
#         self.Department = Department
#     def empdetails(self):
#         print("ID :" + self.ID + " Name :" + self.Name + " Department : " + self.Department)
# emp1= Employee("01","Rahul")
# # print(emp1.empdetails())
# # emp2= Employee("02","Ashok")
# # emp3 =Employee("03","viswa")
# # emp4 = Employee("04", "Anish")
#
# class Part_time(Employee):
#     def __init__(self,Duration,Total_Payout):
#         self.Duration = Duration
#         self.Total_Payout= Total_Payout
#     def partdetails(self):
#         return ("Duration" + self.Duration+ " " +"Salary" + self.Total_Payout)
#
# # par1 = Part_time("50 hours", "24000")
# # print(emp1.empdetails())
# # pt2 = Part_time("50 hours","24000")
# # print(pt2.partdetails())
#
# class Full_time(Employee):
#     def __init__(self,ID,Name,Manager,Salary):
#         self.ID = ID
#         self.Name = Name
#         self.Manager=Manager
#         self.Salary=Salary
#     def info(self):
#         print("ID :" + self.ID + " Name :" + self.Name + " Manager : " + self.Manager + "Salary :" + self.Salary)
#         # print("Manager of the Employee is : " + self.Manager)
#         # print("Salary of the Employee is : " + self.Salary)
#
#
#
# #
# #
#
# # # #
# # pt1 = Part_time("01","Rahul","50 hours", "24000")
# # pt1.info()
# # pt2 = Part_time("02","Ashok","50 hours","24000")
# # pt2.info()
# #
# # ft1 = Full_time("03","Viswa","Gopi","40000")
# # ft1.info()
# # ft2 = Full_time("04","Anish","Arjun","45000")
# # ft2.info()
#
#
#
#
#
#  # print("ID of the Employee is :" + self.ID )
#         # print("Name of the Employee is :" + self.Name)
#         # print("Work duration of the employe: " + self.Duration)
#         # print("Total Payout of the employe: " + self.Total_Payout)