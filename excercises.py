# x = 0
# for x in range(0,11):
#     print(x)              ex 1

# lastNumber = 6
# for row in range(1, lastNumber):
#     for column in range(1, row + 1):
#         print(column, end=' ')
#     print("")         ex 2

# x = int(input())
# suma=0
# for y in range(0,x+1):
#     suma=suma+y
# print(suma)       ex 3

# x=int(input())
# for x in range(1,11):
#     x=x+x
#     print(x)      ex 4

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for element in list1:
#     if element%5==0 and element<=150:
#         print(element)        ex 5

# x=int(input())
# s=str(x)
# list(s)
# suma=0
# for z in list(s):
#     suma=suma+1
# print(suma)           ex 6

# for y in range(5,0,-1):
#     for x in range(y,0,-1):
#         print(x, end=" ")
#     print()       ex 7

# list1 = [10, 20, 30, 40, 50]
# for index in range(4,-1,-1):
#     print(list1[index])       ex 8

# for x in range(-10,0):
#     print(x)      ex 9

# print("Fibbonacci sequence: ")
# prev=0
# last=1
# print(0)
# print(1)
# for x in range(0,10):
#     temp=last
#     last=temp+prev
#     prev=temp
#     print(last, end=" ")      ex 12

# x=int(input())
# o=1
# for z in range(1,x+1):
#     o=z*o
# print(o)      ex 13

# x=int(input())
# s=str(x)
# list(s)
# for i in range(len(list(s))-1,-1,-1):
#     print(list(s)[i], end=" ")        ex 14

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for e in range(1,10,2):
#     print(my_list[e])     ex 15

# print("input_number = ", )
# x=int(input())
# o=1
# for z in range(1,x+1):
#     o=z*z*z
#     print("Current number is : ", z, "and the cube is: ", o)      ex 16

# print("number_of_terms= ")
# x=int(input())
# sum=0
# for z in range(1,x+1):
#     u=int('2'*z)
#     sum+=u
# print(sum)        ex 17

# for x in range(0,6):
#     print(x*"*")
# for z in range(6,0,-1):
#     print(z*"*")      ex 18

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# y=hour+(dura//60)
# x=mins+(dura%60)
# if x>=60:
#     y+=1
#     x-=60
#
# print(y,":","{:02d}".format(x))

# myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# newList = []
# for number in myList:  # Browse all numbers from the source list.
# 	if number not in newList:  # If the number doesn't appear within the new list...
# 		newList.append(number)  # ...append it here.
# myList = newList[:]  # Make a copy of newlist.
# print("The list with unique elements only:")
# print(myList)

# try:
#     raise Exception
# except BaseException:
#     print("a")
# except Exception:
#     print("b")
# except:
#     print("c")

# def o(p):
#     def q():
#         return '*' * p
#     return q
#
# r=o(1)
# s=o(2)
# print(r()+s())

