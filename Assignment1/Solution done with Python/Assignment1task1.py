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
