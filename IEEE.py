import fileinput
##for x in range(0,n):
##    for y in range(0,n):
##        lookup[n - x][n - y]



#True is left, false is down
def lookup_alg(x,y,turns_left,previous_x,previous_y):
    direction = ""
    if(previous_x == x):
        direction = "down"
    elif(previous_y == y):
        direction = "right"
    if (x==1 and y ==1):
##        print "In start node"
        partOne = lookup_alg(x + 1, y,turns_left,1,1)
        partTwo = lookup_alg(x,y + 1,turns_left,1,1)
        return partOne + partTwo
##    print "X: " + str(x) + " Y: " + str(y) + " turns: " + str(turns_left)
##    print y
##    print turns_left
    if (lookup[x][y][turns_left][direction] == None):
##        print "Checking for node"
        partOne = 0
        partTwo = 0
        if (x + 1 <= n):
            if (previous_x == x):
                if (turns_left >= 1):       
                    partOne = lookup_alg(x+1,y,turns_left - 1,x,y)
                else:
                    partOne = 0
            else:
                partOne = lookup_alg(x+1,y,turns_left,x,y)
        if (y + 1 <= n):
            if (previous_y == y):
                if(turns_left >= 1):
                    partTwo = lookup_alg(x,y+1,turns_left - 1,x,y)
                else:
                    partTwo = 0
            else:
                partTwo = lookup_alg(x,y+1,turns_left,x,y)
##        print "x: " + str(x) + " y: " + str(y)
##        print "part 1:" + str(partOne)
##        print "part 2: " + str(partTwo)
        lookup[x][y][turns_left][direction] = partOne + partTwo
        return partOne + partTwo
    else:
##        print "x: " + str(x) + " y: " + str(y) + " turns_left: " + str(turns_left) + " value: " + str(lookup[x][y][turns_left][direction])
        return lookup[x][y][turns_left][direction]
        


##            
##            if y == n:
####                 print str(x) + " " + str(y) + " " + str(z)
##                 if (z==0):
##                     lookup[x][y][0] = None
##                 else:
##                     lookup[x][y][z] = None
##            elif x == n:
####                print str(x) + " " + str(y) + " " + str(z)
##                if (z==0):
##                    lookup[x][y][0] = None
##                else:
##                    lookup[x][y][z] = None
##            else:
##                 lookup[x][y][z] = None

##set zero to anything that doesn't have any turns left and isn't on the edges
##for x in range (1,n):
##    for y in range(1,n):
##        lookup[x][y][0] = 0


        
for line in fileinput.input():
    n,k  = map(int, line.strip().split(' '))
    
    lookup = dict()
    #Initalize
    for x in range (1,n+ 1):
        lookup[x] = dict()
        for y in range(1,n+ 1):
            lookup[x][y] = dict()
            for z in range(0,k+1):
                lookup[x][y][z] = dict()
                lookup[x][y][z]["down"] = None
                lookup[x][y][z]["right"] = None
    try:
        lookup[n][n][0]["down"] = 1
        lookup[n][n][0]["right"] = 1
    except KeyError:
        pass
    try:
        print lookup_alg(1,1,k,0,0)
    except KeyError:
        pass
