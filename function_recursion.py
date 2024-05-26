def sum_of_digits(n):
    if n < 10 :          # Base case: If n in a single-digit number, return n
        return n
    
    else:      #Recursive case: Calculate the sumn of digits
        last_digit = n % 10        # Get the last digit of n
        remaining_digits = n // 10 # Get the remaining digit by integer division with 10
        return last_digit + sum_of_digits(remaining_digits) #Recursively call the function with the ramaining digits
                                                            #and add the last digit to the result

print(sum_of_digits(123))
                            