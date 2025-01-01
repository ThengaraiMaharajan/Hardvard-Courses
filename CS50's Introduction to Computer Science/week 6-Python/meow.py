def main():
    iteration = int(input("Enter the number of times you want to print meow: "))
    meow(iteration)

def meow(iteration):
    for i in range(iteration):
        print("meow")

main()