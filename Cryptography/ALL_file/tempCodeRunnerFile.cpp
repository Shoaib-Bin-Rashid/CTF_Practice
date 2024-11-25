#include <iostream>
#include <cmath>

using namespace std;

double f(double x)
{
    return sin(x);
}

double trapezoidal_rule(double a, double b, int n)
{
    double h = (b - a) / n;
    double integral = 0.0;

    cout << "Trapezoidal Rule:\n";
    cout << "h = " << h << endl;

    integral += f(a) / 2.0;
    cout << "f(a)/2 = " << f(a) / 2.0 << endl;

    for (int i = 1; i < n; ++i)
    {
        double x_i = a + i * h;
        integral += f(x_i);
        cout << "f(x_" << i << ") = " << f(x_i) << endl;
    }

    integral += f(b) / 2.0;
    cout << "f(b)/2 = " << f(b) / 2.0 << endl;

    return integral * h;
}

double simpsons_rule(double a, double b, int n)
{
    double h = (b - a) / n;
    double integral = 0.0;

    cout << "\nSimpson's Rule:\n";
    cout << "h = " << h << endl;

    integral += f(a);
    cout << "f(a) = " << f(a) << endl;

    for (int i = 1; i < n; i += 2)
    {
        integral += 4 * f(a + i * h);
        cout << "4 * f(x_" << i << ") = " << 4 * f(a + i * h) << endl;
    }

    for (int i = 2; i < n - 1; i += 2)
    {
        integral += 2 * f(a + i * h);
        cout << "2 * f(x_" << i << ") = " << 2 * f(a + i * h) << endl;
    }

    integral += f(b);
    cout << "f(b) = " << f(b) << endl;

    return integral * h / 3.0;
}

int main()
{
    double a, b;
    int n;
    cout << "Enter lower limit 1: ";
    cin >> a;
    cout << "Enter lower limit 2: ";
    cin >> b;
    cout << "Enter interval n: ";
    cin >> n;

    double trapezoidal_result = trapezoidal_rule(a, b, n);
    cout << "\nFinal approximation using Trapezoidal Rule: " << trapezoidal_result << endl;

    double simpsons_result = simpsons_rule(a, b, n);
    cout << "\nFinal approximation using Simpson's Rule: " << simpsons_result << endl;

    return 0;
}