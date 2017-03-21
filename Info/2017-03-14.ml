
(* This stuff fails *)
(*
let rec min = function
| [n]  -> n
| []   -> failwith "[]"
| t::q -> let m = min q in
		  if t >= q
          then m
		  else t
;;

let rec pop m = function
| t::q -> if t = m
		  then q
		  else t:: pop m q
| [] -> failwith "Not found"
;;

let pop_min l =
 pop (min l) l
;;
*)

let rec dpp = function
| [] -> failwith "nei"
| [x] -> failwith "nei"
| [a;b] -> if a <= b
           then a,b
		   else b,a
| t::q -> let (m,n) = dpp(q) in
          if t <= m
		   then t, m
		  else if t <= n
		   then m, t
		   else m, n
;;

let rec extr_min = function
| [] -> failwith "nei"
| [x] -> x, []
| t::q -> let (m, r) = extr_min q in
          if t <= m
		   then t, q
		   else m, t::r
;;

let deu l =
 let (m, l) = extr_min l in
 let mm, ll = extr_min l in
 mm
;;

let rec extr_all_min = function
| [] -> failwith "[min]"
| [x] -> x, []
| t::q -> let (m,reste) = extr_all_min q in
          if t < m
		   then t, q
		  else if t = m
		   then m, reste
		   else m, t::reste
;;

let deu_strict l =
 let m, l = extr_all_min l in
 if l = []
  then failwith "const list"
  else let (mm, ll) = extr_all_min l in
   mm
;;

(* .append *)

let rec append elem =
| [] -> [elem]
| t::q -> t :: tole elem q
;;

let rec

let rec test l cmp =
 
 
let rec memebre x = function
| [] -> false
| t::q -> t = x || membre x q
;;

let a() =
 print_string "a eval";
 true
;;

let rec ts_diff = function
| [] -> true
| [x] -> true
| t::q -> (not (membre t q)) && (ts_diff q)
;;

(*
  | t::q -> if membre t q 
            then true 
            else ts_diff q
*)

let rec ts_diff_triee = function
| [] -> true
| [x] -> true
| a::b::q -> a <> b && ts_diff_triee b::q
;;

let t = [|1;2;13;4;34;34;864;3;137;43;65|] ;;
t.(9);;

t.(vect_length(t) -1);;
t.(7) <- 43;;
 
let rec remplir_dep ind t u =
 if ind >= vect_length t
 then ()
 else begin
  t.(ind) <- u(ind) ;
  remplir_dep (ind+1) t u
  end
;;

let cr_t n =
 let t = make_vect n 0 in
 remplir_dep 0 t (fun x -> x + 1)
;;

(*
let rec dich vect start finish comp =
 if start > finish
      then print_string "No -_-"
 else if start = finish
      then if vect.(start) = comp
           then start
	       else -1
 else if vect.(start) = comp then start
 else if vect.(finish) = comp then finish
 else  
	  
*)

let rec ppind t i j x =
  if j = i + 1
  then
    if x <= t.(i)
	then i
	else j
  else
    let c = (i+j)/2 in
    if t.(c) < x
    then ppind t c j x
    else ppind t i c x
;;

(* Recherche d'un elem dans un tableau range dans l'ordre croissant :
   on renvoie l'indice de sa premiere occurence si on le trouve,
   et -1 sinon
*)
let indice t x =
  if t.(0) > x || t.(vect_length(t) -1) < x
  then -1
  else 
    let ind = ppind t 0 (vect_length(t) -1) x in
    if t.(ind) = x
    then ind 
	else -1
;;
