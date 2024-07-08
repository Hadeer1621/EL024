
// check the letters is vowel or not

# include<iostream>

int main(){

    char letter;
    bool islowercasevowel , isuppercasevowel ;

    std::cout << "Enter the letters" << std::endl;
    std::cin >> letter;
    islowercasevowel = (letter == 'a' || letter == 'o' || letter == 'i' || letter == 'e' || letter == 'u');
    isuppercasevowel = (letter == 'A' || letter == 'O' || letter == 'I' || letter == 'E' || letter == 'U');
    if(islowercasevowel || isuppercasevowel){
        std::cout << "The entered letter is a vowel" << std::endl;
    }
    else{
        std::cout << "The entered letter is not a vowel" << std::endl;
    }

    return 0;
}