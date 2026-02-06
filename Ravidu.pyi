# x = (10+20)*3 - (50//5) + (100 % 15) + (2**5)
# print(x)

# car_1 = 120
# car_2  = 400
# if car_1 < car_2 :
#     print("car_2 is fast")
# else :
#     if car_1 > car_2 :
#         print("car_1 if fast")
#     else :
#         print("car_1 and car_2 same")    
       
# maths = 50
# sceience = 50
# english   = 100
# avg = (maths + sceience + english) / 3
# if maths and sceience > 40:
#     print("studen pass maths and science")
# else :
#     print("student failled maths and science")

# print (avg )
 
# blacnce = 1000
# money = int(input("$"))
# doller = blacnce//10
# if money >= 500:
#     blacnce += money
#     print("crunnet balnce",blacnce)
# else:
#     if money <= 200:
#         blacnce -= money
#         print("crunnet balnce",blacnce)
#     else:
        
#         blacnce -= money
#         print("crunnet balnce",blacnce)
# print(doller)


# n =  int(input ("number"))
# if n > 0:
#     print("positive")
# else:
#     print("negative")
    
    
# full_name = "JohnDoe" 
# first_name = full_name[:full_name.index(" ")] 
# print("First name:", first_name) 


# name = str(input("name ="))
# email = name.lower() + "@email.com"
# print("Email =",email)

# input_ex = "   hello ,  world    "
# celan_iput = input_ex.split
# print(celan_iput())

# description = "this is a bard new product in this shop"
# updatet_description = description.replace("bard new" , " fack one")
# print("update description",updatet_description)

# pragrah = "T like python to becuse python is very easy to understainding python can be code using free softwaer pytho python python "
# extits = pragrah.find("pythoyn") != -1
# coutable = pragrah.count("python")
# print("ther are no python word",extits)
# print("there are have python word like =",coutable)

# name = "thejan"
# age = 18
# nick_name = "gemba"
# message = f"Hello {name}, you are {age} years old nick name is {nick_name}."
# print("call nick name is",message)


# items = "apple , mango , orange , lemon"
# new_item =  items.split(",")
# print("new iteam lis are ",new_item)


# value = input("input value name or age")
# if value.isalpha():
#     print(" vaild name")
# elif value.isdigit():
#     print("is valid age")
# else:
#     print("invalid value")



# customers = ["Alice", "Bob", "Charlie", "Diana", "Eve"] 
# print("Second customer:", customers[1]) 
# print("Fourth customer:", customers[3]) 
# print("All# log_file = "log.txt" except the first:", customers[1:]) 



# total_hours = 0 
# max_hours = 0 
# max_day = "" 

# for line in data:
#     date , hours=  line.strip().split(", ")
#     hours =+ int(hours)
#     total_hours =+ hours
#     if hours > max_hours:
#         max_hours = hours
#         max_day = date

# print(f"Total hours worked in the week: {total_hours}") 
# print(f"Day with maximum hours worked: {max_day} ({max_hours} hours)")
# file = open("G:\\log\log.txt","a")
# file.write("2025-01-01, 8 2025-01-02, 6 2025-01-03, 7 2025-01-04, 5 2025-01-05, 9 2025-01-06, 4 2025-01-07, 8")
# file = open("G:\\log\log.txt","r")
# data = file.readline()
# file.close()

# total_hours = 0 
# max_hours = 0 
# max_day = "" 


# for line in data:
#    date   = line.strip().split(", ")
#    hours = line.strip().split(", ")

# hours = int(hours) 
# total_hours += hours 
# if hours > max_hours: 
#      max_hours = hours 
#      max_day = date
# print(f"Total hours worked in the week: {total_hours}") 
# print(f"Day with maximum hours worked: {max_day} ({max_hours} hours)")


# name= 'Piumi'  
# age=16 
# print('My name is' +age)

# inlist = int(input("positive"))
# k = int(input("positive"))

B = (1,2,3,4,5)
B.__reversed__()
print(B)