open Scanf
open Printf
open String
;;
let explode s = List.init (length s) (get s)
;;
let f s =
  let addscore = function
    | ':' -> 1
    | '_' -> 5
    | _ -> 0 in
  let rec g = function
    | [] -> 0
    | h :: t -> g t + addscore h in
  (s |> explode |> g) + length s
;;
scanf "%s\n" (fun s -> s |> f |> printf "%d\n")
;;
