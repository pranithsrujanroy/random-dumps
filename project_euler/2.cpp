/*
Even fibonacci numbers
*/
#include<iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        long n;
        cin >> n;
        long long a,b,c=2;
        a = 1;
        b = 2;
        long long sum = 0;
        while(c<n){
            if(c%2==0)
                sum+=c;
            c = a+b;
            a = b;
            b = c;
        }
        cout<<sum<<endl;
    }
    return 0;
}