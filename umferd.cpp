#include <iostream>

using namespace std;

int main()
{
    double cells{ 0 }, lanes{ 0 };

    cin >> cells;
    cin >> lanes;

    double total = cells * lanes;

    double empty{ 0 };

    char check;

    for (int i = 0; i < total; ++i)
    {
        cin >> check;

        if (check == '.')
        {
            empty++;
        }
    }

    double result = empty / total;

    cout << result;

    return 0;
}
