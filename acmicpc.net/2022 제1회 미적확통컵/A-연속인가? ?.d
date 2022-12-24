import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


void sol(){
    
    long k, a, b, c, d;
    scanf("%lld\n%lld %lld %lld %lld", &k, &a, &b, &c, &d);

    if(a*k+b == c*k+d){
        writeln("Yes ", a*k+b);
    }
    else{
        writeln("No");
    }
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
}
