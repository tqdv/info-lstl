type 'a arbre =
	| Vide
	| Noeud of 'a  * ('a arbre) * ('a arbre)
;;

let a1 = Noeud( 3,
  Noeud(2, Noeud(1, Noeud(5, Vide, Noeud(2, Vide, Vide)), Noeud(5, Vide, Vide)), Vide), Vide);;
(*

    3
    |
    2
    |
    1
   / \
  5   5
  |
  2

*)

let rec ajouter a x =
    match a with
	| Vide -> Noeud((x, 1), Vide, Vide)
	| Noeud((mot, eff), g, d) ->
		if mot = x
		then Noeud((mot, eff +1), g, d)
		else
			if mot < x
			then Noeud((mot, eff), ajouter g x, d)
			else Noeud((mot, eff), g, ajouter d x)
;;

let a = ajouter Vide "Hello";;
let a = ajouter a "oh";;
let a = ajouter a "...";;

let rec effectif a x =
	match a with
	| Vide -> 0
	| Noeud((mot, eff), g, d) ->
		if x = mot
		then eff
		else
			if x < mot
			then effectif g x
			else effectif d x
;;

let rec list_of_arbre = function
	| Vide -> []
	| Noeud(n, g, d) -> (list_of_arbre g) @ (n :: (list_of_arbre d))
;;

let eff_max l =
	let rec aux = function
		| [] -> failwith "Vide"
		| [(mot, eff)] -> (mot, eff)
		| (mot, eff) :: q ->
			let (m, e) = aux q in
			if eff > e
			then (mot, eff)
			else (m, e)
	in fst(aux l)
;;

let rec arbre_of_list = function
	| [] -> Vide
	| x :: q ->
		let a = arbre_of_list q in
		ajouter a x
;;

let meilleur_mot texte =
	eff_max (list_of_arbre (arbre_of_list texte))
;;

meilleur_mot ["bonjour"; "le"; "monde"; "et"; "bonjour"; "la"; "lune"];;


#open "stack";;

let p = new();;
push 1 p;;
push 17 p;;
push 43 p;;
push 16 p;;
push 12 p;;
push 19 p;;
push 42 p;;
push 1 p;;
push 11 p;;

let est_vide p =
	try
		let x = pop p
		in push x p;
		false
	with Empty -> true
;;

let rec hauteur p =
	if est_vide p
	then 0
	else (
		let x = pop p in
		let h = hauteur p in
		push x p;
		h + 1
	)
;;

let sommet(p) =
	let x = pop p in
	push x p;
	x
;;

let sssommet p =
	let x1 = pop p in
	try
		let x2 = pop p in
		push x2 p;
		push x1 p;
		x2
	with Empty ->
		push x1 p;
		raise Empty
;;

let k2 = sssommet;;

let rec bottom p =
	let x = pop p in
	if est_vide p
	then (
		push x p;
		x
	) else (
		let b = bottom p in
		push x p;
		b
	)
;;

#close "stack";;

let creer() = [];;

let empiler x p = x :: p;;
let depiler p =
	match p with
	| [] -> failwith "Vide"
	| x :: q -> (x, q)
;;
let est_vide p = p = [];;
