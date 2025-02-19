/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList <Integer> list= new ArrayList<>();
        preorderTraversal1(root, list);
        return list;
    }
    public void preorderTraversal1(TreeNode root, ArrayList <Integer> list){
        if(root == null) return;
        list.add(root.val);
        preorderTraversal1(root.left, list);
        preorderTraversal1(root.right, list);
    }
}