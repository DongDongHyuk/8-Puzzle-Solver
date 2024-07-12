from queue import PriorityQueue

def astar(root):
    pq = PriorityQueue()
    pq.put(root)
    mkd = {root}
    while 1:
        if not que:
            print('fail to find')
            break
        cur = pq.get()
        if cur.m == cur.leaf:
            break
        for i in cur.childs():
            if i not in mkd:
                que.put(i)
                mkd.add(i)
                i.parent = cur
    return mkd,cur
