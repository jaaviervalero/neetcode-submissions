class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> countS;
        map<char, int> countT;

        for (char c : s){
            countS[c]++;
        }
        for (char c : t){
            countT[c]++;
        }
        return countS == countT;
    }
};
