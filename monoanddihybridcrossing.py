question = input("Monohybrid(M) cross or Dihybrid(D) cross? ")
if question == "M":
    firstcross = input("First Monohybrid Cross: ")
    secondcross = input("Second Monohybrid Cross: ")
    crossedgenotypes = []
    uniqueset = []
    uniquelist =[]
    splitone = list(firstcross)
    splittwo = list(secondcross)
    for f in splitone:
        for s in splittwo:
            crossedgenotypes.append(f + s)
    uniqueset = set(crossedgenotypes) #alr so set basically mixes it up but it doesn't matter since the numberoflists matches up and nobody cares abt the order 
    for thing in uniqueset:#converts from set to list "uniqueset" is really just a useless middleman
        uniquelist.append(thing)
    numberof = []
    for i in range(0, len(uniquelist)):
        numberof.append(0)
    for u in range(0, len(uniquelist)):
        for a in range(0, len(crossedgenotypes)):
            if uniquelist[u] == crossedgenotypes[a]:
                numberof[u] = numberof[u] + 1
    def sortcapitals(list):
        newlist = []
        for item in list:
            for character in item:
                newlist.append(character)
        upper = []
        lower = []
        for i in range(0, len(newlist), 2):
            if newlist[i].isupper():
                upper.append(newlist[i])
                lower.append(newlist[i+1])
            elif newlist[i].islower() & newlist[i+1].isupper():
                upper.append(newlist[i+1])
                lower.append(newlist[i])
            elif newlist[i].islower() & newlist[i+1].islower():
                upper.append(newlist[i])
                lower.append(newlist[i+1])
            sorted = []
        for x in range(0, len(upper)):
            sorted.append(upper[x] + lower[x])
        return sorted
    uniquelist = sortcapitals(uniquelist)
    print("Punnet Square")
    separator = "----+----"#incredibly ugly way to do this btw 
    print("    " + splitone[0] + "    " + splitone[1])
    print("   " + separator)
    for x in range(0,len(splitone)): 
        print(splittwo[x] + " " + '|' + " " + crossedgenotypes[x] + " " + '|' + " " + crossedgenotypes[x+2])
        print("   " + separator)
    for x in range(0, len(uniquelist)):
        print(str(numberof[x]) + "/4 " + str(uniquelist[x]))
elif question == "D":
    firstcross = input("First Dihybrid Cross: ")
    secondcross = input("Second Dihybrid Cross: ")
    def sameline(list,string):#makes something like 'a','b' into "a b"
        newlist = []
        for i in range(0, len(list)):
            newlist.extend([list[i], string])
        return newlist
    def cross(mom, dad):
        mom=list(mom)
        dad=list(dad)
        splitone = []
        splittwo = []
        for i in range(0, 2):
            splitone.extend([mom[i] + mom[2], mom[i] + mom[3]]) #makes them into pairs of two RRYY into RY RY RY RY
            splittwo.extend([dad[i] + dad[2], dad[i] + dad[3]])
        newsplitone = [letter for i in splitone for letter in i]
        newsplittwo = [letter for i in splittwo for letter in i]# makes them all into individual letters 
        genotypes =[]
        for f in range(0,4):
            for s in range(0,4): # crosses them all over corresponding r's to r's y's to y's in groups of 4
                genotypes.extend([newsplitone[2*f] + newsplittwo[2*s] + newsplitone[2*f+1] + newsplittwo[2*s+1]])
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
        return(uniquelist, numberof, splitone, splittwo, sortednonsepcapitals)
    uniquelist, numberof, splitone, splittwo, genotypes = cross(firstcross,secondcross)
    separator = "-------+------+------+------"#incredibly ugly way to do this btw 
    print("Punnet Square")
    print("      " + ''.join(sameline(splitone, "     ")))
    print("   " + separator)
    for x in range(0,len(splitone)): 
        print(splittwo[x] + " " + '|' + " " + genotypes[x] + " " + '|' + " " + genotypes[x+4]+ " " + '|' + " " + genotypes[x+8]+ " " + '|' + " " + genotypes[x+12])
        print("   " + separator)
    for i in range(0, len(uniquelist)):
            print(str(numberof[i]) + "/16" + " " + str(uniquelist[i])) #printing the probs all out

