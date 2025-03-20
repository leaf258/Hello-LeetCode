

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# 前序遍历: 访问优先级：根节点 -> 左子树 -> 右子树
# 中序遍历: 访问优先级：左子树 -> 根节点 -> 右子树
# 后序遍历: 访问优先级：左子树 -> 右子树 -> 根节点

class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        self._tree = list[arr]

    def size(self):
        return len(self._tree)
    
    def val(self, i : int) -> int | None:
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]
    
    def left(self, i : int) -> int | None:
        return 2*i+1
    
    def right(self, i: int) -> int | None:
        return 2*i+2
    
    def parent(self, i: int) -> int | None:
        return (i-1)//2