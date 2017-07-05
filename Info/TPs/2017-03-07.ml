let rec minimum = function
| []   -> failwith "Pas de minimum"
| [x]  -> x
| t::q -> let m = minimum(q) in
          if t < m
		  then t
		  else m
;;

let rec extraire_min = function
| []   -> failwith "vide"
| [x]  -> x, []
| t::q -> let (m, reste) = extraire_min q in
          if t <= m
          then t, q
		  else m, t::reste
;;

let rec extraire_min_p prefix << = function
| []   -> failwith "vide"
| [x]  -> x, []
| t::q -> let (m, reste) = extraire_min prefix << q in
          if t << m
          then t, q
		  else m, t::reste
;;

let rec tri l =
 if l = []
 then []
 else let (m, reste) = extraire_min l in
      m :: (tri reste)
;;

let rec distribuer x = function
| [] -> []
| p1 :: autres_p -> (x::p1):: p1 :: (distribuer x autres_p)
;;

let rec parties = function
| [] -> [[]]
| t::q -> distribuer t (parties q)
;;

let rec cat l1 l2 =
 match l1 with
 | [] -> l2
 | t::q -> t :: cat q l2
;;

let rec fab_l = function
| 0 -> []
| n -> 0 :: fab_l (n-1)
;;

let time_cat l1 l2 =
 let deb = sys__time() in
 let _ = cat l1 l2 in
 sys__time() -. deb
;;

let rec est_triee prefix $> = function
| [] -> true
| [x] -> true
| a :: b :: q -> (a $> b) && (est_triee prefix $> (b :: q))
;;

let est_cr = est_triee prefix <= ;;
let est_str_cr = est_triee prefix < ;;
let est_cst = est_triee prefix = ;;

let rec ins_elem x = function 
| [] -> [x]
| t :: q -> if x <= t
            then x :: t :: q
			else t :: (ins_elem x q)
;;

let rec tri_ins = function
| [] -> []
| t::q ->  ins_elem t  (tri_ins q)
;;

(* This actually isn't a sorting algorithm *)
let rec merge_sort l1 l2 =
 match (l1, l2) with
 | ([], l) -> l
 | (l, []) -> l
 | (t1::q1, t2::q2) -> if t1 <= t2
                       then t1 :: merge_sort q1 (t2::q2)
					   else t2 :: merge_sort (t1::q1) q2
;;


let rec split = function
| [] -> [], []
| [x] -> [x], []
| x1::x2::q -> let (a, b) = split(q) in
               x1::a, x2::b
;;

(* This is actually a sorting algorithm *)
let rec mmergee = function
| [] -> []
| [x] -> [x]
| l -> let (a, b) = split l in
       merge_sort (mmergee a) (mmergee b)
;;

let rec randl = function
| 0 -> []
| n -> random__int 1000 :: randl (n - 1)
;;
