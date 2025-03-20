
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    # 访问过的节点为Gray，未访问节点为White
    def inorderTraversal(self, root:TreeNode | None) -> list[int]:
        res = []
        White, Gray = 1, 0
        stack = [(White, root)]
        while stack:
            color, node = stack.pop() # stack栈弹出节点
            if node is None:
                continue # 执行continue后，下面的if else 均不执行
            if color is White:
                stack.append([White, node.left])
                stack.append([Gray, node])
                stack.append([White, node.right])
            else:
                res.append(node.value)
        return res
    
    # 中序遍历：递归
    def inorderTraversal_recursion(self, root:TreeNode|None) -> list:
        res = []
        def recursion(node:TreeNode):
            if node is None:
                return 
            else:
                recursion(node.left)
                res.append(node.value)
                recursion(node.right)
        recursion(root)
        return res
    
    # 迭代
    def inorderTraversal_iteration(self, root:TreeNode|None) -> list:
        res = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.value)
            current = current.right
        return res
    
    # Hello算法
    def order(self, root:TreeNode|None) -> list:
        res = []

        # 前序遍历
        def pre_order(root: TreeNode | None):
            if root is None:
                return
            # 访问优先级：根节点 -> 左子树 -> 右子树
            res.append(root.val)
            pre_order(root=root.left)
            pre_order(root=root.right)

        # 中序遍历
        def in_order(node):
            if node is None:
                return  # 当 node 为 None 时，return 会立即结束当前递归层，返回到上一层递归调用 in_order 的位置，继续执行后续代码
            # 访问优先级：左子树 -> 根节点 -> 右子树
            in_order(node = node.left)
            res.append(node.value)
            in_order(node = node.right)

        # 后序遍历
        def post_order(root: TreeNode | None):
            if root is None:
                return
            # 访问优先级：左子树 -> 右子树 -> 根节点
            post_order(root=root.left)
            post_order(root=root.right)
            res.append(root.val)

        in_order(root) # 这里选择中序遍历
        return res
    



    
def test():
    solution = Solution()
    root = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3), right=None))
    reslut = solution.inorderTraversal(root = root)
    reslut.reverse() # reverse() 方法直接修改原列表
    print(reslut) # 返回原列表
    reslut_recursion = solution.inorderTraversal_recursion(root=root)
    print(reslut_recursion)
    reslut_iteartion = solution.inorderTraversal_iteration(root=root)
    print(reslut_iteartion)
    reslut_order = solution.order(root=root)
    print(reslut_order)

if __name__ == "__main__":
    test()