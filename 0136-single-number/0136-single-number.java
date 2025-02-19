class Solution {
    public int singleNumber(int[] nums) {
        ArrayList<Integer> track = new ArrayList<>();
        int left = 0;
        int nonRepeat = nums[0];
        for(int i:nums){
            if(track.contains(i)){
                track.remove(Integer.valueOf(i));
            }
            else{
                track.add(i);
            }
        }
        return track.get(0);

    }
}