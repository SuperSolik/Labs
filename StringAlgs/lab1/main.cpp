#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cassert>

std::vector<int> compute_prefix_function(const std::string& s) {
    int len = s.length();
    std::vector<int> p(len);
    p[0] = 0;
    int k = 0;
    for (int i = 1; i < len; ++i) {
        while ((k > 0) && (s[k] != s[i]))
            k = p[k - 1];
        if (s[k] == s[i])
            ++k;
        p[i] = k;
    }
    return p;
}

std::string kmp(const std::string& p, const std::string& s){
    std::string res;
    if(p == s){
        res += "0";
        return res;
    }
    auto pf = compute_prefix_function(p);
    for (int k = 0, i = 0; i < s.size(); i++){
        while ((k > 0) && (p[k] != s[i]))
            k = pf[k-1];
        if (p[k] == s[i])
            k++;
        if (k == p.size()) {
            res += (std::to_string(i - p.size() + 1)) + ",";
        }
    }
    if(res.size() > 0) res.erase(res.end()-1); //erasing last ','
    if(res.empty()) res += "-1";
    return res;
}

void test(){
    assert(kmp("a", "aaa") == "0,1,2");
    std::cout << "TEST#1 OK" << std::endl;
    assert(kmp("test", "test") == "0");
    std::cout << "TEST#2 OK" << std::endl;
    assert(kmp("a", "bbb") == "-1");
    std::cout << "TEST#3 OK" << std::endl;
    assert(kmp("asd", "") == "-1");
    std::cout << "TEST#4 OK" << std::endl;
    assert(kmp("BCA", "ABCDABCAABCAD") == "5,9");
    std::cout << "TEST#5 OK" << std::endl;
}

int main(){
    test();
    std::cout << "ALL OK" << std::endl;
    return 0;
}