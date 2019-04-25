#include <iostream>
#include "funcs.h"

int main(){
    std::string pattern, str;
    std::getline(std::cin, pattern);
    std::getline(std::cin, str);
    auto res = checkCircle(pattern, str);
    std::cout << res << std::endl;
    return 0;
}
