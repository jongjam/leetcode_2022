class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // so we get an input vector, which is basically just a dynamic array I am FERMNETING IN HERE
        std::unordered_map<int, int> map;
        std::vector<int> res;

        // for (auto num : nums) {

        // }
        for (size_t i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];

            if (map.find(diff) != map.end()) {
                res.push_back(i);
                res.push_back(map[diff]);
                return res;
            } else {
                map.insert(std::make_pair(nums[i], i));
            }
        }

        return res;
    }
};
