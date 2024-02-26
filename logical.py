#AND operator
# Example 1 
x = 5
print(x > 3 and x < 10) # True because both condition are ture

#Example 2 
y = 12
print(y > 10 and y % 5 ==0)#False beacuse the second condition is false

# OR operator
#Example 1
x = 5
print(x < 3 or x > 10)#False because both the condition are false

#Example 2
y = 12
print(y < 10 or y % 2 == 0 )#True because second conditioon is true

# NOT operator
#Exampple 1 
x = 5
print(not( x > 3 and x < 10))#Fasle because the condiotion inside the not is true

#Example 2
y = 12
print(not(y > 10 and y % 5 == 0))#True because th econdition inside the not is false