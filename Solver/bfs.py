def bfs(root):
    que = [root]
    mkd = {root}
    while 1:
        if not que:
            print('fail to find')
            break
        cur = que.pop(0)
        if cur.m == cur.leaf:
            break
        for i in cur.childs():
            if i not in mkd:          
                que.append(i)
                mkd.add(i)
    return mkd,cur
