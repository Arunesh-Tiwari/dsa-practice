class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int n = arrays.size();
        int maxi = arrays.get(0).get(arrays.get(0).size()-1);
        int mini = arrays.get(0).get(0);
        int result = 0;

        for(int i=1; i<n; i++){
            List<Integer> array = arrays.get(i);
            int len = array.size();
            int current_min = array.get(0);
            int current_max = array.get(len-1);

            int distmin = Math.abs(current_min - maxi);
            int distmax = Math.abs(current_max - mini);

            result = Math.max(result, Math.max(distmin, distmax));

            mini = Math.min(mini, current_min);
            maxi = Math.max(maxi, current_max);
        }
        return result;
    }
}