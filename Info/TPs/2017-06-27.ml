(* Construction d'arbres *)

type 'a Arbre =
	| Vide
	| Noeud of 'a * 'a Arbre * 'a Arbre
;;

let rec arbre_a_inverse = function
	| 0 -> Vide
	| n -> Noeud(n, (arbre_a_inverse(n-1)), Vide)
;;

let arbre_a n =
	let rec aux k =
		if k = n
		then Vide
		else Noeud(k, (arbre_a_inverse(k +1)), Vide)
	in aux 1
;;

let arbre_b n =
	let rec aux k =
	if k > n
	then Vide
	else Noeud(k, aux(2 * k), aux(2 * k + 1))
	in aux 1
;;

let rec image f = function
	| Vide -> Vide
	| Noeud(x, g, d) -> Noeud(f(x), image f g, image f d)
;;

let arbre_c n =
	image (fun x -> n + 1 - x) (arbre_b n)
;;

(* Arbres multi-aires *)

type 'a m_arbre =
	| Vide
	| Noeud of 'a * ('a m_arbre list)
;;

let rec map f = function
	| [] -> []
	| x::q -> f(x) :: (map f q)
;;

let rec list_it f e = function
	| [] -> e
	| x::q -> f(x, list_it f e q)
;;

(* list_it (fun(x, y) -> x+y) 0 [1;2;3;4;5;6];; *)

let rec somme = function
	| Vide -> 0
	| Noeud(x, s_arbres) -> list_it (fun (a,b) -> somme(a) + b) x s_arbres
;;

(* (r*x-(r-2)) *)
(* 0..(r-1) *)
let petite_liste r =
	let rec aux k =
		if k = r
		then []
		else k :: (aux (k + 1))
	in aux 0
;;

(* multi-abre à r-ramifications *)
let m_arbre_complet r n =
	let rec aux k =
		if k > n
		then Vide
		else Noeud(k, map (fun i -> aux(r*k -(r-2) + i)) (petite_liste r))
	in aux 1
;;

(*

A chaque ligne, ya r^i noeuds avec i = 0.. la profondeur de la ligne.
Le 1er elem de la ligne est 1 + (r^i -1)/(r - 1)

Supposons x = 1 + (r^i - 1)/(r - 1) + j
Donc y = 1 + (r^(i+1) - 1)/(r - 1) + j*r

Vérifions aue y = r*x - (r-2)

*)