#include <stdio.h>


int main(void){
	long n,m,i,k;
	scanf("%ld %ld", &n,&m);
	long a[n+1];
	for (i=0;i<n;i++){
		scanf("%ld",&k);
		a[i]=k;
	}
	long d[n];
	for (i=0;i<n-1;i++){
		d[i]=a[i]-a[i+1];
	}
	long s,t,j,w;
	long D;
	for (i=0;i<m;i++){
		D=0;
		scanf("%ld %ld",&s,&t);
		if (s<t){
			for (j=0;j<t-s;j++){
				w=d[s-1+j];
				D+=w>0?w:0;
			}
		}
		else{
			for (j=0;j<s-t;j++){
				w=d[t-1+j];
				D+=w<0?-w:0;
			}
		}
		printf("%d\n",D);
	}
	return 0;
}
