import std.stdio;
import core.stdc.stdlib;


void main() {

    int n, m, k, t, r, acc = 0;
    scanf("%d %d %d", &n, &m, &k);
    foreach(i; 1..m+1) {
        scanf("%d %d", &t, &r);
        acc += r;
        if(acc > k) {
            printf("%d 1", i);
            exit(0);
        }
    }
    writeln(-1);
}
