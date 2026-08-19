class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        vector<vector<int>> v (nums.size() + 1);
        vector<int> resultado;
        for (int& n : nums){
            m[n]++;
        }

        for(auto [num, freq] : m){
            v[freq].push_back(num);
        }

        for (int i =v.size() -1 ; i >= 0; i--){
            for (int num : v[i]){
                resultado.push_back(num);
                if (resultado.size() == k){
                    return resultado;
                }
            }
            
        }
        return {};
    }
};
