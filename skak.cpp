#include <iostream>

using namespace std;

int main()
{
    int x1{ 0 }, y1{ 0 }, x2{ 0 }, y2{ 2 }, moves{ 0 };

    cin >> x1 >> y1;

    cin >> x2 >> y2;

    if (x1 != x2)
    {
        moves++;
    }

    if (y1 != y2)
    {
        moves++;
    }

    cout << moves;

    return 0;
}
