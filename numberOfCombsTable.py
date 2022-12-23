from tabulate import tabulate
from heapq import heappush, heappop

class WaterAStar:

    visited, nodesTraversed = set(), 0

    class Jug:
        def __init__(self, cap):
            self.capacity, self.volume = cap, 0
        
        def empty_or_fill(self, should_empty):
            self.volume = 0 if should_empty else self.capacity
            WaterAStar.addState(WaterAStar.jugs, 0)
    
    @staticmethod
    def transfer(a, b):
        transfer_amount = min(a.volume, b.capacity - b.volume)
        a.volume -= transfer_amount
        b.volume += transfer_amount
        WaterAStar.addState(WaterAStar.jugs, 0)

    @staticmethod
    def addState(jugs, cost):
        volumes = tuple(j.volume for j in jugs)
        if volumes not in WaterAStar.visited:
            heappush(WaterAStar.queue, (cost + sum(volumes), volumes))
        
        for jug, initial_volume in zip(WaterAStar.jugs, WaterAStar.initial_volumes):
            jug.volume = initial_volume
      
    @staticmethod
    def main(args):
        WaterAStar.visited.clear()
        WaterAStar.nodesTraversed = 0
        WaterAStar.queue = []

        WaterAStar.jugs = [WaterAStar.Jug(cap) for cap in args]
        WaterAStar.initial_volumes = (0 for _ in args)
        
        volumes = tuple(WaterAStar.initial_volumes)
        heappush(WaterAStar.queue, (0, volumes))

        while WaterAStar.queue:
            _, volumes = heappop(WaterAStar.queue)
            if volumes not in WaterAStar.visited:
                WaterAStar.visited.add(volumes)
                WaterAStar.nodesTraversed += 1
                for jug, volume in zip(WaterAStar.jugs, volumes):
                    jug.volume = volume
                WaterAStar.initial_volumes = [j.volume for j in WaterAStar.jugs]

                for jug in WaterAStar.jugs:
                    jug.empty_or_fill(False)
                    jug.empty_or_fill(True)
    
                for jug1 in WaterAStar.jugs:
                    for jug2 in WaterAStar.jugs:
                        if jug1 != jug2:
                            WaterAStar.transfer(jug1, jug2) 
                          
        return WaterAStar.nodesTraversed

if __name__ == "__main__":

    capacities = []
  
    while True:
        cap = int(input("Enter the capacity of a jug (0 to stop): "))
        if cap == 0:
            break
        capacities.append(cap)

    Aval = [i for i in range(capacities[0]+1)]
    Bval = [i for i in range(capacities[1]+1)]

    print(tabulate([[WaterAStar.main([a, b] + capacities[2:]) for a in Aval] for b in Bval], headers=Aval, tablefmt="fancy_grid", showindex="always"))
