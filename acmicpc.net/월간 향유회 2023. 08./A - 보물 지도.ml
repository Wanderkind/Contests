open Int64
;;
let rec f tp dn lf rt = function
| 0 -> (tp, dn, lf, rt)
| t -> Scanf.scanf "%Ld %Ld %c\n" @@ fun x y c -> (
  match c with
  | 'L' -> f tp dn lf (min rt @@ sub x 1L) @@ t - 1
  | 'R' -> f tp dn (max lf @@ add x 1L) rt @@ t - 1
  | 'U' -> f tp (max dn @@ add y 1L) lf rt @@ t - 1
  | 'D' -> f (min tp @@ sub y 1L) dn lf rt @@ t - 1
  | _   -> assert false
);;
let bnd = 1000000001L
;;
let n = read_int ()
;;
let (tp, dn, lf, rt) = f (bnd) (neg bnd) (neg bnd) (bnd) n
;;
if tp = bnd || dn = neg bnd || lf = neg bnd || rt = bnd then print_endline "Infinity"
else Printf.printf "%Ld\n"@@ mul (add 1L @@ sub tp dn) (add 1L @@ sub rt lf)
;;
