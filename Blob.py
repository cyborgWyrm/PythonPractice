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
    @staticmethod
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