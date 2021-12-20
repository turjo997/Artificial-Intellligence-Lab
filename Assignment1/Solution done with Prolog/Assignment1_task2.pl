%Defining parent relation
parent('Bob' , 'Jesica'). parent('Bob' , 'Jane'). parent('Bob' , 'Richard').
parent('Bob' , 'Kalis').
parent('Lia' , 'Jesica'). parent('Lia' , 'Jane'). parent('Lia' , 'Richard').
parent('Lia' , 'Kalis').
parent('Jesica' , 'Jim'). parent('Jesica' , 'Ann').
parent('Richard' , 'Tom'). parent('Richard' , 'Gary').
%Defining gender relation
male('Adam'). male('Bob'). male('Richard'). male('Kalis'). male('Jim'). male('Tom').
female('Lia'). female('Jesica'). female('Jane'). female('Ann'). female('Gary').
%Brother relation
brother(B1,B2) :- parent(Father , B1) , parent(Father , B2) ,
    male(B1), not(B1 = B2).

%Sister relation
sister(S1,S2):-parent(Father , S1) , parent(Father , S2) , female(S1), not(S1 = S2).
% Uncle relation
uncle(X , Z):- brother(X , Y) , parent(Y , Z) ,not(parent(X,Z)).
% Aunt relation
aunt(A1 , A2):- sister(A1 , Y) , parent(Y , A2) , not(parent(A1,A2)).
findBrother:- write('Enter the name: ') , read(Y),
    write('Brother name: ') , brother(X , Y), write(X),tab(5),fail.
findBrother.
findSister:- write('Enter the name: ') , read(Y),
    write('Sister name: ') , sister(X , Y), write(X),tab(5),fail.
findSister.


findUncle:- write('Enter the name: ') , read(Y),
    write('Uncle name: ') , uncle(X , Y), write(X),tab(5),fail.
findUncle.


findAunt:- write('Enter the name: ') , read(Y),
    write('Aunt name: ') , aunt(X , Y), write(X),tab(5),fail.
findAunt.





%parent('Adam' , 'Lia'). parent('Adam' , 'Bob')















