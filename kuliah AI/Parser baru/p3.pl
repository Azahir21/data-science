determiner([D], katasandang(D)) :-
	member(D,[seorang, sebutir, seekor, dua, tiga]).

noun([N], katabenda(N)) :-
	member(N,[manusia, telur, ayam]).

verb([V], katakerja(V)) :-
	member(V,[makan, terbang, jatuh]).

adj([A], keterangan(A)) :-
	member(A,[tinggi, sedikit]).

noun_phrase(NP,frasa_benda(NTree)) :-
	noun(NP,NTree).

noun_phrase(NP,frasa_benda(DTree,NTree)) :-
	determiner(D,DTree), 
	noun(N,NTree),append(D,N,NP).

verb_phrase(VP, frasa_kerja(VTree, ATree)) :-
	verb(V, VTree),
	adj(A, ATree),append(V,A,VP).

verb_phrase(VP, frasa_kerja(VTree)) :-
	verb(VP, VTree).

sentence(S, kalimat(NPTree,VPTree) ) :-
	noun_phrase(NP,NPTree),
	verb_phrase(VP,VPTree), append(NP,VP,S).
	

