open Int64;;
Scanf.scanf "%Ld %Ld\n" @@ fun x n ->
  let rec f t = function
  | 4L -> print_int 4
  | 8L -> List.nth [8; 2; 7] @@ (rem t 3L |> to_int) |> print_int
  | 0L -> List.nth [0; 6; 5; 12] @@ (rem t 4L |> to_int) |> print_int
  | x  -> (
    if t = 0L then x |> to_int |> print_int
    else f (sub t 1L) @@ if rem x 2L = 0L then logxor (div x 2L) 6L else logxor (mul 2L x) 6L
  ) in f n x
