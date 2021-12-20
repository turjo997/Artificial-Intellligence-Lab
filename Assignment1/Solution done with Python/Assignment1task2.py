tuple = [
    ('parent','Bob','Jesica'),('parent','Bob','Jane'),('parent','Bob','Richard'),('parent','Bob','Kalis'),
    ('parent' ,'Lia','Jesica'),('parent' ,'Lia','Jane'),('parent','Lia','Richard'),
    ('parent','Lia','Kalis'),('parent','Jesica','Jim'),('parent','Jesica','Ann'),('parent','Richard','Tom'),
    ('parent','Richard','Gary')
]

male = ['Adam','Bob','Richard','Kalis','Jim','Tom']

female = ['Lia','Jesica','Jane','Ann','Gary']

def brother(X):
    print('Brothers: ', end='')

    ans = []
    i = 0
    while(i<len(tuple)):
        if((tuple[i][0] == 'parent') & (tuple[i][2] == X)):
            for j in range (len(tuple)):
                if((tuple[j][0] == 'parent') & (tuple[i][2] != tuple[j][2]) &(tuple[i][1] == tuple[j][1])):
                    for k in range (len(male)):
                        if((tuple[j][2] == male[k]) & (tuple[i][2] != male[k])):
                            #print(tuple[j][2],end =' ')
                            ans.append(tuple[j][2])
        i = i + 1
    list_set = set(ans)
    print(list_set, end='')

def sister (X):
    print('Sisters: ', end='')
    i = 0
    ans = []
    while(i<len(tuple)):
        if((tuple[i][0] == 'parent') & (tuple[i][2] == X)):
            for j in range (len(tuple)):
                if((tuple[j][0] == 'parent') & (tuple[i][2] != tuple[j][2]) &(tuple[i][1] == tuple[j][1])):
                    for k in range (len(female)):
                        if((tuple[j][2] == female[k]) & (tuple[i][2] != female[k])):
                            #print(tuple[j][2],end =' ')
                            ans.append(tuple[j][2])
        i = i + 1
    list_set = set(ans)
    print(list_set, end='')
ans = []
def brother1(X):
    i = 0
    while (i < len(tuple)):
        if ((tuple[i][0] == 'parent') & (tuple[i][2] == X)):
            for j in range(len(tuple)):
                if ((tuple[j][0] == 'parent') & (tuple[i][2] != tuple[j][2]) & (tuple[i][1] == tuple[j][1])):
                    for k in range(len(male)):
                        if ((tuple[j][2] == male[k]) & (tuple[i][2] != male[k])):
                            ans.append(tuple[j][2])
                            #return tuple[j][2]
        i = i + 1


ans1 = []
def sister1(X):
    i = 0
    while (i < len(tuple)):
        if ((tuple[i][0] == 'parent') & (tuple[i][2] == X)):
            for j in range(len(tuple)):
                if ((tuple[j][0] == 'parent') & (tuple[i][2] != tuple[j][2]) & (tuple[i][1] == tuple[j][1])):
                    for k in range(len(female)):
                        if ((tuple[j][2] == female[k]) & (tuple[i][2] != female[k])):
                            ans1.append(tuple[j][2])
                            #return tuple[j][2]
        i = i + 1
def uncle(Z):
    print('Uncle: ', end='')

    i = 0

    while(i<len(tuple)):
        if((tuple[i][2] == Z) & (tuple[i][0] == 'parent')):
            if(brother1(tuple[i][1]) != []):
                #name = brother1(tuple[i][1])
                list_set = set(ans)
                print(list_set, end='')
        i = i + 1


def aunt(Z):
    print('Aunt: ', end='')

    i = 0

    while(i<len(tuple)):
        if((tuple[i][2] == Z) & (tuple[i][0] == 'parent')):
            if(sister1(tuple[i][1]) != []):
                #name = sister1(tuple[i][1])
                list_set = set(ans1)
                print(list_set , end='')
        i = i + 1
X = str(input("BrotherOf: "))
Y = str(input("SisterOf: "))
Z = str(input("UncleOf: "))
W = str(input("AuntOf: "))

brother(X)
print(end = ' ')
sister(Y)
print(end = ' ')
uncle(Z)
print(end = ' ')
aunt(W)