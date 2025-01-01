# c = input("Do you Agree ? 'Yes' or 'No' : ")
# if c == 'y' or c == 'Y':
#     print("Agreed")
# elif c == 'n' or c == 'N':
#     print("Not Agreed")
# else:
#     print("Invalid Input")

# c = input("Do you Agree ? 'Yes' or 'No' : ")
# if c in ['y', 'Y', 'yes', 'Yes', 'YES']:
#     print("Agreed")
# elif c in ['n', 'N', 'no', 'No', 'NO']:
#     print("Not Agreed")
# else:
#     print("Invalid Input")

c = input("Do you Agree ? 'Yes' or 'No' : ")
c = c.lower()
if c in ['y', 'yes']:
    print("Agreed")
elif c in ['n', 'no']:
    print("Not Agreed")
else:
    print("Invalid Input")

# c = input("Do you Agree ? 'Yes' or 'No' : ").lower()