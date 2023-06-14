from idlelib.tree import TreeNode
from typing import Optional, List


class Trees:
    def binarySearch(self, root: Optional[TreeNode]) ->List[int]:

        ans= []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root=stack.pop()
            ans.append(root.val)
            root=root.right

        return  ans