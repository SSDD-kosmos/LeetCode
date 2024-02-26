# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        counter = 0
        if root is None:
            return counter

        v = [root]
        while v:
            vn = []
            for x in v:
                counter += 1
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
        return counter




