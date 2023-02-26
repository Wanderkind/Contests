import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;

int p (long n) {

    int ans = 0;
    while (n > 1) {
        n >>= 1;
        ans++;
    }
    
    return ans;
}

void main () {
    
    int n;
    scanf("%d", &n);

    int[63] arr = 0;
    long d;
    foreach (i; 0..n) {
        scanf("%lld", &d);
        if (d) {arr[p(d)]++;}
    }
    
    foreach (i; 0..62) {
        arr[i + 1] += arr[i]/2;
    }
    
    int s = 62;
    long a = 1;
    while (!arr[s]) {s--;}
    writeln(a << s);
}
