#include <string.h>
#include <iostream>

using std::string;
using std::cout;

bool is_permutation(const string& s1, const string& s2){
    if(s1.size() != s2.size()) 
        return false;

    int arr[128] = {0};
    for(int i = 0; i < s1.size(); ++i){
        arr[(int)s1[i]]++;
    }
    for(int i = 0; i < s2.size(); ++i){
        arr[(int)s2[i]]--;
        if( arr[(int)s2[i]] < 0){
            return false;
        }
    }
    for(int i = 0; i < 128; ++i){
        if(arr[i] != 0)
            return false;
    }
    return true;
}

int main(void){
    string s1 = "Btian", s2 = "Brain";
    if(is_permutation(s1, s2)){
        cout << "yay" << '\n';
    } else {
        cout << "oh no!" << '\n';
    }

    return 0;
}