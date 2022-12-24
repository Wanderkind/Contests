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
    
    long b, c, a0, a1;
    scanf("%lld %lld %lld %lld", &b, &c, &a0, &a1);

    double s = sqrt(cast(double)4*c+b*b);
    printf("%.12lf\n", cast(double)(b+s)/2);
}

void main(){
    
    /*
    int t;
    scanf("%d", &t);

    while(t--){
        writeln(sol());
    }
    */
    
    sol();
}B
