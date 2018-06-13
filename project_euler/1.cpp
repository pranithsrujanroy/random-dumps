/* 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3 5 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

*/
#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        long a,b,c;
        a = (n-1)/3;
        b = (n-1)/5;
        c = (n-1)/15;
        
        long total = 3*a*(a+1)/2 + 5*b*(b+1)/2 - 15*c*(c+1)/2;
        cout<<total<<endl;
    }
    return 0;
}
