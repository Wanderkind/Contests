import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


void sol(){
    
    double p = 0.28442912381662033;
    double x;
    int b = 0;

    foreach(_; 0..5000){
        scanf("%lf", &x);
        if(p < x && x <= 1-p){
            b++;
        }
    }
    //writeln(b);
    writeln(b > 2337 ? "B" : "A");
}

void main(){
    
    /*
    int t;
    scanf("%d", &t);
    */
    int t = 100;

    while(t--){
        sol();
    }
    
    
    //sol();
}
