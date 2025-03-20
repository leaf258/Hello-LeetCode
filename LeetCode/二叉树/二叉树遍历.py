from collections import deque


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历（广度优先）
def level_order(root:TreeNode|None):
    res = []
    # collections模块提供的双端队列deque(),时间复杂度 ​O(1)
    queue = deque() # 高效双端队列，适合频繁头部/尾部操作
    queue.append(root)
    while queue:
        node = queue.popleft() # 此时queue已经更新为popleft()后的队列
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    # # 用列表实现双端队列，时间复杂度O(n)：列表的pop(0)或insert(0, x)操作需要移动所有后续元素
    # queue = [root]
    # while queue:
    #     node = queue.pop(0) # pop()为栈操作，先进后出；pop(0)为队列操作，先进先出
    #     # # 此时queue已经更新为pop(0)后的队列
    #     res.append(node.val)
    #     if node.left:
    #         queue.append(node.left)
    #     if node.right:
    #         queue.append(node.right)

    return res

# 深度优先遍历（前序、中序、后续）
def pre_order(root : TreeNode|None, res:list):
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left, res=res)
    pre_order(root=root.right, res=res)
    return res
def in_order(root:TreeNode|None, res:list):
    # res = [] # 这样是错的，相当于每次递归res都会清空
    if root is None:
        return 
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left, res=res)
    res.append(root.val)
    in_order(root=root.right, res=res)
    return res
def post_order(root:TreeNode|None, res:list):
    # res = [] # 这样是错的，相当于每次递归res都会清空
    if root is None:
        return 
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left, res=res)
    post_order(root=root.right, res=res)
    res.append(root.val)
    return res



def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5)))
    print(level_order(root))
    res = []
    print(pre_order(root, res))
    print(in_order(root, res = []))
    print(post_order(root, res = []))

if __name__ == "__main__":
    main()