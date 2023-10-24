determiner([D], determinan(D)):-
    member(D, [seorang]).

noun([N], katabenda(N)):-
    member(N, [dokter, perawat, budi, pasien, obat]).

verb([V], katakerja(V)):-
    member(V, [memeriksa, mengambil, minum]).

adverb([A], kataketerangan(A)):-
    member(A, [dikamar, diapotek]).

noun_phrase(NP, subyek(DTree,NTree)) :-
	determiner(D,DTree), 
	noun(N,NTree),append(D,N,NP).

noun_phrase(NP, subyek(NTree)) :-
    noun(NP, NTree).

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