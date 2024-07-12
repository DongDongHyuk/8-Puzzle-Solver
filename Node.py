class Node:

    leaf = [1,2,3,4,5,6,7,0,0]
    
    def __init__(self,m):
        self.m = m[:]
        self.parent = -1
        self.fix = []

    def __ne__(self,other):
        return self.m != other.m

    def __eq__(self,other):
        return self.m == other.m

    def __hash__(self):
        return hash(tuple(self.m))

    def childs(self):
        res = []
        dxy = [-3,1,3,-1]
        wall = [[0,1,2],[2,5,8],[6,7,8],[0,3,6]]
        for i in range(9):
            if i in self.fix or self.m[i] != 0:
                continue            
            for j in [i + dxy[j] for j in range(4) if i not in wall[j]]:            
                if j in self.fix or self.m[j] == 0:
                    continue
                mClone = self.m[:]
                mClone[i],mClone[j] = mClone[j],mClone[i]
                res.append(Node(mClone))
        return res

    def printNode(self):
        print('Node Informations')
        m = self.m
        print(m[:3])
        print(m[3:6])
        print(m[6:])
        print()
    

        
