


//  c^2 = a^2 + b^2

#include<iostream>
// Function to check if a triangle is right angle triangle or not

int main() {
    std::cout << "Enter the three sides of the triangle" << std::endl;
    int base , perpendicular , hypotenuse ;
     std::cout <<"Enter the base trangle" << std::endl;
    std::cin>> base ;
     std::cout << "Enter the perpendicular  triangle" << std::endl;
    std::cin>> perpendicular ;
     std::cout << "Enter the thypotenuse the triangle" << std::endl;
    std::cin>> hypotenuse ;

    if ((base*base)+ (perpendicular*perpendicular)== (hypotenuse*hypotenuse) || (hypotenuse*hypotenuse)-(base*base) == (perpendicular*perpendicular) ||  (hypotenuse*hypotenuse) - (perpendicular*perpendicular)== (base*base)){
        std::cout << "The triangle is right  angle triangle" << std::endl;

    }
    else{
        std::cout << "The triangle is not right angle triangle" << std::endl;
    }

    return 0;
}