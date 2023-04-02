Scanf.scanf "%s %d\n%s %d\n%s %d\n%s %d\n" @@ fun a b c d e f g h ->
  let z y = function
  | "Es" -> 21*y
  | _ -> 17*y in
  z b a + z d c + z f e + z h g |> print_int
