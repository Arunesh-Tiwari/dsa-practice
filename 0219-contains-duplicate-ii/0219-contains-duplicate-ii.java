class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int n = nums.length;

        HashMap<Integer, Integer> indexMap = new HashMap();

        for (int i = 0; i<n; i++){
            int curNum = nums[i];

            if (indexMap.containsKey(curNum)){
                if (i - indexMap.get(curNum) <= k)
                return true;
            }

            indexMap.put(curNum,i);
        }
        return false;
    }
}