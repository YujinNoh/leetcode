# version 1
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        visited = []
        results = []
        def dfs(self, node):
            if (not node.left) and (not node.right):
                results.append(node.val)

            if node not in visited:
                visited.append(node)
                if node.left:
                    node.left.val += node.val
                    dfs(self, node.left)
                if node.right:
                    node.right.val += node.val
                    dfs(self, node.right)
        if not root:
            return False
        else:        
            dfs(self, root)
            return targetSum in results
          
# version 2
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if (not root.left) and (not root.right) and targetSum - root.val == 0:
            result = True
        else:
            result = False
        
        return result or self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
