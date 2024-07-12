from queue import PriorityQueue

def astar(root):
    pq = PriorityQueue()
    pq.put(root)
    mkd = {root}
    while 1:
        if not pq:
            print('fail to find')
            break
        cur = pq.get()
        if cur.m == cur.leaf:
            break
        for i in cur.childs():
            if i not in mkd:
                pq.put(i)
                mkd.add(i)
    return mkd,cur
