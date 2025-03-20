from os import name
from typing import List, Optional


class ListNode: # """链表节点类"""
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def cross_link(self, headA:ListNode, headB:ListNode) -> Optional[ListNode]:
        # Optional[ListNode] 是一个类型提示（type hint），它表示一个变量可以是 ListNode 类型的实例，或者是 None。
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            # if p:
            #     p = p.next
            # else:
            #     p = headB
            # 如果p是真值（在Python中，非空对象、非零数字、非空字符串等都被视为真值），则表达式的结果为p.next，并且这个结果被赋值给p，即p被更新为其下一个节点。如果p是假值（例如，None或空对象），则表达式的结果为headB，这个结果被赋值给p，即p被更新为headB。
            q = q.next if q else headA
        return p

def listTolink(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head

    # for i, value in enumerate(lst): # 错误，列表第一项被处理的2次，导致链表错误
    #     current.next = ListNode(value)
    #     current = current.next
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head  # 在链表构建过程中，head 是链表的起始节点，而 current 是一个用于遍历和构建链表的临时指针。所以应该返回head

if __name__ == "__main__":
    a = Solution()
    listA = [1,9,1,2,4]
    headA = listTolink(listA)

    # listB = [3,2,4]  # 错误：新建立的链表中，2对应的是一个新地址，无法与链表headA相交
    # headB = listTolink(listB)

    # 找到链表A中的节点2（第四个节点）
    current = headA 
    for _ in range(3): # 移动三次到达节点2
        current = current.next # current 最终指向链表A的节点2
    
    headB = ListNode(3)
    headB.next = current # 链表B的第二个节点直接复用链表A的节点2

    result = a.cross_link(headA=headA, headB=headB)

    print(result.val) if result else print("No intersection")
    # if result:
    #     print(result.val)
    # else:
    #     print("No intersection")

            
# 模块是被导入的，而脚本是直接运行的。
# 比如，假设我有一个文件叫mymodule.py，里面定义了一些函数，比如add(a, b)，然后在文件最后写了if __name__ == "__main__":，下面调用了add(2,3)并打印结果。这样的话，当直接运行这个文件的时候，会执行这个测试代码。但如果其他文件导入这个mymodule的时候，这个测试代码就不会被执行。