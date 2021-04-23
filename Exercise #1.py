# Assume you have the list xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Write a loop that prints each of the numbers on a new line

for i in xs:
    print(i)

# Write a loop that prints each number and its square on a new line.

for i in xs:
    print(i,i**2)

# Write a loop that adds all the numbers from the list into a variable called total.
# You should set the total variable to have the value 0 before you start adding them up,
# and print the value in total after the loop has completed.

total=0
for i in xs:
    total+=i
print("Total:", total)

# Print the product of all the numbers in the list. (product means all multiplied together)

product=1
for i in xs:
    product*=i
print("Product:", product)