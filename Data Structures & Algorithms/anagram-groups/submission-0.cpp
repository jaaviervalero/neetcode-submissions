class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (string word : strs){
            string sorted = word;
            sort(sorted.begin(), sorted.end());
            m[sorted].push_back(word);
        }

        vector<vector<string>> sol;
        for (auto& par : m){
            sol.push_back(par.second);
        }
        return sol;
    }
};
