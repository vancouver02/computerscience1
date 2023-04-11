def reverse(number):
    return int(str(num)[::-1])

num = int(input("Enter a value => "))
print(num)

# Perform the parlor trick
rev_num = reverse(num)

diff = abs(num - rev_num)
rev_diff = reverse(diff)
result = diff + rev_diff

# Print the steps of the computation
print(num)
print("Here is the computation:")
print(f"{max(num, rev_num)} - {min(num, rev_num)} = {diff}")
print(f"{diff} + {rev_diff} = {result}")

# Check if the result is 1089 and print the appropriate message
if result == 1089:
    print("You see, I told you.")
else:
    print("Are you sure your input is valid?")
