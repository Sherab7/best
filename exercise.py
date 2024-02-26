#Exercise
A = int(input("Enter your age: "))
S = input("Are you student?(yes / no ):")

if  A <= 12:
    print("eligible for discount")

elif (A >= 13 or A <= 18) and S == "yes" :
    print("eligible for discount")

else: 
    print("not eligible for discount")