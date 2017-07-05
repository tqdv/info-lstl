(*
On crée un tableau avec la longueur de la plssc terminant à cet indice,
puis, pour chaque élément non-rempli, on parcourt la liste des plssc à indice inférieur,
si la dernière valeur de cette ssc est inférieure à la valeur de l'élément à cet nouvel indice,
on prend le max de ces longueur + 1
*)

let rec petit_max n l deb i mx x =
	if deb >= i
	then mx
	else if hd(l) <= x
	then petit_max n (tl l) (deb + 1) i (max (1 + n.(deb)) mx) x
	else petit_max n (tl l) (deb + 1) i  mx x
;;
(* 
n : partially filled table w/ maxes
deb : current
i : index
mx : partial maximum
l : list
x : value at index
*)

let rec toutni n l r i =
	match r with
	| [] -> ()
	| x :: q ->
		n.(i) <- petit_max n l 0 i 1 x;
		toutni n l q (i+1)
;;

let maxi t a b =
	let ind = ref a in
	for i = a + 1 to b do
		if t.(i) > t.(!ind)
		then ind := i
	done;
	!ind
;;

let l_plssc l =
	let n = make_vect (list_length(l)) 0 in
	toutni n l l 0;
	n.(maxi n 0 (vect_length(n) - 1))
;;

let plssc l =
	let n = make_vect (list_length l) 0 in
	toutni n l l 0;
	let ind = maxi n 0 (vect_length(n) - 1) in
	let rec aux lg x i r =
		match r with
		| [] -> []
		| y :: q ->
			if y <= x && n.(i) = lg - 1
			then y :: (aux (lg - 1) y (i - 1) q)
			else aux lg x (i - 1) q
	in rev (aux (n.(ind) + 1) max_int (vect_length(n) - 1) (rev l))
;;

let mots_en_chaine s =
	let rec aux i j =
		if j >= string_length s
		then
			if i < j
			then [sub_string s i (j - i)]
			else []
		else
			match s.[j] with
			| ` ` | `.` | `,` | `;` | `:` | `(` | `)`
			| `\n` | `!` | `?`
			->
				if i < j
				then (sub_string s i (j - i) :: (aux (j + 1) (j + 1)))
				else aux (j + 1) (j + 1)
			| _ -> aux i (j + 1)
	in aux 0 0
;;

(* DICTIONNAIRES *)

let ajouter dico cle elt = (cle, elt) :: dico;;

let rec supprimer dico cle =
	match dico with
	| [] -> []
	| (c, x) :: q ->
		if c = cle
		then q
		else (c, x) :: (supprimer q cle)
;;

let rec elt_of_cle dico cle =
	match dico with
	| [] -> failwith "Elem introuvable"
	| (c, x) :: q ->
		if c = cle
		then x
		else elt_of_cle q cle
;;

let rec modif_cle dico cle nv_cle =
	match dico with
	| [] -> failwith "Do it
Just do it

Don't let your dreams be dreams
Yesterday you said tomorrow
So just do it
Make your dreams come true
Just do it

Some people dream of success
While you're gonna wake up and work hard at it
Nothing is impossible

You should get to the point
Where anyone else would quit
And you're not going to stop there
No, what are you waiting for?

Do it
Just do it
Yes you can
Just do it
If you're tired of starting over
Stop giving up"
	| (c, x) :: q ->
		if c = cle
		then (nv_cle, x) :: q
		else (c, x) :: modif_cle dico cle nv_cle
;;

int_of_char `z`