
#include <iostream>
#include <bitset>

using namespace std;

int main() {
    // Input decimal number
    unsigned long decimal;
    cout << "Enter a decimal number: ";
    cin >> decimal;

    // Create a bitset from the decimal number
    bitset<8> bits(decimal) ;


    // Output the binary equivalent as a string
    cout << "Binary equivalent: " << bits.to_string() << endl;

    return 0;
}
