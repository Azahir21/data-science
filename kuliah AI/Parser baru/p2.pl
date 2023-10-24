noun([N], katabenda(N)) :-
	member(N,[ayam, kucing, budi]).

verb([V], katakerja(V)) :-
	member(V,[makan, minum, baca]).

sentence(S, kalimat(NPTree,VPTree) ) :-
	noun(N, NPTree),
	verb(V, VPTree),
        append(N,V,S).
	


