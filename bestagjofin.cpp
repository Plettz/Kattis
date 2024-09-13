#include <iostream>

using namespace std;

int main()
{
    int guests{ 0 }, topNum{ 0 }, tempNum{ 0 };

    string topName, tempName;

    cin >> guests;

    for (int i = 0; i < guests; ++i)
    {
        cin >> tempName;
        cin >> tempNum;

        if (topNum < tempNum)
        {
            topName = tempName;
            topNum = tempNum;
        }
    }

    cout << topName;

    return 0;
}
