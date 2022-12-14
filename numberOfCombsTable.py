from tabulate import tabulate

class WaterDFS:

    visited, nodesTraversed, stack = [], 0, []

    class Node:
        def __init__(self, *volumes):
            self.volumes = volumes

        def toList(self):
            return self.volumes
    
    class Jug:
        def __init__(self, cap):
            self.capacity, self.volume = cap, 0
        
        def empty_or_fill(self, should_empty):
            self.volume = 0 if should_empty else self.capacity
            newNode = WaterDFS.Node(*[j.volume for j in WaterDFS.jugs])
            WaterDFS.addState(newNode)
    
    @staticmethod
    def transfer(a, b):
        transfer_amount = min(a.volume, b.capacity - b.volume)
        a.volume -= transfer_amount
        b.volume += transfer_amount
        newNode = WaterDFS.Node(*[j.volume for j in WaterDFS.jugs])
        WaterDFS.addState(newNode)

    @staticmethod
    def addState(node):
        formatted = node.toList()
        if formatted not in WaterDFS.visited and node not in WaterDFS.stack:
            WaterDFS.stack.append(node)
        
        for jug, initial_volume in zip(WaterDFS.jugs, WaterDFS.initial_volumes):
            jug.volume = initial_volume
      
    @staticmethod
    def main(args):
        WaterDFS.visited.clear()
        WaterDFS.nodesTraversed = 0

        WaterDFS.jugs = [WaterDFS.Jug(cap) for cap in args]
        WaterDFS.initial_volumes = [0 for _ in args]
        
        n = WaterDFS.Node(*WaterDFS.initial_volumes)
        WaterDFS.stack.append(n)

        while WaterDFS.stack:
            node = WaterDFS.stack.pop()
            if node.toList() not in WaterDFS.visited:
                WaterDFS.visited.append(node.toList())
                WaterDFS.nodesTraversed += 1
                for jug, volume in zip(WaterDFS.jugs, node.volumes):
                    jug.volume = volume
                WaterDFS.initial_volumes = [j.volume for j in WaterDFS.jugs]

                for jug in WaterDFS.jugs:
                    jug.empty_or_fill(False)
                    jug.empty_or_fill(True)
    
                for jug1 in WaterDFS.jugs:
                    for jug2 in WaterDFS.jugs:
                        if jug1 != jug2:
                            WaterDFS.transfer(jug1, jug2)

        return WaterDFS.nodesTraversed

if __name__ == "__main__":

    capacities = []
    while True:
        cap = int(input("Enter the capacity of a jug (0 to stop): "))
        if cap == 0:
            break
        capacities.append(cap)

    Aval = [i for i in range(capacities[0]+1)]
    Bval = [i for i in range(capacities[1]+1)]

    combs, truecombs = [], []

    for i in Bval:
        for j in Aval:
            capacities[0] = j
            capacities[1] = i
            combs.append(WaterDFS.main(capacities))
        truecombs.append(list(combs))
        combs.clear()

    print(tabulate(truecombs, headers=Aval, tablefmt="fancy_grid", showindex="always"))
