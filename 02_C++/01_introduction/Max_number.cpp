#include<iostream>



int main() {
std::cout << "Enter the three number"<<std::endl;
int num1, num2, num3;
std::cin >> num1 >> num2 >> num3;

if(num1 > num2 && num1 > num3) {
    std::cout << "The largest number is: " << num1 << std::endl;
} 
else if(num2 > num1 && num2 > num3) {
    std::cout << "The largest number is: " << num2 << std::endl;
}
else {
    std::cout << "The largest number is: " << num3 << std::endl;
}

    return 0;
}