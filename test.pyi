# def modify_list(lst):
#  lst = lst + [10]
#  return lst
# my_list = [1, 2, 3]
# my_list = modify_list(my_list)
# print(my_list)  # Output: [1, 2, 3, 10]

# i = 1
# total = 0
# while i <= 5:
#  if i % 2 == 0:
#   total += i * 3
#  else:
#   total += i * 2
# i += 1
# print(total)
# x = open("test.txt","a")
# x.write("Hello, World!\n", "This is a test file.\n")
# x.close()
 
 
# y = open("test.txt", "a")
# y.write("Hello, World!\n")
# y.write("This is a test file.\n")
# y.close()


# def largennumber(a,b):
#    if a > b:
#        print("a is larger")
#    else:
#        print("b is larger")
#    return None   
# largennumber(0,-1)

# x = [1,2,3,4,5]
# for i in range (len(x)-1):
#     for i in range (len(x)-1-i):
#         if x[i] < x[i+1]:
#             x[i], x[i+1] = x[i+1], x[i]
# print(x)

# def number(num):
#     print(num **2)
# x = int("hello")
# y = int("wolrd")
# print(x+y)

# units  = int(input("enter the  number of units:"))
# total_price = 0
# payment = 0
# total_price1 = 0
# total_price2 = 0
# def calculation_units(units):
#     if units >= 64:
#         total_price1 = units*10 + units*5
#     else:
        
#         total_price2 = units*5
#         total_price = int(total_price1 + total_price2)
#         print("the total price is:", total_price)
        
   
# calculation_units(units)

# units = int(input("Enter the number of units: "))

# def calculation_units(units):
#     if units > 64:
#         total_price = units * 10 + units * 5 # 10 + 5 per unit combined as example
#     else:
#         total_price = units * 5
#     print("The total price is RS:", total_price) 
#     f = open("elcticity_bill.txt", "a")
#     print("the total price is rs:", total_price, file=f)
#     f.close()



# calculation_units(units)

# l = list(map(int, input().split()))
# k = int(input())

# print("hello" if k in l else "false")

# def check_in_list(lst, k):
#     if k in lst:
#         return "hello"
#     else:
#         return "false"
# lst = list(map(int, input().split(",")))    
# k = int(input())
# print(check_in_list(lst, k))





# this is a positive negtive number check in python(usinig if else statement)

# n = int(input("enter the number:"))
# if n > 0:
#     print("this is a positive")
# else:
#     print("this is a negative")
    
# this is a positive negtive number check in python(usinig function)

    
# n = int(input("enter the number:"))
# def check_number(n):
#     if n > 0:
#         print("this is a positive")
#     else:
#         print("this is a negative")
# check_number(n)        


# n = int(input("enter the number:"))
# if n > 0 :
#     print("this is a positive")
# elif n < 0:
#     print("this is a negative")
# else:
#     print("this is zero")\



# c =int(input("enter the number:"))
# x = 0 
# s = 0
# while x <= c:
#     zs = float(input("enter the number:"))
#     zs1 = float(input("enter the number:"))
#     x = x + 1
#     if zs < 1.5:
#         print(" qualified")
#         s = s + 1
#     else:
#         print("not qualified")
# print("total qualified students:", s)    


# index = int(input("enter the index:"))  
# name = input("enter the name:")
# house_no = index % 4
# if house_no == 1:
#     house = "perakum"
# elif house_no == 2:
#     house = "wijaya"    
# elif house_no == 3:
#     house = "gemunu"
# else:
#     house = "gajaba"
#     print("student 's  name , index and house are:", name,index,house)       



# n =  int (input("enter the number:"))
# for c in range (n):
#     index  = int(input("enter the index:"))
#     name = input("enter the name:")
#     house_no = index % 4
#     if house_no == 1:
#         house = "perakum"
#     elif house_no == 2:
#         house = "wijaya"    
#     elif house_no == 3:
#         house = "gemunu"
#     else:
#         house = "gajaba"
#     print("student 's  name , index and house are:", name,index,house)    


  
# name = input("enter the NAME:")
# N = float(input("enter the IN kg WEIGTH number:"))
# H = float(input("enter the HEIGTH IN CM:"))
# H2 = H / 100
# BMI = N / (H2**2)
# BMI = N / (H2 * H2)
# b = BMI
# if b>= 30:
#     print("obese")
# elif 25 >=b>=29.9:
#     print("overweight")
# elif 18.5 >=b>=24.9:
#     print("normal weight")
# else:
#     print("underweight")
    
# F = open("bmi.txt", "a")
# print(name, " this man bmi is :", b, file=F)
# F.close()


