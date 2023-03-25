Scanf.scanf "%s\n" @@ fun s ->
  print_string @@ match s with
  | "BHA" -> "Branksome Hall Asia"
  | "KIS" -> "Korea International School"
  | "SJA" -> "St. Johnsbury Academy"
  | _     -> "North London Collegiate School"
