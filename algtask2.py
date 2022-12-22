def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    stack = [root]
    lst = []
    while stack:
        a = stack.pop()
        if a.left:
            stack.append(a.left)
            lst.append((a.left).val)
        if a.right:
            stack.append(a.right)
            lst.append((a.right).val)

    min_v = 10 ** 6
    lst.append(root.val)
    lst.sort()
    for i in range(1, len(lst)):
        if min_v > abs(lst[i] - lst[i - 1]):
            min_v = abs(lst[i] - lst[i - 1])
    return min_v