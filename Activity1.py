# Program to check if a number is the power of 2

def power2(number):
    # A power of 2 has only one bit set in the binary representation 
    if number <= 0: # 0 or negative are not power2 of 2
        return False 
    # Check using the (number & (number - 1)) == 0 property
    return (number & (number -1)) == 0

# Take input from the user
number = int(input("Enter the nunber: "))

# Check and print the result
if power2(number):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")