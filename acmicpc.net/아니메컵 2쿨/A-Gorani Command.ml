open Printf
open Scanf
;;
let rec intarr = function | 1 -> [scanf "%d\n" (fun n -> n)] | x -> scanf "%d " (fun n -> n :: intarr (x-1))
;;
let sol n m =
  let rec minvert = function
    | 0 -> 100
    | x -> min (scanf "%d\n" (fun n -> n)) (minvert (x-1)) in
  let mvt = minvert (n-1) in
  let rec minhor = function
    | [] -> 100
    | h :: t -> min h (minhor t) in
  let arr = intarr m in
  let mh = minhor arr in
  let first = function
    | [] -> 0
    | h :: t -> h in
  let mv = min mvt (first arr) in
  let (a, b) = (n - mh , mv + 1) in
  printf "%d %d\n" a b
;;
scanf "%d %d\n" (fun n m -> sol n m)
;;
