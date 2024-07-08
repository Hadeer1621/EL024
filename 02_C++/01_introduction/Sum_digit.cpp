// summation the digits of integer entered by user

# include<iostream>

int main(){
    // taking integer input from user
std::cout << "Enter an integer: ";
int number , remainder ;
int sum = 0;
std::cin >> number;
while(number!= 0){ // loop over digits and increment number until is reached zero 
remainder = number % 10; // remainder the number of digits to take last digit
sum += remainder ;      // then  sum the remainder 
number = number / 10 ; // divide the number by 10 
}
// print the sum and the last digit of the number
std::cout << "Sum of digits: " << sum << std::endl;
return 0; // return
}