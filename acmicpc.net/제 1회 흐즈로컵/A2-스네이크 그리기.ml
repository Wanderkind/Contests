open Printf;;
Scanf.scanf "%d %d\n" @@ fun a b ->
  printf "%d\n" (a*b/2*2);
  for i = 1 to a do printf "%d 1\n" i done;
  if a mod 2 = 0 then
    for i = 0 to a/2 - 1 do
      for j = 2 to b do printf "%d %d\n" (a - 2*i) j done;
      for j = 0 to b - 2 do printf "%d %d\n" (a - 2*i - 1) (b - j) done;
    done
  else (
    for j = 2 to b do printf "%d %d\n" a j done;
    for i = 0 to a/2 - 2 do
      for j = 0 to b - 2 do printf "%d %d\n" (a - 2*i - 1) (b - j) done;
      for j = 2 to b do printf "%d %d\n" (a - 2*i - 2) j done;
    done;
    printf "2 %d\n" b;
    let r = b mod 2 in
    if r = 0 then (
      printf "1 %d\n" b;
    )
    else (
      printf "2 %d\n" (b - 1);
      printf "1 %d\n" (b - 1););
    for j = 1 to b/2 - 1 do
      printf "1 %d\n" (b - 2*j + 1 - r);
      printf "2 %d\n" (b - 2*j + 1 - r);
      printf "2 %d\n" (b - 2*j - r);
      printf "1 %d\n" (b - 2*j - r);
    done)
