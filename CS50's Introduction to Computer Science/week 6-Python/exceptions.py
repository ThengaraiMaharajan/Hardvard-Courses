def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("Not an integer. Please try again.")
            pass

def main():
    x = getInt("x: ")
    y = getInt("y: ")
    print("You entered:", x+y)

main()