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

# blobs are creatures with the ability to eat, reproduce, and die
# their genetics change how they function
class Blob:
    mature: bool = False
    agression: bool = False
    food: float = 1
    fed: bool = False

    def __init__(self,agression):
        self.agression = agression
    
    def feed(self,amount):
        # blobs will not eat food when already fed
        #print(self.fed)
        if self.fed == False:
            self.food = self.food+amount
            self.mature = True
            self.fed = True

    def reproduce(self):
        return Blob(self.agression)

    def die(self):
        self = None

# function that controls what happens when two blobs meet to feed
# an agressive blob meeting a peaceful blob gets 2 food, while the peaceful blob gets none
# peaceful blobs meeting get 1.5 food each
# agressive blobs meeting get 0.5 food each
def eat(blob0,blob1):
    if blob0==None:
        if blob1!=None:
            blob1.feed(1)
    elif blob1==None:
        blob0.feed(1)

    elif blob0.agression==False:
        if blob1.agression==False:
            blob0.feed(1.5)
            blob1.feed(1.5)
        elif blob1.agression==True:
            blob1.feed(3)
    
    elif blob0.agression==True:
        if blob1.agression==False:
            blob0.feed(3)
        elif blob1.agression==True:
            blob0.feed(0.5)
            blob1.feed(0.5)

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

# ---------Script!!!-----------
# creates an array of new blobs with random genes
blobs = []
i = 0
while i<200:
    num = random.randint(0,1)
    agressive: bool = False
    if num==0:
        agressive=True
    newBlob = Blob(agressive)
    blobs.append(newBlob)
    i=i+1

# runs until there is only one blob left
while len(blobs)>1:
    # set blob fed states to False
    for blob in blobs:
        blob.fed = False
    
    # feed blobs until they have all eaten
    foods = 100
    while foods>0 and allFed()==False:
        blob1=getHungryBlob(None)
        blob2=getHungryBlob(blob1)
        eat(blob1,blob2)
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
    
    # print update
    print(f"There are {len(blobs)} blobs")
    agressiveBlobs=0
    for blob in blobs:
        if blob.agression:
            agressiveBlobs = agressiveBlobs+1
    print(f"{agressiveBlobs} of them are agressive, {len(blobs)-agressiveBlobs} are not")
    time.sleep(1)

