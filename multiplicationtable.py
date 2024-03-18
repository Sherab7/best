
number = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit up to which you want the table generated: "))

# Generate the multiplication table
print(f"Multiplication table for {number} up to {limit}:")
for i in range(1, limit+1):
    result = number * i
    print(f"{number} x {i} = {result}")