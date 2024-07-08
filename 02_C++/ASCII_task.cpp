
#include<iostream>

int main()
{
        std::cout << "Enter the character :- " << std::endl;
        char c;
        std::cin >> c;
        std::cout << "ASCII value of the entered character is: " << static_cast<int>(c) << std::endl;
        
    return 0 ;
}


/* 
#include<iostream>
using namespace std;
 
int main()
{
   char a;
    int i;
    cout<< "DEC" << "\t" << "char"<<endl ;
    cout<< "----------------------"<<endl ;
    for (int i=33; i<=126; i++){
                a=i;
    cout << i << "\t" << a << " " <<endl;
    } 
return 0;
}
*/



/*

#include <iostream>
#include <iomanip>
int main(){


        std::cout << "ASCII" << std::endl;
         std::cout << "----------------------" << std::endl;
        std::cout << std::setw(10) << "DEC" << std::setw(10) << "CHAR" << std::endl;
        std::cout << "----------------------" << std::endl;

        for (int i = 0; i<127; ++i) {
                std::cout << std::setw(10) << i << std::setw(10) << static_cast<char>(i) << std::endl;
              
        }

    return 0;
}

*/


