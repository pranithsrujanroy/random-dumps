/*
Largest prime factor
*/
#include<iostream>
#include<cmath>
using namespace std;

long largest_prime_factor(long long n){
	if(n==0||n==2)
		return n;
	while(!n%2)
		n/=2;
	if(n==1)
		return 2;
	long i;
	for(i=3;i<=sqrt(n);i+=2){
		while(n%i==0)
			n=n/i;
		if(n==1)
			break;
	}
	if(n>2)
		return n;
	else 
		return i;
}

int main(){
	int t;
	cin>>t;
	for(int a = 0;a < t;a++){
		long long n;
		cin>>n;
		cout<<largest_prime_factor(n)<<endl;
	}
}