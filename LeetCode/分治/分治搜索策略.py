# 给定一个长度为 n 的有序数组 nums ，其中所有元素都是唯一的，请查找元素 target 。
def dfs(nums:list, i:int, j:int, target:int):
    if i > j:
        return
    m = (i+j)//2
    if nums[m] > target:
        return dfs(nums, i, m, target)
    elif nums[m] < target:
        return dfs(nums, m, j, target)
    else:
        return m
    
# 给定一棵二叉树的前序遍历 preorder 和中序遍历 inorder ，请从中构建二叉树，返回二叉树的根节点。假设二叉树中没有值重复的节点（如图 12-5 所示）。
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
        
def tree_dfs(preorder:list, inorder_map:dict[int, int], i:int, left:int, right:int) -> TreeNode|None:
    if left > right:
        return
    root = TreeNode(preorder[i])
    m = inorder_map[preorder[i]]
    # 左树
    root.left = tree_dfs(preorder, inorder_map, i+1, left, m-1)
    # 右树
    root.right = tree_dfs(preorder, inorder_map, i+1+(m-left), m+1, right)
    return root

def buildtree(preorder:list, inorder:list) -> TreeNode|None:
    inorder_map = {val : i for i ,val in enumerate(inorder)}
    root = tree_dfs(preorder, inorder_map, i = 0, left = 0, right = len(inorder)-1)
    return root


    
def main():
    nums = [1,3,4,5,6]
    i ,j  = 0, len(nums)-1
    target = nums[3]
    res = dfs(nums=nums, i = i, j = j, target = target)
    print(res)
    a = [1,1,2,3,2]
    print(sorted(a))
    preorder = [3,9,2,1,7]
    inorder = [9,3,1,2,7]
    root = buildtree(preorder, inorder)
    print(root)

if __name__ == "__main__":
    main()