# my_list = list(map(int, input("enter the numbers:").strip() .split(",")))
# max_num = int(input("enter the max number:"))
# for i in  len(my_list):
#     if my_list[i] > max_num:
#         print(my_list[i])
   
    
# n = int(input("enter the start number: "))
# m = int(input("enter the end number: "))
# count = 0

# number_list = list(range(n, m + 1))
# for num in number_list:
#     if num % 2 == 0:
#         count += 1
#         print(num)
    
# print("Total even numbers:", count)


# def new_func():
#     count = 0 
#     l = [20,20,20,20,40,50, 70,20,50,40,20]
#     for i in range(len(l)):
#         if l[i] == 20:
#             count += 1
#     print(count)

# new_func()

# first = str(int(input("enter the first number:")))
# last = str(int(input("enter the last number:")))
# first_01 = int(first)
# last_01 = int(last)
# f = int(first[0])
# l = int(last[-1])
# def number_list(f,l):
#   while True:
        
#    if f == l:
#        first = first_01 + 1
#        last = last_01 + 1
#    print(first, last)

# name = input("enter the name:")
# answer = ["1-A","2-B","3-C","4-D","5-E","6-F","7-G","8-H","9-I","10-J"]
# count = 0
# i = 0
# quzno = int(input("enter the quz number:"))
# ans =[quzno, "- ",input("enter the answer:")]
# if quzno < len(answer):
#    if ans == answer[i]:
#       count += 1
#       i += 1
    
#       if count >=7:
#         print(name, "your selected")
#       else:
#         print(name, "your not selected")
# else:
#     print("invalid quz number")       

# corlist=['A', 'C','D', 'B', 'A', 'A', 'C', 'C', 'B', 'D']





#  corcount=0

#  incorcount=0

# anslist=input("Enter list : ").split(',')

# for x in range (10):

#  if anslist [x]==corlist[x]:

#   corcount+=1

#  else:
#    incorcount+=1

# print("Correct Answers: ", corcount)

# print ("Incorrect Answers : ", incorcount)

# if corcount>=7:

#   print("You are selected")

# else:
#  print ("You are not selected")






# print()
# lst = input("Enter elements separated by space: ").split()

# f1 = open("results.txt", "a")
# f1.write(str(lst) + "\n")
# f1.close()


# salary = float(input("Enter your salary: "))
# date = int(input("Enter the date you worked: "))
# alowance = 0
# total_salary = 0
# if date >= 30:
#     alowance = salary * (15/100)
#     total_salary = salary + alowance
#     print("Total salary with allowance:", total_salary)
# elif 25 <= date < 30:
#     alowance = salary * (10/100)
#     total_salary = salary + alowance  
#     print("Total salary with allowance:", total_salary)
# else:
#   print("No allowance awarded.")      


# list1 = [1, 2, 3, 4, 5]
# print(list1[:2:2])
# 


# f1 = open("results.txt", "r")
# conten = f1.readline()
# f2 = open("data_copy.txt", "w")
# f2.write(conten)
# f1.close()
# f2.close()
# print("File copied successfully.")

# x = (2, 4, 6, 8, 10, 12,14)
# print(x[-1:])


# def max_num(a,b):
#     if a > b:
#         print("this is largest number",a)
#     else:
#         print("this is largest number",b)
        
        
# num_1 = int(input("enter the first number:"))
# num_2 = int(input("enter the second number:"))
# max_num(num_1,num_2)

# i= 0
# j= 0
# n_1 = int(input("enter the first number:"))
# n_2 = int(input("enter the second number:"))
# count = 0
# if n_1 < n_2:
#     firstrow = n_1  +  i
#     i = i + 1
#     firstrowcount = count + 1
#     secondrow = n_2  -  j
#     j = j + 1
#     secontrowcount = count + 1


#     if firstrowcount == secontrowcount:
#         print(firstrow )
#         print(secondrow)
#         print(" end tha loop")
  
  
# else:
#      print("plese re enter the number")
#      n_1 = int(input("enter the first number:"))
#      n_2= int(input("enter the second number:"))
     
list_1 = [1, 2, 3, 4, 5,8,9,12,56]
total = sum(list_1)
avg = round(total / len(list_1),2)
print ('the average of the list is:', avg)
for  i in range (len(list_1)):
    if list_1[i] > avg:
        print('the numbers greater than average are:', list_1[i])
        largest = list_1[i]
    else:
            continue
        
        
f1 = open("results.txt", "w")
f1.write("the largest number is:" + str(largest) + "\n" +"the average is:" + str(avg) + "\n")
f1.close()