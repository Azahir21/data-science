noun([N], subyek(N)):-
	member(N,[adik,kakak]).
verb([V],noun(V)):-
	member(V,[main,ajar, buat, datang, pergi]).
object([O],obyek(O)):-
	member(O,[bola, boneka, makanan]).
adv([A],noun(A)):-
	member(A,[sendiri, hari, malam]).
awalan([F],awalan(F)):-
	member(F,[ber,bel,me,mem,se]).
akhiran([P],akhiran(P)):-
	member(P,[an,i]).

%% frase

phrase4(AF, keterangan(FTree, ATree)):-
	awalan(F, FTree).
	adv(A, ATree),
	append(F,A,AF).
phrase3(OA, frase_obyek(OTree, AFTree)):-
	object(O,OTree),
	phrase4(AF,AFTree),
	append(O,AF,OA).
phrase2(VP,frase_kerja(VTree, PTree)):-
	verb(V,VTree),
	phrase3(OA, PTree),
	append(V,OA,VP).
phrase(P,predikat(FTree, VPTree)):-
	awalan(F, FTree), 
	phrase2(VP, VPTree),
	append(F,VP,P).

%% kalimat

sentence(S, kalimat(NTree, PPTree)):-
	noun(N,NTree),
	phrase(P, PPTree),
	append(N,P,S).
