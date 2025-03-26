#include <iostream>
#include <cmath>

using namespace std;
 
int main(){
    int k ,n ,w , total , needed;
    cin >> k >> n >> w;
    total = k * (w *(w + 1)/2);
    needed = total - n;
    cout << max(0,needed);


    return 0;
}