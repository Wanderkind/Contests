open Scanf;;
scanf "%d %d\n" @@ fun c h ->
  let n _ =
    scanf "%d:%d:%d\n" @@ fun hr mn sc ->
      hr*3600 + mn*60 + sc in
  let rec f lst = function
  | 0 -> lst
  | x -> f (n () :: lst) @@ x - 1 in
  let lc = f [] c in
  let lh = f [] h in
  let etoe x y =
    let d = abs @@ x - y in
    if d < 40 then 40 - d else 0 in
  let rec etol x = function
  | [] -> 0
  | h :: t -> (etoe x h) + etol x t in
  let rec ltol = function
  | [] -> 0
  | h :: t -> etol h lc + ltol t in
  let z = ltol lh in
  86400 - 40*(c + h) + z |> print_int
