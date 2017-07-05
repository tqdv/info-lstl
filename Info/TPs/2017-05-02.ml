(* ech : 'a vect -> int -> int -> unit *)

let ech t i j =
  let aux = t.(i) in
  t.(i) <- t.(j) ;
  t.(j) <- aux
;;

(* Tri par selection *)

let indice_min_a t =
  let min = ref t.(0) and out = ref 0 in
  for i = 0 to vect_length(t) - 1 do
    let current = t.(i) in
	if current < !min
	then 
	  min := current;
	  out := i
  done;
  out
;;

let indice_min t a b =
  let ind = ref a in
  for i = a + 1 to b do
    if t.(i) < t.(!ind)
	then ind := i
  done;
  !ind
;;

let tri_selection t =
  for j = 0 to vect_length(t) -2 do
    let i = indice_min t j (vect_length(t) -1) in
	ech t i j
  done
;;

(* Tri par insertion *)
let inserer t i =
  let j = ref i in
  while !j > 0 && t.(!j -1) > t.(!j) do
    ech t (!j -1) !j;
    decr j;
  done
;;

let rec inserer_r t i =
  if i > 0 && t.(i -1) > t.(i)
  then (
    ech t (i -1) i;
	inserer t (i-1)
  )
;;

let tri_insertions t =
  for i = 0 to vect_length(t) -1 do
    inserer t i
  done
;;

(* Quicksort (go look it up on Wikipedia) *)

(* Pivot *)
let pivotage t a b =
  let i = ref a and j = ref b in
  while !i < !j do
    if t.(!i +1) <= t.(!i)
	then (
	  ech t !i (!i +1);
	  incr i
	) else (
	  ech t (!i +1) !j;
	  decr j
	)
  done;
  !i
;;

let tri_rapide t =
  let rec aux a b =
    let i = pivotage t a b in
	if a < i -1
	then aux a (i - 1) ;
	if i + 1 < b
	then aux (i +1) b
  in aux 0 (vect_length(t) -1)
;;

exception Break;;

let chercher t x =
  try 
    for i = 0 to vect_length(t) -1 do
	  if t.(i) = x
	  then raise Break
	done;
	false
  with 
  | Break -> true
;;
  