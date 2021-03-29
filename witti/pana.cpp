#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int n, P[100], W[100], D[100];
    ifstream f("./data.txt");
    string s;
    while (s != "data.19:")
        f >> s;
    f >> n;
    for (int i = 0; i < n; i++)
        f >> P[i] >> W[i] >> D[i];
    f.close();
    for (int i = 0; i < n; i++)
        cout << P[i] << " " << W[i] << " " << D[i] << endl;
    //
    int N = 1 << n, *F = new int[N];
    F[0] = 0;
    for (int set = 1; set < N; set++)
    {
        int c = 0;
        for (int i = 0, b = 1; i < n; i++)
            if (set & b)
                c += P[i];
        F[set] = 9999999;
        for (int k = 0, b = 1; k < n; k++, b *= 2)
            if (set & b)
            {

                if (F[set]>F[set - b] + W[k] * max(c - D[k], 0))
                {
                    F[set]=F[set - b] + W[k] * max(c - D[k], 0);
                }
            }
    }
    cout << F[N - 1] << endl;
    delete[] F;
    cin.get();
    return 0;
}