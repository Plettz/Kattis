#include <iostream>
#include <string>

using namespace std;

int main()
{
    int letters{ 0 };
    string input;

    cin >> input;

    for (int i = 0; i < input.size(); ++i)
    {
        if (isalpha(input[i]))
        {
            letters++;
        }
    }

    cout << letters;

    return 0;
}
