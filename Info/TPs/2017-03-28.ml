(* Ordre lexicographique sur des couples d'entiers *)
let ord1 (x1, y1) (x2, y2) =
  (x1 < x2) || ((x1 = x2) && (y1 <= y2))
;;

let rec ord2 l1 l2 =
 match (l1, l2) with
 | ([], _) -> true
 | (_, []) -> false
 | (x1::q1, x2::q2) -> (x1 < x2) || ((x1 = x2) && (ord2 q1 q2))
;;

(* 
   Those two function above are useless because OCaml already 
   knows how to compare those
*)

(* The Ackermann function *)
let rec ack = function
| (0, n) -> n+1
| (m, 0) -> ack(m-1, 1)
| (m, n) -> ack(m-1, ack(m, n-1))
;;

let test() =
 for i = 1 to 10
 do
   print_int(i);
   print_newline(); (* <- this very specific semi-colon is useless *)
 done
;;

let a = ref 12;;

a := 16;;
a;;
!a;;

(* Euclide *)
let pgcd(x, y) =
 let a = ref x in
 let b = ref y in
 while !b > 0
   do
	 let r = !a mod !b in
	 a := !b;
	 b := r;
   done;
 !a
;;


(* Min of table *)

let min a =
  if a = [||]
  then failwith "Empty" ;
  let min = ref a.(0) in
  for i = 1 to vect_length(a) -1
  do
    if a.(i) < !min
	then min := a.(i)
  done;
  !min
;;

let rec list2vect = function
| [] -> [||]
| [n] -> [|n|]
| t::q -> concat_vect ([|t|]) (list2vect(q))
;;
(* ^ Not efficient *)

let rec remplir_dep deb t l =
  match l with
  | [] -> ()
  | x::q -> 
      t.(deb) <- x;
      remplir_dep (deb+1) t q
;;

let vect_of_list l =
  match l with
  | [] -> [||]
  | x::q ->
    let t = make_vect (list_length l) x in
	remplir_dep 1 t q;
	t
;;

let list_of_vect t =
  let rec construire_depuis i =
    if i >= vect_length t
	then []
	else t.(i)::construire_depuis(i+1)
  in construire_depuis 0
;;

let revert arr =
  let buff = ref 0 in
  let len = vect_length arr in
  for i = 0 to len/2
  do
      buff := arr.(len-1 -i) ;
	  print_int !buff;
	  arr.(len-1 -i) <- arr.(i) ;
	  arr.(i) <- !buff ;
  done ;
  arr
;;

let ech t i j =
  let tmp = t.(i) in
  t.(i) <- t.(j);
  t.(j) <- tmp
;;

let renv_t t =
  for i = 0 vect_length(t) /2
  do ech t i (vect_length(t) -1 -i)
  done
;;

(* Bad revert list in O(n2) *)
let rec add2end x = function
| [] -> [x]
| t::q -> t::(add2end x q) ;;
let rec badrev = function
| [] -> []
| t::q -> add2end t (badrev q) ;;

(* Good list revert in O(n) *)
let rec revertin this = function
| [] -> this
| t::q -> revertin (t::this) q;;
let goodrev(t) = 
  revertin [] l;;

(* Good list rot *)
let toutMettreAuBout relicat = function
| [] -> relicat
| t::q -> t::(toutMettreAuBout relicat q) ;;
let prendrePremiers r l =
  if r = 0
  then ([], l)
  else 
    match l with
	| [] -> failwith "NEI"
	| t::q ->
	  let (a, b) = prendrePremiers (r-1) q in
	  (t::a, b)
;;

let goodrot r l =
  let (a, b) prendrePremiers (r mod (list_length l)) in
  toutMettreAuBout a b;;