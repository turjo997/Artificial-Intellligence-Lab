parent('Fahim' , 'Debo').  parent('Eliya' , 'Fahim').
parent('Bob' , 'Hasan').   parent('Hasan' , 'Aziz').
parent('Rubel' , 'Fahim'). parent('Rebeka' , 'Jashim').
parent('Jashim' , 'Anis'). parent('Hasan' , 'Nila').
parent('Fahim' , 'Nikil'). parent('Nikil' , 'sajib').
parent('Hasan' , 'Tumpa'). parent('Fahim' , 'Chandra').
parent('Jesica' , 'Hasan').

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).


findGp:- write('Grandchildren: ') , read(X) , write('Grandparent: ') ,
    grandparent(Gp , X) , write(Gp) , tab(5) , fail.
findGp.









