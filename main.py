from Node import Node
from Solver.bfs import *
from Solver.astar import *
from time import time as t


def main():
    
    m = [5, 4, 3,
         6, 0, 7,
         8, 2, 1]

    root = Node(m)    
    Solution = astar

    t1 = t()
    mkd,leaf = Solution(root)
    t2 = t() - t1

    cur = leaf
    path = [leaf]    
    while cur != root:
        cur = cur.parent
        path.append(cur)
    path = path[::-1]
        
    for node in path:
        if Solution == astar:
            f,h,g = node.F(),node.H(),node.G()
            print('F({}) = H({}) + G({})'.format(f,h,g))
        node.printNode()
    print('visited {}nodes.'.format(len(mkd)))
    print('Searched in {}s'.format(round(t2,3)))

if __name__ == '__main__':
    main()


