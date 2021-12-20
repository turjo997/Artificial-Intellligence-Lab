tuple =[
    ('parent' , 'Fahim' , 'Debo'),('parent' , 'Eliya' , 'Fahim'),
    ('parent' , 'Bob' , 'Hasan'),('parent' , 'Hasan' , 'Aziz'),
    ('parent' , 'Rubel' , 'Fahim'),('parent' , 'Rebeka' , 'Jashim'),
    ('parent' , 'Jashim' , 'Anis'),('parent' , 'Hasan' , 'Nila'),
    ('parent' , 'Fahim' , 'Nikil'),('parent' , 'Nikil' , 'sajib'),
    ('parent' , 'Hasan' , 'Tumpa'),('parent' , 'Fahim' , 'Chandra'),
    ('parent' , 'Jesica' , 'Hasan')
]

i = 0
Y = str(input("Grandchildren: "))
print('Grandparents: ' , end = '')
while(i<len(tuple)):
    if(tuple[i][2] == Y):
        for k in range(len(tuple)):
            if((tuple[i][1] == tuple[k][2])):
                print(tuple[k][1] , end = ' ')
    i = i + 1














'''
tuple = [('parent' , 'Hasib' , 'Rakib') ,
         ('parent' , 'Rakib' , 'Sohel') ,
         ('parent' , 'Rakib' , 'Rebeka') ,
         ('parent' , 'Rashid' , 'Hasib')
         ]
tuple =[
    ('parent' , 'Bob' , 'Hasan'),
    ('parent' , 'Hasan' , 'Aziz'),
    ('parent' , 'Rubel' , 'Fahim'),
    ('parent' , 'Rebeka' , 'Jashim'),
    ('parent' , 'Jashim' , 'Anis'),
    ('parent' , 'Hasan' , 'Nila'),
    ('parent' , 'Fahim' , 'Nikil'),
    ('parent' , 'Nikil' , 'sajib'),
    ('parent' , 'Hasan' , 'Tumpa')
]

'''
'''
print(tuple)

X = str(input("Grandparent: "))
print('Grandchildren: ' , end = '')

i =0

while(i<len(tuple)):
    if((tuple[i][0] == 'parent') & (tuple[i][1] == X)):
        for j in range (len(tuple)):
            if((tuple[j][0] == 'parent') & (tuple[i][2] == tuple[j][1])):
                print(tuple[j][2]  , end = ' ')
    i = i + 1




tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Sohel'),
('parent', 'Rakib', 'Rebeka'),('parent', 'Rashid', 'Hasib')]
# Procedure to find the grandchildren of X
#X=str(input("Grandparent:"))
#print('Grandchildren:', end=' ')
i=0
while(i<=3):
    if ((tuple[i][0] == 'parent')&( tuple[i][1] == X)):
        for j in range(4):
            if ((tuple[j][0] == 'parent') & ( tuple[i][2] == tuple[j][1])):
                print(tupleList1[j][2], end=' ')
    i=i+1

'''



