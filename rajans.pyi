# v = input("Enter a vehical type: ")
# t1 = int(input("Enter a time of entry: "))
# t2 = int(input("Enter a time of exit: "))
# T = t2-t1
# if v == "car":
#     Am = 50
# elif v == "van":
#     Am = 100
# else:
#     Am = 20
    
# Tot = Am * T
# print("\n type of vehicle :-", v)
# print(" amount per hour :-", Am)
# print(" total time :-", T)
# print("Parking Fee :-", Tot)

# x = [5,2,8,1,7]
# for i in range(len(x)-1):
#     for j in range(len(x)-1-i):
#         if x[j] > x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
#             print(x)

A = int(input("Enter a number:"))
B = 0
while(A > 0):
 C = A % 10
 B =   str(B) + str(C)

 A = A // 10 # // is integer division
print(B)