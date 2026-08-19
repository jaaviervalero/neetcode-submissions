class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> appeared;
        for (int n = 0; n < nums.size(); n++){
           appeared.insert(nums[n]);
        }

        return !(nums.size() == appeared.size());
        
    }
};