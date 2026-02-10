# get a list of characters to sort
string: str = input("Say something: ")
array = list(string)

# count how many runthroughs it takes
runs: int = 0

# set number of changes to a large number to start
changes: int = 1000000

# run until you stop making changes to the list
while changes != 0:
    changes = 0
    runs = runs + 1

    # basically a for loop, check each pair and switch if a < b
    i: int = 0
    while i<len(array)-1:
        if array[i+1] < array[i]:
            array[i],array[i+1] = array[i+1],array[i]
            changes = changes + 1
        i = i+1

# print results
print(array + "\n")
print("It took me " + runs + " tries. Be proud of me.")