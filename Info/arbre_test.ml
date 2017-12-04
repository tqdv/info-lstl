(* to compile and run:
       ocamlopt -o arbre_test arbre.ml arbre_test.ml
       ./arbre_test
*)


open Arbre
open Printf
let () =
  let a1 =
    Noeud(1, 
      Noeud(2, Arbre_vide, Arbre_vide),
      Noeud(3, 
        Noeud(4, Arbre_vide, Arbre_vide),
        Noeud(5, Arbre_vide, Arbre_vide)
      )
    )
  and a2 =
    Noeud(1, 
      Feuille(2),
      Noeud(3, 
        Feuille(4),
        Feuille(5)
      )
    )
  in
  printf "hauteur(a1) = %d\n" (hauteur a1);
  printf "hauteur_rt(a1) = %d\n" (hauteur_rt a1);
  printf "hauteur(a2) = %d\n" (hauteur a2);
  print_string "a1 = ";
  print_arbre a1;
  print_newline();
  print_string "a2 = ";
  print_arbre a2;
  print_newline();
  print_string "miroirV_rec a1 = ";
  miroirV_rec a1 |> print_sq;
  print_newline()

