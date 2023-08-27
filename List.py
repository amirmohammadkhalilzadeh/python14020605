number_list = []
n = int(input("How many number do you have? "))             # Enter your number of numbers
print("\n")
for x in range(0, n):
    item = int(input("Enter number "+ str(x+1) + ": "))     # Enter the number X
    number_list.append(item) 
    print("User list is ", number_list)                     # Print the list