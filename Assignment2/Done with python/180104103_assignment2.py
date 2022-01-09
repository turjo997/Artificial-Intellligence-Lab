########################   QUESTION 1 ###############

def sum(n,i,f):
    if(n == 0):
        return 0
    elif(n>=1):
        return sum(n-1 , i , f) + f + (n-1) * i

f= int(input("First number: "))
i = int(input("Interval: "))
n = int(input("How many numbers: "))

print("Series sum is " , sum( n , i , f))

########################   QUESTION 2 ############### 

def pathDist(start, end, cost=0):
    if (start, end) in pairList:
        print(str(cost + edgeDist[(start, end)]) + ' ')
    for (i, j) in pairList:
        if i == start:
            pathDist(j, end, cost + edgeDist[(i, j)])
# %% Input Handling and Calling recursive Function
edgeDist = {('i', 'a'): 35, ('i', 'b'): 45, ('a', 'c'): 20, ('a', 'd'): 30,
             ('b', 'd'): 25, ('b', 'e'): 35, ('b', 'f'): 27, ('c', 'd'): 30,('c', 'g'): 47,
             ('d', 'g'): 30, ('e', 'g'): 25}
pairList = [('i', 'a'), ('i', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd'),
            ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'g'), ('d', 'g'),
            ('e', 'g')]
start = str(input('Enter Starting point: '))
end = str(input('Enter Ending point: '))
print('The length of path is: ')
pathDist(start, end)



########################   QUESTION 3 ###############
#Goal state value
gtp=[(1,1,1), (2,1,2), (3,1,3), (4,2,3), (5,3,3), (6,3,2), (7,3,1), (8,2,1)]
gblnk = (2,2)

#Current state value
tp=[(1,1,2), (2,1,3), (3,2,1), (4,2,3), (5,3,3), (6,2,2), (7,3,2), (8,1,1)]
blnk = (3,1)

i,h=0,0

while(i<= 7):
    if((gtp[i][1] != tp[i][1])|(gtp[i][2] != tp[i][2])):
        h = h + abs(gtp[i][1] - tp[i][1]) + abs(abs(gtp[i][2] - tp[i][2]))
    i = i + 1
print('Heuristics Manhattan Distance : ',h)




########################   QUESTION 4 ###############
queen = [(1 , 1 , 2) ,(2 , 1 , 8) ,(3 , 3 , 6) , (4 , 4 , 5) ,
         (5 , 5 , 3) ,(6 , 6 , 1) , (7 , 7 ,4) , (8 , 8 , 7)]
ans , cnt = 0 , 0

for i in range (len(queen)):
    for j in range (len(queen)):
        ## if they are face to face
        if((i != j) & (queen[i][1] == queen[j][1])):
            cnt += 1
            ans = ans + 1
        ##face to face diagonally down
        elif ((i != j) & ( abs(queen[i][1] - queen[j][1]) ==  abs(queen[i][2] - queen[j][2]) )
                 & ( queen[i][1] > queen[j][1] )  & ( queen[i][2]<queen[j][2]) ):
            ans = ans + 1
        ##face to face diagonally up
        elif ((i != j) & ( abs(queen[i][1] - queen[j][1])  ==  abs(queen[i][2] - queen[j][2]) )
                  & ( queen[i][2] < queen[j][2] ) & ( queen[i][1] < queen[j][1]) ):
            ans = ans + 1

print("Heuristic (attacking power) : " , int(ans - cnt/2))