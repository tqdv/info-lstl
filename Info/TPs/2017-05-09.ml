(* ABANDONNE *)

(*
  On veut calculer le prochain element de l'ensemble des permutations
  avec ... (?)
*)

let tri = sort__sort (prefix <=);;

(*
  Trouve le plus petit elem m d'une liste superieur a x, et renvoie
  (m, (tri (x :: l'))) où l' s'obtient à partir de l en retirant m
*)
let rec min_et_tri x = function
  | [] -> failwith "La liste est vide"
  | [t] ->
    if t <= x
	then (false, x, [])
	else (true, t, [x])
  | t::q ->
    let (b, m, s) = min_et_tri x q in
	if t <= x || (b && t > m)
	then (true, m, tri(t::s))
	else if t > x
	then (true, t, tri(x::q))
	else (false, x, [])
;;

(*
  Retourne s'il est possible de trouver un successeur, et le retourne
  s'il existe
*)
let rec augmenter = function
  | [] -> (false, [])
  | [_] -> (false, []) 
  | x1 :: x2 :: q ->
    let (b, q') = augmenter (x2 :: q) in
	if b
	then (true, x1 :: q')
    else
	  let (b', m, s) = min_et_tri x1 (x2::q) in
	  if b'
	  then (true, m::s)
	  else (false, [])
;;

let permutation_suivante l =
  let (b, l') = augmenter l in l'
;;

(* Return last *)







let creer m n =
  let t = make_vect m [| |] in
  for i = 0 to m - 1 do
    t.(i) <- make_vect n 0
  done;
  t
;;

let ex1 n =
  let t = make_matrix n n 0 in
  for i = 0 to n - 1 do
    for j = 0 to n - 1 do
      t.(i).(j) <- (i + j) mod n + 1
    done
  done;
  t
;;

let creer_tableau_vide(n) = make_vect n None;;

let ajouter t x =
  let i = ref 0 in
  while !i < vect_length(t) && t.(!i) <> None do
    incr i
  done;
  if  !i  = vect_length(t)
  then failwith "Le tableau est plein"
  else t.(!i) <- Some x
;;

let retirer t x =
  let i = ref 0 in
  while !i < vect_length(t) && t.(!i) <> Some x do
    incr i
  done;
  if  !i  = vect_length(t)
  then failwith "Pas dans le tableau"
  else t.(!i) <- None
;;

let retirer_tous t x =
  for i = 0 to vect_length(t) -1 do
    if t.(i) = Some x
	then t.(i) <- None
  done
;;

let taille_gros t =
  let m = ref 0 in
  for i = 0 to vect_length(t) do
    for j = 0 to vect_length(t.(0)) do
	  m := max !m (string_length (string_of_int t.(i).(j)))
	done
  done;
  !m
;;

let afficherb k =
  for i = 1 to k do
    print_string " "
  done
;;

let printy t =
  let m = taille_gros t in
  for i = 0 to vect_length(t) -1 do
    print_string "| ";
	for j = 0 to vect_length(t.(0)) -1 do
	  afficher_blancs(m - string_length (string_of_int t.(i).(j)));
	  print_int t.(i).(j);
	  print_string " ";
	done;
    print_string "|";
	print_newline()
  done
;;

let t = [|[|1; 500|];[|-102;5|]|];;