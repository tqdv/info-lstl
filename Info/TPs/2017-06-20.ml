(* # Arbres binaires *)

(* Vocabulaire des arbres *)

type ('a, 'b) arbre =
	| Vide
	| Noeud of 'b * ('a, 'b) arbre * ('a, 'b) arbre
	| Feuille of 'a
;;

let a1 = Noeud(5, Feuille(), Feuille());;

(* 
if ($ahashref->{"$aval"} != 0) {
	push @cmps, ($ahashref->{"$aval"} > 0 ? 1 : -1);
} else { warn "Added a zero to value"; }
*)

let rec hauteur = function
	| Vide -> -1
	| Feuille(_) -> -1
	| Noeud(n, g, d) -> 1 + (max (hauteur g) (hauteur d))
;;

(*
unshift @bkeys, $bval;
if ($ahashref->{"$aval"} > 0) {
	push @cmps, -1;
} elsif ($ahashref->{"$aval"}) {
	push @cmps, 1;
} elsif ($ahashref->{"$aval"} == 0) {
	warn "Added a zero to value";
}
*)

type op = Plus | Moins | Fois ;;
let print_op = function
	| Plus -> print_string " + "
	| Moins -> print_string " - "
	| Fois -> print_string " x "
;;

let e1 = 
Noeud(
	Fois,
	Noeud(
		Plus,
		Feuille 7,
		Feuille 2
	),
	Noeud(
		Moins,
		Noeud(
			Fois,
			Feuille 4,
			Feuille 2
		),
		Feuille 1
	)
)
;;

let rec eval = function
	| Vide -> failwith "Rien à évaluer"
	| Feuille(x) -> x
	| Noeud(Plus, g, d) -> (eval g) + (eval d)
	| Noeud(Moins, g, d) -> (eval g) - (eval d)
	| Noeud(Fois, g, d) -> (eval g) * (eval d)
;;

let rec infixe = function
	| Vide -> failwith "Rien à évaluer"
	| Feuille(x) -> print_int x
	| Noeud(o, g, d) ->
		print_string "(";
		infixe g;
		print_op o;
		infixe d;
		print_string ")"
;;

type lex =
	| Nombre of int
	| Operateur of op
;;

let rec postfixe = function
	| Vide -> failwith "Rien à évaluer"
	| Feuille(x) -> [Nombre x]
	| Noeud(o, g, d) -> (postfixe g) @ (postfixe d) @ [Operateur o]
;;

(* Evaluer une expression postfixe *)

let creer_pile () = ref [] ;;
let empiler p x =
	p := x :: !p
;;
let depiler p =
	match !p with
	| [] -> failwith "Pile vide"
	| x :: q ->
		p := q;
		x
;;

(* pf = postfixe *)
let eval_pf e =
	let p = creer_pile() in
	let rec aux = function
		| [] -> depiler p
		| (Nombre x) :: q ->
			empiler p x;
			aux q
		| (Operateur Plus) :: q ->
			let y = depiler p
			and x = depiler p in
			empiler p (x + y);
			aux q
		| (Operateur Moins) :: q ->
			let y = depiler p
			and x = depiler p in
			empiler p (x - y);
			aux q
		| (Operateur Fois) :: q ->
			let y = depiler p
			and x = depiler p in
			empiler p (x * y);
			aux q
	in aux e
;;

