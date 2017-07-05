
(* Teste si elem est dans la liste *)
let rec est_dedans x l =
 match l with
 | [] -> false
 | t::q -> (t = x) || est_dedans x q
;;

(* Teste inclusion *)
let rec inclus a b =
 match a with
 | [] -> true
 | x::q -> (est_dedans x b) && (inclus q b)
;;

(* Calcul de l'union *)
let rec union a b =
 match a with
 | [] -> b
 | x::q -> if est_dedans x b
           then union a b
		   else x:: (union a b)
;;

(* Calcul intersect *)
let rec inter a b =
 match a with 
 | [] -> []
 | x::q -> if est_dedans x b
            then x::(inter  q b)
			else inter q b
;;

(* Cas des listes triees dans l'ordre croissant *)
let rec est_dedans_triee x l =
 match l with
 | [] -> false
 | t::q -> if t = x
           then true
		   else if t < x
		   then est_dedans_triee x q
		   else false
;;

(* Inclusion *)
let rec inclus_triee a b =
 match (a, b) with
 | ([], _) -> true
 | (_, []) -> false
 | (x1::q1, x2::q2) -> 
    if x1 = x2
    then inclus_triee q1 q2
	else if x1 < x2
	then false
	else inclus_triee a q2
;;

let rec intersec_triee a b =
 match (a, b) with
 | ([], _) -> []
 | (_, []) -> []
 | (t1::q1, t2::q2) ->
     if t1 = t2
	 then t1::(intersec_triee q1 q2)
	 else if t1 < t2
	 then intersec_triee q1 b
	 else intersec_triee a q2
;;

let rec union_triee a b =
 match (a, b) with
 | ([], _) -> b
 | (_, []) -> a
 | (t1::q1, t2::q2) ->
     if t1 = t2
	 then t1::(union_triee q1 q2)
	 else if t1 < t2
	 then t1::(union_triee q1 b)
	 else t2::(union_triee a q2)
;;

let succ = function
 | 0 -> [0; 1]
 | 1 -> [2]
 | 1000 -> []
 | x -> 
     if x <= 500
     then [x + 1; 2*x]
	 else [x+1]
;;

let rec suivants p =
 match p with
 | [] -> []
 | x::q -> union_triee (succ x) (suivants q)
;;

(* Cherche le plus petit n tq x mene a y en n etapes *)
let distance x y =
 if x > y
 then failwith "Nope"
 else 
  let rec parcours_en_largeur n p =
   if est_dedans_triee y p
   then n
   else parcours_en_largeur (n+1) (union_triee p (suivants p))
  in parcours_en_largeur 0 [x]
;;