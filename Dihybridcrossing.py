firstcross = input("First Dihybrid Cross: ")
secondcross = input("Second Dihybrid Cross: ")
def cross(mom, dad):
    mom=list(mom)
    dad=list(dad)
    splitone = []
    splittwo = []
    for i in range(0, 2):
        splitone.extend([mom[i] + mom[2], mom[i] + mom[3]]) #makes them into pairs of two RRYY into RY RY RY RY 
        splittwo.extend([dad[i] + dad[2], dad[i] + dad[3]])
    splitone = [letter for i in splitone for letter in i]
    splittwo = [letter for i in splittwo for letter in i]
    genotypes =[]
    for f in range(0,4):
        for s in range(0,4): # crosses them all over 
            genotypes.extend([splitone[2*f] + splittwo[2*s] + splitone[2*f+1] + splittwo[2*s+1]])
    sortcapitals=[]
    def spliter (lists): # this splits them in half basically so you can sort them individually like yY can turn into Yy
        new_list = []
        for lis in lists:
            lis_middle = (len(lis))//2
            first_half = lis[:lis_middle]
            second_half = lis[lis_middle:]
            new_list.append(first_half)
            new_list.append(second_half)
        return new_list
    
    sortcapitals = spliter(genotypes)

    newList = spliter(sortcapitals)
    upper = []
    lower = []
    for p in range(0, len(newList),2):
            if newList[p].islower() & newList[p+1].isupper():
                upper.append(newList[p+1])
                lower.append(newList[p])
            else:
                upper.append(newList[p]) 
                lower.append(newList[p+1])
    sortedsepcapitals=[]
    for i in range(0, len(upper)):
        sortedsepcapitals.append(upper[i] + lower[i])
    def joiner(lists):
        middlelist =[]
        middlelist = (len(lists)//2)
        i = 0
        while i < middlelist:
            lists[(0+i) : (2+i)] = [''.join(lists[(0+ i) : (2+i)])]
            i = i + 1
        return lists
    sortednonsepcapitals=joiner(sortedsepcapitals)
    uniqueones = set(sortednonsepcapitals)
    uniquelist = []
    for number in uniqueones:
        uniquelist.append(number)
    numberof = []
    for i in range(len(uniquelist)): #can't append and add at the same time so just flood it with the same number of zeroes as the unique list length
        numberof.append(0)
    for u in range(0, len(uniquelist)): #basically comparing the number of unique ones to the actual list and compiling it
        for s in range(0, len(sortednonsepcapitals)):
            if uniquelist[u] == sortednonsepcapitals[s]:
                numberof[u] = numberof[u]+1
    return(uniquelist, numberof)
uniquelist, numberof = cross(firstcross,secondcross)
for i in range(0, len(uniquelist)):
    print(str(numberof[i]) + "/16" + " " + str(uniquelist[i])) #printing it all out