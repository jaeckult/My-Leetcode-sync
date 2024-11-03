class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        if (s.isEmpty()) {
            return true; 
        }
        for (int i = 0; i < s.length(); i++) {
            String rotated = goal.substring(i) + goal.substring(0, i);
            if (rotated.equals(s)) {
                return true;
            }
        }

        return false;
    }
}
