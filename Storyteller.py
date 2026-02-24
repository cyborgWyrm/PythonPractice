import random

nouns = ["cat","Eiffel Tower", "hospital", "code", "chair", "python", "shirt", "LED", "bar", "coffee", "java"]
verbs_for_objects = ["elect","make","dispell","pick","attack","destroy","love","enrage","organize","read","pet"]
verbs_no_objects = ["run","jump","sleep","think","rest","giggle","talk","consider","sit","walk","laugh"]
verbs_maybe_objects = ["cook","code","create","eat","drink"]
adjs = ["funny", "red", "hot", "cool", "intense", "excited", "happy", "mellow", "concerning", "coded", "purple"]
adverbs_for_adj = ["super","very","not","intrinsically","unusually","firmly","organically","sleepily","mega"]
articles = ["the", "a"]
connectors = ["and", "with", "beside", "above", "next to", "under"]

def random_sentance():
    ran = random.randint(0,1)
    if ran==0:
        return noun_verb()
    elif ran==1:
        return noun_verb_noun()

def noun_verb():
    return noun() + " " + verb_present(False)
    return "ERROR"
    
def noun_verb_noun():
    return noun() + " " + verb_present(True) + " " + noun()
    return "ERROR"

def article():
    return get(articles)
    return "ERROR"

def noun():
    ran = random.randint(0,2)
    if ran==0:
        return article() + " " + get(nouns)
    elif ran==1:
        return article() + " " + adj() + " " + get(nouns)
    elif ran==2:
        return noun() + " " + get(connectors) + " " + noun()
    #elif ran==3:
        #return article() + " " + get(nouns) + " that " + verb_past(False)
    #elif ran==4:
        #return article() + " " + get(nouns) + " that " + verb_past(True) + " " + noun()
    return "ERROR"

def adj():
    ran = random.randint(0,2)
    if ran==0 or ran==1:
        return get(adjs)
    elif ran==2:
        return get(adverbs_for_adj) + " " + adj()
    return "ERROR"

def verb(withObj):
    if random.randint(0,1)==0:
        return get(verbs_maybe_objects)
    if withObj==True:
        return get(verbs_for_objects)
    elif withObj==False:
        return get(verbs_no_objects)
    return "ERROR"

def verb_present(withObj):
    return verb(withObj) + "s"
    return "ERROR"

def verb_past(withObj):
    return verb(withObj) + "ed"
    return "ERROR"

def verb_future(withObj):
    return "will " + verb(withObj)
    return "ERROR"

def get(array):
    return array[random.randint(0,len(array)-1)]
    return "ERROR"

print(random_sentance())