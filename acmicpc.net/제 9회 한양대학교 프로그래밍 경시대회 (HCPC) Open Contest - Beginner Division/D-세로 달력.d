import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;

int yoon(int n){

    if(n%400 == 0){
        return 29;
    }

    if(n%100 == 0){
        return 28;
    }

    if(n%4 == 0){
        return 29;
    }

    return 28;
}

void sol(){
    
    int n, m;
    scanf("%d\n%d", &n, &m);

    int[12] days = [31, yoon(n), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    int count = 0;
    int i, a, t, f;

    foreach(h; 0..12){

        i = days[h]-21;
        t = 8-m;
        a = t;
        i -= t;

        m = i>6 ? i-6 : i+1;
        f = max(0, a+i-7);
        
        count += f;
        //printf("%d %d\n", h+1, f);////////////////////
    }

    writeln(count);
}

void main(){

    sol();
}
