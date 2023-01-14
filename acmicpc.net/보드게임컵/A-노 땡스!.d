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


void main(){
    
    int n;
    scanf("%d", &n);
    int score;
    scanf("%d", &score);
    int temp = score, c;
    foreach(_; 1..n){
        scanf("%d", &c);
        if(c != temp+1){
            score += c;
        }
        temp = c;
    }

    writeln(score);
}
