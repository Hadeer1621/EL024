
// multiplication table in c++ 

#include<iostream>


int main () {
    int number ; 
    std::cout << "Enter the number:- "<< std::endl;
    std::cin >> number ;
     std::cout << "----------------------"<< std::endl;
    for(int i = 0; i<=10;++i) {
        std::cout <<number<<" * "<< i << "  = " << number * i << std::endl;
    }

    return 0;
}