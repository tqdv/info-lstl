let rec max u a b =
 if a = b
 then u(a)
 else
  let m = max (u : int -> int) (a+1) b
  in
   if u(a) > m
    then u(a)
	else m
;;

let u(x) = x * x mod 171 ;;

max u 1 100 ;;

(* And with tail recursion *)
let rec aux m u a b =
 if a > b
  then m
  else
   if m > u(a)
    then aux m u (a+1) b
    else aux (u(a)) u (a+1) b
;;
let max u a b = aux (u(a)) u (a+1) b ;;

let ms x =
 (x * x mod 1000000000000) / 10000
;;

type nombre =
| Entier of int 
| Flottant of float
;;

let prefix +: x y =
 match (x,y) with
 | (Entier u, Entier v) -> Entier(u+v)
 | (Entier u, Flottant v) -> Flottant(float_of_int u +. v)
 | (Flottant u, Entier v) -> Flottant(u +. float_of_int v)
 | (Flottant u, Flottant v) -> Flottant(u +. v)
;;

Entier 5 +: Flottant 1.2 ;;

let l1 = 1::2::3::4::5::[] ;;
hd(l1);;
tl(l1) ;;

let rec fill x = function
| 0 -> []
| n -> x::(fill x (n-1))
;;

fill 0 5;;

let rec alterner a b = function
| 0 -> []
| n -> a :: alterner b a (n-1) ;;

alterner 1 0 5;;
alterner 1 0 4;;

let rec decr = function
| 0 -> []
| n -> n::decr (n-1)
;;

decr 5;;

let rec cr i n =
 if i > n
  then []
  else i :: cr (i+1) n 
;;

let crr = cr 1 ;;

crr 5;;

(* Squares *)
(* 1 on squares, 0 elsewhere *)

let rec longueur = function
| [] -> 0
| t::q -> 1 + longueur q
;;

(*Sum ? Max ? Tail recusion for length ? 
 * sumthin
 *)

let rec sum temp = function
| [] -> temp
| t::q -> sum (temp+t) q
;;
let summ = sum 0 ;;
summ (crr 2) ;;

let rec somme = function
| [] -> 0
| t::q -> t + somme(q)
;;

let rec maximum = function
| [] -> failwith "Liste vide sans maximum"
| [x] -> x
| t::q ->
   let m = maximum(q) in
    if t > m
	 then t
	 else m
;;

maximum (crr 5) ;;
