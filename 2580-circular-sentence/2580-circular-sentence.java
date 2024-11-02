class Solution {
    public boolean isCircularSentence(String sentence) {
        if (sentence.isEmpty()) {
            return false; 
        }

        String[] words = sentence.trim().split(" ");
        if (words.length == 1) {
            return words[0].charAt(words[0].length() - 1) == words[0].charAt(0); 
        }

        for (int i = 1; i < words.length; i++) {
            if (words[i - 1].charAt(words[i - 1].length() - 1) != words[i].charAt(0)) {
                return false;
            }
        }
        if (words[words.length - 1].charAt(words[words.length - 1].length() - 1) != words[0].charAt(0)) {
            return false;
        }

        return true; 
    }
}

