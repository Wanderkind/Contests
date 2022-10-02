# include <stdio.h>

int max(int a, int b){
	return a>b?a:b;
}

int min(int a, int b){
	return a<b?a:b;
}

int f1(int p){
	return max(0,p-500);
}

int f2(int p){
	return p*9/10;
}

int f3(int p){
	return max(0,p-2000);
}

int f4(int p){
	return p*3/4;
}

int slv(int n, int p){
	if (n<5){
		return p;
	}
	else if (n<10){
		return f1(p);
	}
	else if (n<15){
		return min(f1(p),f2(p));
	}
	else if (n<20){
		return min(f2(p),f3(p));
	}
	else{
		return min(f3(p),f4(p));
	}
}

int main(void){
	
	int n,p;
	scanf("%d",&n);
	scanf("%d",&p);
	
	printf("%d",slv(n,p));
	
	return 0;
	
}
