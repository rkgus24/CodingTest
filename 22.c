#include<stdio.h>
#include<vector>

using namespace std;			

int main(){
	freopen("input.txt", "rt", stdin);
	int n, k, i, sum=0, res;
	scanf("%d %d", &n, &k);
	vector<int> a(n);

	for(i=0; i<n; i++){
		scanf("%d", &a[i]);
	}

	for(i=0; i<k; i++){
		sum=sum+a[i];
	}

	res=sum;

	for(i=k; i<n; i++){
		sum=sum+(a[i]-a[i-k]);
		if(sum>res) res=sum;
	}

	printf("%d\n", res);

	return 0;
}