Scanf.scanf "%s\n" @@ fun s ->
  let rec f = function
  | "northlondo" -> "NLCS"
  | "branksomeh" -> "BHA"
  | "koreainter" -> "KIS"
  | "stjohnsbur" -> "SJA"
  | s -> (
    let explode s = List.init (String.length s) (String.get s) in
    let rec convert = function
    | [] -> []
    | h :: t -> char_of_int ((int_of_char h - 96) mod 26 + 97) :: convert t in
    let rec recomb = function
    | [] -> ""
    | h :: t -> Char.escaped h ^ recomb t in
    s |> explode |> convert |> recomb |> f
  ) in s |> f |> print_string
