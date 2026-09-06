"""
Ideas:
fast forward: runs without wait for a set number of times to check if population is stable or goes to zero
add food, remove food from command line
reproductive genetics
more types of feeding genetics
breeding instead of mitosis
"""

# imports
import random
import time
from Blob import Blob
from pynput import keyboard


# checks if all blobs have been fed (returns False if there are more than 1 unfed blobs)
def allFed():
    foundOne = False
    for blob in blobs:
        #print(blob.fed)
        if foundOne==False:
            foundOne=True
        elif blob.fed==False:
            return False
    return True

# returns a random hungry blob that is not notThisOne
# if there there is less than 2 hungry blobs total, returns None
def getHungryBlob(notThisOne: Blob):
    hungryBlobs = []
    for blob in blobs:
        if blob.fed==False:
            hungryBlobs.append(blob)
    
    if len(hungryBlobs)<2:
        return None
    
    num = random.randint(0,len(hungryBlobs)-1)
    if hungryBlobs[num] == notThisOne:
        return getHungryBlob(notThisOne)
    return hungryBlobs[num]

def averageFood():
    sum = 0
    for blob in blobs:
        sum = sum + blob.food
    return sum/len(blobs)

def run():
    # set blob fed states to False
    for blob in blobs:
        blob.fed = False
    
    # feed blobs until they have all eaten
    foods = initialFood
    while foods>0 and allFed()==False:
        blob1=getHungryBlob(None)
        blob2=getHungryBlob(blob1)
        if blob1!=None and blob2!=None and (blob1.fed==True or blob2.fed==True):
            print("---------A BLOB IS CHEATING!--------")
        Blob.eat(blob1,blob2)
        foods = foods-3
        #print(allFed())
    
    # run through blobs
    index=0
    for blob in blobs:
        # make blobs lose one food (energy used)
        blob.food = blob.food-1
        # blobs die if food<0
        if blob.food<0:
            blob.die()
            blobs.pop(index)

        # blobs reproduce
        if blob.food>2 and blob.mature:
            blob.food = blob.food-2
            blobs.append(blob.reproduce())
        index=index+1

def runToInfinity():
    average = len(blobs)
    i=0
    while i<1:
        i=i+1
        run()
        average = (average + len(blobs))/2

    if abs(average-len(blobs)) < 5:
        print(f"stable at about {average}\n\n\n")
    else:
        print("not stable\n\n\n")
    endDay = True



waitTime = 1
endDay = False

# ---------Script!!!-----------
# asks user for information
initialBlobNum = int(input("How many blobs initially exist? "))
initialFood = int(input("How much food is avaliable? "))


# creates an array of new blobs with random genes
blobs = []
i = 0
while i<initialBlobNum:
    num = random.randint(0,2)
    agressive: bool = False
    if num==0:
        agressive=True
    newBlob = Blob(agressive)
    blobs.append(newBlob)
    i=i+1

def on_key_press(key):
    if hasattr(key, "char") and key.char == "s":
        runToInfinity()
keyboard_listener = keyboard.Listener(
    on_press=on_key_press)
# start the listener
keyboard_listener.start()

# runs until there is only one blob left
while len(blobs)>1 and (endDay == False):

    # run a day for blobs
    run()

    
    # print update
    print(f"There are {len(blobs)} blobs")
    print(f"They have {averageFood()} food on average")
    agressiveBlobs=0
    for blob in blobs:
        if blob.agression:
            agressiveBlobs = agressiveBlobs+1
    print(f"{agressiveBlobs} of them are agressive, {len(blobs)-agressiveBlobs} are not")
    time.sleep(waitTime)
