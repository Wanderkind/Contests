open Scanf
open Printf
;;
let rec f n =
  if n=1 then
    scanf "%s %d\n" (fun a c ->
      match a with
      | "STRAWBERRY" -> (c, 0, 0, 0)
      | "BANANA" -> (0, c, 0, 0)
      | "LIME" -> (0, 0, c, 0)
      | _ -> (0, 0, 0, c)
    )
  else
    let (s, b, l, p) = f (n-1) in
    scanf "%s %d\n" (fun a c ->
      match a with
      | "STRAWBERRY" -> (s+c, b, l, p)
      | "BANANA" -> (s, b+c, l, p)
      | "LIME" -> (s, b, l+c, p)
      | _ -> (s, b, l, p+c)
    )
;;
let n = read_int() in
let (s, b, l, p) = f n in
if s=5 || b=5 || l=5 || p=5 then printf "YES\n" else printf "NO\n"
;;
