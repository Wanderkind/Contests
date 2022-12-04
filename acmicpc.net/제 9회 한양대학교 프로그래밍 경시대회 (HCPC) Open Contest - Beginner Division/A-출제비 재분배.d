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


void sol(){
    
    int n, m;
    scanf("%d %d", &n, &m);

    int[2001] c = 0;
    int money;

    foreach(i; 0..n){
        scanf("%d", &c[i]);
    }

    foreach(i; 0..n){
        
        foreach(u; 0..n+m){

            scanf("%d", &money);
            c[i] -= money;
            c[u] += money;
        }
    }

    foreach(i; 0..n+m){
        printf("%d ", c[i]);
    }
}

void main(){

    sol();
}
