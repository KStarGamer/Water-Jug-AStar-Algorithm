from tabulate import tabulate

class WaterDFS:
    
    visited, nodesTraversed, stack = [], 0, []

    class Node:
        def __init__(self, a, b, c, d):
            self.a, self.b, self.c, self.d = a, b, c, d
            
        def toList(self):
            return [self.a, self.b, self.c, self.d]
    
    class jug:
        def __init__(self, cap):
            self.capacity, self.volume = cap, 0
        
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
        formatted = [node.a, node.b, node.c, node.d]
        if formatted not in WaterDFS.visited and node not in WaterDFS.stack:
            WaterDFS.stack.append(node)
        
        WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume = WaterDFS.initA, WaterDFS.initB, WaterDFS.initC, WaterDFS.initD
      
    @staticmethod
    def main(args):
        capA, capB, capC, capD = args
        WaterDFS.visited.clear()
        WaterDFS.nodesTraversed = 0
    
        n = WaterDFS.Node(0, 0, 0, 0)
        WaterDFS.stack.append(n)
        WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD = (WaterDFS.jug(cap) for cap in args)
    
        while WaterDFS.stack:
            node = WaterDFS.stack.pop()
            if node.toList() not in WaterDFS.visited:
                WaterDFS.visited.append(node.toList())
                WaterDFS.nodesTraversed += 1
                WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume = node.a, node.b, node.c, node.d
                WaterDFS.initA, WaterDFS.initB, WaterDFS.initC, WaterDFS.initD = WaterDFS.jugA.volume, WaterDFS.jugB.volume, WaterDFS.jugC.volume, WaterDFS.jugD.volume

                for jug in (WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD):
                    jug.empty_or_fill(False)
                    jug.empty_or_fill(True)
    
                for jug1 in (WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD):
                    for jug2 in (WaterDFS.jugA, WaterDFS.jugB, WaterDFS.jugC, WaterDFS.jugD):
                        if jug1 != jug2:
                            WaterDFS.transfer(jug1, jug2)

        return WaterDFS.nodesTraversed

if __name__ == "__main__":
    
    A = int(input("Specify A volume: "))
    B = int(input("Specify B volume: "))
    C = int(input("Specify C volume: "))
    D = int(input("Specify D volume: "))

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
