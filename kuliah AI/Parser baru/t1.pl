determiner([D], determinan(D)):-
    member(D, [seorang, seekor]).

noun([N], katabenda(N)):-
    member(N, [manusia, anjing, nasi, daging, air]).

verb([V], katakerja(V)):-
    member(V, [makan, minum]).

adverb([A], kataketerangan(A)):-
    member(A, [kemaren, tadi]).

noun_phrase(NP,subyek(DTree,NTree)) :-
	determiner(D,DTree), 
	noun(N,NTree),append(D,N,NP).

verb_phrase(VP, predikat(VTree)) :-
	verb(VP, VTree).

verb_phrase(VP, frasa_kerja(VTree, NTree)) :-
	verb(V, VTree),
	noun(N,NTree),append(V,N,VP).

sentence(S, kalimat(NPTree,VPTree) ) :-
	noun_phrase(NP,NPTree),
	verb_phrase(VP,VPTree), append(NP,VP,S).
    
sentence(S, kalimat_lengkap(NPTree, VPTree, ATree)) :-
    noun_phrase(NP, NPTree),
    verb_phrase(VP, VPTree), append(NP, VP, SA),
    adverb(A, ATree), append(SA, A, S).