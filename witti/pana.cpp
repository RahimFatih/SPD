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
    //Dane załadwoane
    //
    int N = 1 << n, *F = new int[N];//Stwórz tablicę w Intów, w której przechowywane będą informajce o najlepszych wynikach dla konkretnych konfiguracji
    //
    //
    F[0] = 0;//ustaw wartosc zerowej permutajci jako 0
    //
    //
    //
    for (int set = 1; set < N; set++)//powtarzaj dla wszystkich możliwych permutacji SET jest maską bitową
    {
        int c = 0;
        for (int i = 0,b=1; i < n; i++,b*=2)//powtarzaj dla wszystkich procesow
            if (set & b)
                c += P[i];

        F[set] = 9999999;
        for (int k = 0, b = 1; k < n; k++, b *= 2)
            if (set & b)
            {
                //cout<<"Fset: "<<F[set]<<endl;
                //cout<<"Fset-b: "<<F[set-b]<<endl;
                //cout<<"Wk: "<< W[k]<<endl;
                //cout<<"c: "<<c<<endl;
                //cout<<"Dk: "<<D[k]<<endl;
                //cin.get();

                if (F[set]>F[set - b] + W[k] * max(c - D[k], 0))
                {
                    F[set]=F[set - b] + W[k] * max(c - D[k], 0);
                }
            }
    }
    //cout << F[N - 1] << endl;
    delete[] F;
    cin.get();
    return 0;
}