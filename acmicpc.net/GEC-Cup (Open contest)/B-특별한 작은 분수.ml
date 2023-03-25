Scanf.scanf "%d %d\n" @@ fun x n -> let rec f x t = if n = t then print_int x else f (if x mod 2 = 0 then (x/2) lxor 6 else (2*x) lxor 6) @@ t + 1 in f x 0
