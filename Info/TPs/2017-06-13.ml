(* Implementation de files par des tableaux (FIFO)*)

let creer_file () =
	let t = make_vect (100 +1) 0
	and deb = ref 0
	and fin = ref 0
	in (t, deb, fin)
;;

let enfiler x f =
	let (t, deb, fin) = f in
	if (!deb + 1) mod vect_length(t) = !fin
	then failwith "File pleine";
	t.(!deb) <- x;
	deb := (!deb +1) mod vect_length(t)
;;

let defiler f =
	let (t, deb, fin) = f in
	if !fin = !deb
	then failwith "File vide";
	let y = t.(!fin)
	in fin := (!fin + 1) mod vect_length(t);
	y
;;

let f = creer_file();;

enfiler 1 f;;
enfiler 2 f;;
enfiler 3 f;;
enfiler 4 f;;
enfiler 5 f;;
enfiler 7 f;;
defiler f;;

let a = ref 1;;
let b = ref !a;;
b := 2;;
!a;;

(* Implementation par un couple de files *)

let creer_pile () = ref [] ;;

let empiler x p = p := x :: !p ;;

let depiler p =
	match !p with
	| [] -> failwith "Vide"
	| x :: q ->
		p := q;
		x
;;

let pile_vide p = (!p = []);;

let creer_file_2 () =
	let entrn = creer_pile()
	and sortn = creer_pile()
	in (entrn, sortn)
;;

let enfiler_2 x f =
	let (entrn, sortn) = f in
	empiler x entrn
;;

let transvaser s e =
	while not pile_vide(e) do
	empiler (depiler e) s
	done
;;

let defiler_2 f =
	let (e, s) = f in
	if pile_vide(s)
	then transvaser s e;
	depiler s
;;
	
let file_vide_2 f =
	let (e, s) = f in
	(pile_vide e) && (pile_vide s)
;;

(* Files de priorité *)

let creer_fdp () = ref [];;

let ajouter x p fdp = fdp := (x, p) :: !fdp;;

let rec retirer_max = function
| [] -> failwith "Vide"
| [(x, p)] -> (x, p, [])
| (x, p) :: q ->
	let (x', p', r') = retirer_max q in
	if p >= p'
	then (x, p, q)
	else (x', p', (x, p) :: r')
;;

let retirer fdp =
	let (x, p, r) = retirer_max !fdp in
	fdp := r;
	x
;;

(* Application 1 : les piles *)

let nb = ref 0;;
let fdp = creer_fdp ();;

let push x =
	ajouter x !nb fdp;
	incr nb
	(* incr pour pile, decr pour file *)
;;

let pop () = retirer fdp;;

(* Exercices *)

let rec pile_max p =
	if pile_vide p
	then failwith "Vide"
	else (
		let x = depiler p in
		if pile_vide p
		then (
			empiler x p;
			x
		)
		else (
			let m = pile_max p in
			empiler x p;
			if m > x
			then m
			else x
		)
	)
;;

let rec copier_pile p =
	if pile_vide p
	then creer_pile()
	else (
		let x = depiler p in
		let p' = copier_pile p in
		empiler x p';
		empiler x p;
		p'
	)
;;
