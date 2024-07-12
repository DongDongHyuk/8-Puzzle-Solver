from Node import Node
from Solver.bfs import *
from Solver.astar import *


def main():
    
    m = [5, 4, 3,
         6, 0, 7,
         0, 2, 1]

    root = Node(m)
    leaf = Node(m)
    
    Solution = bfs
    mkd = Solution(root)
    print('visited {}Nodes.'.format(len(mkd)))    

if __name__ == '__main__':
    main()


