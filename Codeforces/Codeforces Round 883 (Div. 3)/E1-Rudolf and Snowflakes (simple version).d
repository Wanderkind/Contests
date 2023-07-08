import std;


bool f(long n, long k) {
    if(n == 1) return false;
    if(n % k == 1) {
        long y = (n - 1)/k;
        if(y == 1) return false;
        else if(y == k + 1) return true;
        else return f(y, k);
    }
    return false;
}

bool sol() {
    long n;
    scanf("%ld", &n);
    long nn = n - 1;
    double s = sqrt(cast(double)nn);
    long k = 1;
    while(k <= s) {
        k++;
        if(f(n, k)) return true;
    }
    return false;
}

void main() {
    int t;
    scanf("%d", &t);
    while(t--) {
        writeln(sol() ? "YES" : "NO");
    }
}
