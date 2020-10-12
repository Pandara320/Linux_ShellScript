//
//  week2quiz1.cpp

#include <iostream>
#include <fstream>
using namespace std;
int calculation1(int n)
{
    int ans=0;
    for (int i=1; i< n; i++)
    {
        if(i< n/2) {
            ans -= i;
        }
        else
        {
            ans += i;
        }
    }
    return ans;
}
int calculation2(int x, int n)
{
    for(int i = 0; i< n; i++)
    {
        if(i % 2 ==0)
        {
            x*=i+1;
            continue;
        }
        x--;
        if(x==0)
        {
            break;
        }
    }
    return x;
}

int main(void) {
    // insert code here...
    
    int myAnswer1 = calculation1(5);
    int myAnswer2 = calculation2(1,3);
    
    std::cout << "my answer1 is: " << myAnswer1 <<endl;
    std::cout << "my answer2 is: " << myAnswer2 <<endl;
    
    return 0;
}
