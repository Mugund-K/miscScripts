import random

def fillList(listSize, minRange, maxRange):
    inputlist = []
    
    for i in range(0,listSize):
        el = random.randint(minRange, maxRange)
        inputlist.append(el)

    return inputlist

if __name__ == "__main__":
    list = fillList(10,1,10)
    print(list)
