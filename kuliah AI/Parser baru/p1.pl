%% define words:

determiner([D],determiner(D)) :-
	member(D,[the, a, an]).

noun([N], noun(N)) :-
	member(N,[dog, street, ball, bat, boy]).

adj([A], adj(A)) :-
	member(A,[fast, little, big]).

prep([P], prep(P)) :-
	member(P,[down, under]).

verb([V], verb(V)) :-
	member(V,[ran, caught, yelled, see, saw]).

%% parse noun phrases:

noun_phrase(NP,noun_phrase(NTree)):-
	noun(NP,NTree).	

noun_phrase(NP,noun_phrase(DTree,NTree)) :-
	determiner(D,DTree),
	noun(N,NTree),append(D,N,NP).

%% parse prepositional phase:

prep_phrase(PP, prep_phrase(PTree, NPTree)) :-
	prep(P, PTree),
	noun_phrase(NP, NPTree),append(P,NP,PP).

%% parse verb phrases:

verb_phrase(VP, verb_phrase(VTree, NPTree)) :-
	verb(V, VTree),
	noun_phrase(NP, NPTree),append(V,NP,VP).

verb_phrase(VP, verb_phrase(VTree, PPTree)) :-
	verb(V, VTree),
	prep_phrase(PP, PPTree),append(V,PP,VP).

verb_phrase(VP, verb_phrase(VTree)) :-
	verb(VP, VTree).

%% parse entences:

sentence(S, sentence(NPTree,VPTree) ) :-
	noun_phrase(NP,NPTree),
	verb_phrase(VP,VPTree),append(NP,VP,S).

%% throw away test code:


%% test :- sentence([the,dog, ran], Tree), print(Tree).
%% test1 :- sentence([the,dog, ran, down, the, street], Tree), print(Tree).


