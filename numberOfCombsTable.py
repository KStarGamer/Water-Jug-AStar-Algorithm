from tabulate import tabulate

class WaterDFS:
    
    visited = []
    nodesTraversed = 0
    stack = []

    class Node:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            
        def toList(self):
            return [self.a, self.b, self.c, self.d]
    
    class jug:
        def __init__(self, cap):
            self.capacity = cap
            self.volume = 0
        
        def empty_or_fill(self, should_empty):
            self.volume = 0 if should_empty else self.capacity
            newNode = WaterDFS.Node(WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume)
            WaterDFS.addState(newNode)
    
    @staticmethod
    def transfer(a, b):
        transfer_amount = min(a.volume, b.capacity - b.volume)
        a.volume -= transfer_amount
        b.volume += transfer_amount
        newNode = WaterDFS.Node(WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume)
        WaterDFS.addState(newNode)

    @staticmethod
    def addState(node):
        formatted = node.toList()
        if formatted not in WaterDFS.visited and node not in WaterDFS.stack:
            WaterDFS.stack.append(node)
        
        WaterDFS.jugA.volume = WaterDFS.initA
        WaterDFS.jugB.volume = WaterDFS.initB
        WaterDFS.jugC.volume = WaterDFS.initC
        WaterDFS.jugD.volume = WaterDFS.initD
        
    @staticmethod
    def main(args):
    
        capA = args[0]
        capB = args[1]
        capC = args[2]
        capD = args[3]
        
        WaterDFS.visited.clear()
        WaterDFS.nodesTraversed = 0
        
        n = WaterDFS.Node(0, 0, 0, 0)
        WaterDFS.stack.append(n)
        
        WaterDFS.jugA = WaterDFS.jug(capA)
        WaterDFS.jugB = WaterDFS.jug(capB)
        WaterDFS.jugC = WaterDFS.jug(capC)
        WaterDFS.jugD = WaterDFS.jug(capD)
        
        while WaterDFS.stack:
            
            node = WaterDFS.stack.pop()
            formatted = node.toList()
            
            if formatted not in WaterDFS.visited:
                WaterDFS.visited.append(formatted)
                WaterDFS.nodesTraversed += 1
                
                WaterDFS.jugA.volume = node.a
                WaterDFS.jugB.volume = node.b
                WaterDFS.jugC.volume = node.c
                WaterDFS.jugD.volume = node.d
                
                WaterDFS.initA = WaterDFS.jugA.volume
                WaterDFS.initB = WaterDFS.jugB.volume
                WaterDFS.initC = WaterDFS.jugC.volume
                WaterDFS.initD = WaterDFS.jugD.volume
    
                for jug in (WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD):
                    jug.empty_or_fill(False)
                    jug.empty_or_fill(True)
    
                for jug1 in (WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD):
                    for jug2 in (WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD):
                        if jug1 != jug2:
                            WaterDFS.transfer(jug1, jug2)

        return WaterDFS.nodesTraversed

if __name__ == "__main__":
    
    A = int(input("Specify A target: "))
    B = int(input("Specify B target: "))
    C = int(input("Specify C target: "))
    D = int(input("Specify D target: "))

    Aval = [i for i in range(A+1)]
    Bval = [i for i in range(B+1)]

    #print(WaterDFS.main([A,B,C,D]))

    combs = []
    colmbs = []
    
    for i in Bval:
        for j in Aval:
            combs.append(WaterDFS.main([i,j,C,D]))
        colmbs.append(list(combs))
        combs.clear()

    print(tabulate(colmbs, headers=Aval, tablefmt="fancy_grid", showindex="always"))
