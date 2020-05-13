#
# Example file for working with loops
#

def main():
    x = 0

    # Define a while loop
    
    # while(x < 5):
    #     print(x)
    #     x = x+1
    # print("\n")
    
    # Define a for loop
    
    # for x in range(5,10):
    #     print(x)
    # print("\n")
    
    # Use a for loop over a collection
    
    # days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    # for d in days:
    #     print(d)

    # Use the break and continue statements

    # for x in range(5,10):
    #     # if(x==7): break
    #     if(x % 2 == 0): continue
    #     print(x)

    # Using the enumerate() function to get index
    days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)

if __name__ == "__main__":
    main()