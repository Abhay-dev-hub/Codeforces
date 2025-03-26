#include <iostream>
using namespace std;

int main() {
    int x , y;
    cin >> x >> y;
    if((x * y) % 2 == 0){
        cout << (x * y)/2 << endl;
    }
    else{
        cout << ((x * y)/2) << endl;
    return 0;
    }
}