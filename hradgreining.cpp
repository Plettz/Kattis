#include <iostream>
#include <string>

using namespace std;

int main()
{
    string dna;

    cin >> dna;

    bool found{ false };

    for (int i = 0; i < dna.length(); ++i)
    {
        if (dna[i] == 'C' && dna[i + 1] == 'O' && dna[i + 2] == 'V')
        {
            found = true;
            break;
        }
    }

    if (found)
    {
        cout << "Veikur!" << endl;
    }
    else
    {
        cout << "Ekki veikur!" << endl;
    }

    return 0;
}
