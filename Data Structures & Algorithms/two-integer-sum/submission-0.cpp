class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for(int i =0; i < nums.size(); i++){
            int pair = target - nums[i];
            if (m.count(pair)){
                return {m[pair], i};
            }
            m.insert({nums[i], i });
        }
    }
};
