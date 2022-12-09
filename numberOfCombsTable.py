from tabulate import tabulate

class WaterDFS:
    
    visited =  []
    nodesTraversed = 0
    stack =  []
    jugA = None
    jugB = None
    jugC = None
    jugD = None
    initA = 0
    initB = 0
    initC = 0
    initD = 0
    
    class Node:
        
        a = 0
        b = 0
        c = 0
        d = 0
        
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            
        def toList(self):
            return [self.a, self.b, self.c, self.d]
    
    class jug:
        
        capacity = 0
        volume = 0
        
        def __init__(self, cap):
            self.capacity = cap
            self.volume = 0
        
        def empty(self):
            self.volume = 0
            newNode = WaterDFS.Node(WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume)
            WaterDFS.addState(newNode)
        
        def fill(self):
            self.volume = self.capacity
            newNode = WaterDFS.Node(WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume)
            WaterDFS.addState(newNode)
    
    @staticmethod
    def transfer(a, b):
        
        difference = b.capacity - b.volume
        
        if (a.volume >= difference):
            b.volume = b.capacity
            a.volume -= difference
            newNode = WaterDFS.Node(WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume)
            WaterDFS.addState(newNode)
        else:
            b.volume += a.volume
            a.volume = 0
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
        
        while len(WaterDFS.stack) != 0:
            
            node = WaterDFS.stack.pop()
            formatted = node.toList()
            
            if formatted not in WaterDFS.visited:
                #print(formatted)
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
                
                WaterDFS.jugA.fill()
                WaterDFS.jugB.fill()
                WaterDFS.jugC.fill()
                WaterDFS.jugD.fill()
                
                WaterDFS.jugA.empty()
                WaterDFS.jugB.empty()
                WaterDFS.jugC.empty()
                WaterDFS.jugD.empty()

                WaterDFS.transfer(WaterDFS.jugA, WaterDFS.jugB)
                WaterDFS.transfer(WaterDFS.jugA, WaterDFS.jugC)
                WaterDFS.transfer(WaterDFS.jugB, WaterDFS.jugA)
                WaterDFS.transfer(WaterDFS.jugB, WaterDFS.jugC)
                WaterDFS.transfer(WaterDFS.jugC, WaterDFS.jugA)
                WaterDFS.transfer(WaterDFS.jugC, WaterDFS.jugB)
                
                WaterDFS.transfer(WaterDFS.jugA, WaterDFS.jugD)
                WaterDFS.transfer(WaterDFS.jugC, WaterDFS.jugD)
                WaterDFS.transfer(WaterDFS.jugB, WaterDFS.jugD)
                WaterDFS.transfer(WaterDFS.jugD, WaterDFS.jugB)
                WaterDFS.transfer(WaterDFS.jugD, WaterDFS.jugC)
                WaterDFS.transfer(WaterDFS.jugD, WaterDFS.jugA)

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

    print(tabulate(colmbs, headers=Aval,tablefmt="fancy_grid", showindex="always"))
