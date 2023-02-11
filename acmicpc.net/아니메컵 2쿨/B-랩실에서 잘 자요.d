import std.stdio;
import std.algorithm;
import std.math;
import std.conv;
//import std.numeric;
//import std.range;
import std.array;
//import std.bigint;
//import std.string;
import core.stdc.stdlib;


void main () {

    int n, m;
    scanf("%d %d\n", &n, &m);
    int[] lost, pages = readln.splitter.map !(to !(int)).array;
    
    foreach (i; 1..n+1) {
        if (! pages.canFind(i)) {lost ~= i;}
    }
    ulong l = lost.length;
    if (l < 2) {
        writeln(7*l);
        exit(0);
    }

    int ans = 0, left = lost[0], right = lost[0];
    foreach (i; lost[1..$]) {
        if (i - right < 4) {
            right = i;
        }
        else {
            ans += (right - left + 1)*2 + 5;
            left = i;
            right = i;
        }
    }

    ans += (right - left + 1)*2 + 5;
    writeln(ans);
}
