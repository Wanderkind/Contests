open Printf
open Scanf
;;
let f n =
  if n mod 3 = 0 then (0, 1)
  else if n mod 3 = 1 then (1, 0)
  else (-1, -1)
;;
let add a b = (fst a + fst b, snd a + snd b)
;;
let rec sol = function
  | 1 -> scanf "%d\n" (fun n -> f n)
  | x -> scanf "%d " (fun n -> add (f n) (sol (x-1)))
;;
scanf "%d\n" (fun n -> let (p, q) = sol n in printf "%d %d\n" p q)
;;
