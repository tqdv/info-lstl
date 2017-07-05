1 + 1 ;;
print_endline "Test" ;;

let a = 1 + 1 ;;
let b = 1. +. 1. ;;
let c = 1. +. float_of_int 1 ;;


let d = not true && false || true ;;

let e = (1 = 2) || (3 < 4) ;;
let f = "Heck" ;;

let f(x) = x + 1 ;;
let f2 = function x -> x + 1 ;;
f2(3) ;;

print_int 42 ;;
print_float 42.3 ;;
print_string "a" ;;

let print_bool (b) =
  match b with
  | true -> print_string("Vrai")
  | false -> print_string("Faux")
;;

print_bool (3 = 4) ;;

let f x =
  match x with
  | 0 -> 1
  | _ -> 0
;;

(* Compte le nombre de 0 dans le couple *)
let g (x, y) = 
  match (x, y) with
  | (0, 0) -> 2
  | (0, _) -> 1
  | (_, 0) -> 1
  | _ -> 0
;;

(* Compte le nombre de `true' dans le couple *)
let g2 (x, y) = 
  match (x, y) with
  | (true, true) -> 2
  | (true, false) -> 1
  | (false, true) -> 1
  | (false, false) -> 0
;;

let g3 = function
| (true, true) -> 2
| (true, false) -> 1
| (false, true) -> 1
| (false, false) -> 0
;;

let h1 (x, y) = x + y ;;

let h2 (x) (y) = x + y ;;

let succesor y = h2 y 1 ;;
let succeseur = h2 (1) ;;


let rec fact2(n) =
  match n with
  | 0 -> 1
  | n -> n * fact(n - 1)
;;

let rec fact = function
| 0 -> 1
| n -> n * fact(n - 1)
;;

let rec pgcd(x,y) =
  if y = 0
    then x
    else pgcd(y, x mod y)
;;

let rec prod (a) (b) =
  if a > b
    then 1
    else a * prod (a + 1) b
;;

(* OMG tail recursion *)
let rec aux p n =
  if n = 0
    then p
    else aux (n * p) (n - 1)
;;
let fact(n) =
  aux 1 n
;;

let rec aux1 p a b =
  if a > b
    then p
    else aux1 (a*p) (a+1) b
;;
let prod1 a b =
  let rec aux1 p a b =
    if a > b
      then p
      else aux1 (a*p) (a+1) b
  
  in aux1 1 a b
;;

let sumDiv x =
  let rec aux sum a b =
    if a > b
	  then sum
    else if b mod a = 0
	  then aux (sum+a) (a+1) b
	  else aux sum (a+1) b
  in aux 0 1 x
;;
