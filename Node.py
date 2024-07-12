class Node:
    
    leaf = [1,2,3,4,5,6,7,8,0]
    
    def __init__(self, m, parent = -1, depth = 0):
        self.m = m[:]
        self.parent = parent
        self.depth = depth

    def __ne__(self,other):
        return self.m != other.m

    def __eq__(self,other):
        return self.m == other.m

    def __hash__(self):
        return hash(tuple(self.m))

    def __lt__(self,other):
        return self.F() < other.F()
    
    def F(self):
        f = self.G() + self.H()
        return f

    def G(self):
        return self.depth

    def H(self):
        h = 0
        m = self.m[:]
        for i in range(9):
            if m[i] != 0:                
                y1,x1 = divmod(i,3)
                y2,x2 = divmod(m[i] - 1, 3)
                h += abs(y1 - y2) + abs(x1 - x2)
        return h                

    def childs(self):
        res = []
        dxy = [-3,1,3,-1]
        wall = [[0,1,2],[2,5,8],[6,7,8],[0,3,6]]
        for i in range(9):
            if self.m[i] != 0:
                continue            
            for j in [i + dxy[j] for j in range(4) if i not in wall[j]]:            
                if self.m[j] == 0:
                    continue
                mClone = self.m[:]
                mClone[i],mClone[j] = mClone[j],mClone[i]
                res.append(Node(mClone, self, self.depth + 1))
        return res

    def printNode(self):
        print('depth :',self.depth)
        m = self.m
        print(m[:3])
        print(m[3:6])
        print(m[6:])
        print()
        
