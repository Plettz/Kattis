#include <iostream>
#include <string>

using namespace std;

int main()
{
    string word;
    int b{0}, k{0};
    
    cin >> word;
    
    for (int i=0; i < word.length(); ++i)
    {
        if (word[i] == 'b')
        {
            b++;
        }
        
        if (word[i] == 'k')
        {
            k++;
        }
    }
    
    if (b == 0 && k == 0)
    {
        cout << "none";
    }
    else if (b > k)
    {
        cout << "boba";
    }
    else if (b < k)
    {
        cout << "kiki";
    }
    else
    {
        cout << "boki";
    }
    
    return 0;
}
