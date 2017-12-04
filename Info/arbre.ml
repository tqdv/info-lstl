type ('n, 'f) arbre_binaire =  
  | Arbre_vide 
  | Feuille of 'f
  | Noeud of 'n * ('n, 'f) arbre_binaire * ('n, 'f) arbre_binaire

type squelette = Sq_vide | Sq_noeud of squelette * squelette

(* a : arbre
 * (n, g, d) : (noeud, sous-arbre gauche, sous-arbre droite)
 *)

let est_vide a = a = Arbre_vide

let racine = function
  | Arbre_vide -> failwith "Arbre vide"
  | Feuille _ -> failwith "Feuille"
  | Noeud(n, _, _) -> n

(* Sous-arbre gauche et droit*)
let sag = function
  | Arbre_vide -> failwith "Arbre vide"
  | Feuille _ -> failwith "Feuille"
  | Noeud(_, g, _) -> g
let sad = function
  | Arbre_vide -> failwith "Arbre vide"
  | Feuille _ -> failwith "Feuille"
  | Noeud(_, _, d) -> d

(* Etiquette d'une feuille *)
let f_etiquette = function
  | Arbre_vide -> failwith "Arbre vide"
  | Feuille f -> f
  | Noeud(_, _, _) -> failwith "Noeud"

(* Squelette d'un arbre *)
let rec radio = function
  | Arbre_vide -> Sq_vide
  | Feuille _ -> Sq_vide
  | Noeud(_, g, d) -> Sq_noeud(radio g, radio d)

(* Mirroir d'un squelette *)
let rec miroirV = function
  | Sq_vide -> Sq_vide
  | Sq_noeud(g, d) -> Sq_noeud(miroirV d, miroirV g)

(*
let miroirV_cps a =
Créer un arbre en continuation ne semble pas être possible
*)

let rec meme_structure a1 a2 =
  match a1, a2 with
    | Noeud(n1, g1, d1), Noeud(n2, g2, d2) ->
        n1 = n2 && meme_structure g1 g2 && meme_structure d1 d2
    | Noeud(_, _, _), _ -> false
    | _, Noeud(_, _, _) -> false
    | _, _ -> true


let rec hauteur = function
  | Arbre_vide
  | Feuille _ -> 0
  | Noeud(n, g, d) -> 1 + max (hauteur g) (hauteur d)

let hauteur_rt a =
  let rec aux m = function
    | [] -> m
    | (Arbre_vide, _) :: q -> aux m q
    | (Feuille _, h) :: q -> aux m q
    | (Noeud(_, g, d), h) :: q ->
          let h' = h + 1 in
          aux (max m h) ((g, h') :: (d, h') :: q)
  in aux 0 [(a, 1)]

let rec print_arbre = function
  | Arbre_vide -> print_string "V"
  | Feuille _ -> print_string "F"
  | Noeud(_, g, d) ->
      print_string "N(";
      print_arbre g;
      print_string ", ";
      print_arbre d;
      print_string ")"

let rec print_sq = function
  | Sq_vide -> print_string "S_V"
  | Sq_noeud(g, d) ->
      print_string "S_N(";
      print_sq g;
      print_string ", ";
      print_sq d;
      print_string ")"

(* type appel_fc = Appel_V | Appel_N *)

(* qp : queue d'aPpels *)
let miroirV_rec a =
  let rec aux reste squels appels =
    match reste, squels, appels with
      | _, [a], [] -> a
      | _, (a :: b :: q), [0] -> aux reste (Sq_noeud(a, b) :: q) []
      | _, (a :: b :: q), (0 :: p :: qp) ->
        aux reste (Sq_noeud(a, b) :: q) ((p-1) :: qp)
      | [], _, _ -> failwith "reste = [], squels et appels non corrects"
      | Arbre_vide :: q, _, [] -> aux q (Sq_vide :: squels) []
      | Arbre_vide :: q, _, (p :: qp) -> aux q (Sq_vide :: squels) ((p-1) :: qp)
      | Feuille _ :: q, _, _ -> aux (Arbre_vide :: q) squels appels
      | Noeud(_, g, d) :: q, _, _ -> aux (g :: d :: q) squels (2 :: appels)
(*      | _, _, [] -> failwith "nb_squels <> 1 et appels = []" *)
  in aux [a] [] []
