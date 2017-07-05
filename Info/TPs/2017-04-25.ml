(* 1 - Exemples *)

(* Un type pour les nombres complexes *)
type cpx = {
  re : float ;
  im : float
} ;;
(* Ajouter `mutable' before to make them... mutable *)

let zero = {re = 0.0 ; im = 0.0} ;;
let un = { re = 1.0 ; im = 0.0} ;;
let i = { re = 0.0 ; im = 1.0} ;;

let ints b = (
  let a = b in
  let c = a in
  (print_int a;
  print_int c)
);;

let add x y = {
  re = x.re +. y.re ;
  im = x.im +. y.im
} ;;

let sstr x y = {
  re = x.re -. y.re ;
  im = x.im -. y.im
} ;;

let mul x y = {
  re = x.re *. y.re -. x.im *. y.im ;
  im = x.re *. y.im +. x.im *. y.re
} ;;

let mod2 x =
  x.re *. x.re +. x.im *. x.im
;;
let div x y =
  let m2 = mod2(y) in
  {
    re = (x.re *. y.re +. x.im *. y.im) /. m2 ;
	im = (x.im *. y.re -. x.re *. y.im) /. m2
  }
;;

let prefix +~ = add ;;
let prefix -~ = sstr ;;
let prefix *~ = mul ;;
let prefix /~ = div ;;

(* Listes doublement chaînées *)

type 'a cell = {
  mutable prec : 'a cell ;
  elt : 'a ;
  mutable suiv : 'a cell
} ;;

type 'a liste = Vide | Tete of 'a cell ;;

let singleton x =
  let rec c = {
    prec = c ;
	 elt = x ;
	 suiv = c
  } in Tete(c)
;;

let ajouter x l =
  match l with
  | Vide -> singleton x
  | Tete(t) -> 
    let c = {
	  prec = t.prec ;
	  elt = x ;
	  suiv = t
	} in
	t.prec <- c ;
	c.prec.suiv <- c ;
	Tete(c)
;;

(* Affichage d'une liste *)
let rec afficher_jusqu_a t c = 
  if not(c == t)
  then begin
  print_string "; " ;
  print_int c.elt ;
  afficher_jusqu_a t c.suiv
  end
;;

let afficher = function
  | Vide -> print_string "[]"
  | Tete(t) ->
    print_string "[" ;
	 print_int t.elt ;
	 afficher_jusqu_a t t.suiv ;
	 print_string "]" ;
	 print_newline()
;;

let l = Vide ;;
let l = ajouter 42 l;;
let l = ajouter 3 l;;
let l = ajouter 1 l;;
let l = ajouter 4 l;;
let l = ajouter 13 l;;

afficher l ;;

let m = Vide ;;
let m = ajouter 1 m ;;
let m = ajouter 2 m ;;
let m = ajouter 3 m ;;
let m = ajouter 4 m ;;
let m = ajouter 5 m ;;

let concat l1 l2 =
  match (l1, l2) with
  | (Vide, _) -> l2
  | (_, Vide) -> l1
  | (Tete t1, Tete t2) ->
    let t = t1.prec in
	t1.prec.suiv <- t2 ;
	t1.prec <- t2.prec ;
	t2.prec.suiv <- t1 ;
	t2.prec <- t ;
	Tete t1
;;

let a = concat m l ;;
afficher a;; 

(* Une structure pour les collections *)
let rec inserer x = function 
  | [] -> [x]
  | t::q ->
    if x <= t
	then x::t::q
	else t::(inserer x q)
;;

let rec est_dedans x = function
  | [] -> false
  | t::q ->
    if x < t
	then false
	else if x = t
	then true
	else est_dedans x q
;;

let rec supprimmer x= function
  | [] -> []
  | t::q ->
    if x < t
	then t::q
	else if x = t
	then q
	else t::(supprimmer x q)
;;

type 'a sac = {
  ajouter : 'a -> unit ;
  est_dedans : 'a -> bool ;
  supprimmer : 'a -> unit ;
} ;;

let creer sac () =
  let l = ref [] in {
    ajouter = (fun x -> l := inserer x !l) ;
	est_dedans = (fun x -> est_dedans x !l) ;
	supprimmer = (fun x -> l := supprimmer x !l) ;
  }
;;

let rec occurences x s =
  if s.est_dedans x
  then (
    s.supprimmer x ;
	let o = occurences x s in
	s.ajouter x ;
	o + 1
  )
  else 0
;;
