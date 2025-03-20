import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
        self.paths = [[] for _ in range(self.V)]

    def printSolution(self,dist):
        print("Vertex \tDistance from Source \tPath")
        for node in range(self.V):
            print(node, "\t", dist[node], "\t\t\t", self.paths[node])

    # A helper function to find the vertex with 
    # the lowest distance value, from the unvisited
    # vertices (ie a vertex whose value in sptSet is 
    # False)
    def minDistance(self, dist, sptSet):
        # Initialize minimum distance as a practically
        # infinitive value
        min = sys.maxsize

        # iterate through the range of vertices
        for v in range(self.V): 
            # find the closest vertex that is reachable
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v]
                min_index = v
        # return that index so the program 
        # knows which node to visit
        return min_index 
    
    def dijkstra(self,src):
        # array of distances from the source 
        # to all other nodes, 
        # with values instantiated to a very high value
        dist = [sys.maxsize] * self.V 
        dist[src] = 0 # setting the source nodes distance to itself at 0
        sptSet = [False] * self.V # setting all values to False or unvisited in sptSet
        self.paths[src] = [src] # setting the source nodes path to itself as itself

        for _ in range(self.V): 
            x = self.minDistance(dist, sptSet) # find the nearest node
            sptSet[x] = True # mark that node as visited/processed
            for y in range(self.V):
                # check other nodes to see if:
                # 1. an edge exists between the two vertices
                # 2. the second vertex has not yet been visited
                # 3. the current distance to the y vertex is greater than the 
                # distance to x plus the connection in question (self.graph[x][y])
                # if so, update the distance to y and the paths to y as the shortest path
                if self.graph[x][y] > 0 and not sptSet[y] and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    self.paths[y] = self.paths[x] + [y]
        self.printSolution(dist)

if __name__ == "__main__":
    # Locations in Middle Earth
    locations = [
        "Earth", "Pleiades", "Alpha Centauri", "Vela Molecular ridge", "Rosette Nebula", "Orion Nebula",
        "Canis Major", "Orion"
    ]

    # Create the graph with 11 locations
    g = Graph(8)

    # Assign the adjacency matrix (Middle Earth distances)
    g.graph = [
        [0, 442, 4, 0, 0, 1344, 0, 0],
        [442, 0, 0, 0, 842, 932, 0, 0],
        [4, 0, 0, 437, 0, 0, 0, 0],
        [0, 0, 437, 0, 0, 399, 337, 0],
        [0, 842, 0, 0, 0, 376, 0, 345],
        [1344, 932, 0, 399, 376, 0, 0, 154],
        [0, 0, 0, 337, 0, 0, 0, 221],
        [0, 0, 0, 0, 345, 154, 221, 0]

    ]




    # Step 2: Find shortest path from Earth to Orion
    print("\nRunning Dijkstra from Earth to Orion:")
    g.dijkstra(0)  # This prints the distances
    distance_Earth_to_Orion = g.paths[7]
    total_distance = sum(
        g.graph[distance_Earth_to_Orion[i]][distance_Earth_to_Orion[i+1]]
        for i in range(len(distance_Earth_to_Orion) - 1)
    )


    # Formatting output for paths
    earth_to_Orion_path = " → ".join(locations[i] for i in distance_Earth_to_Orion)

    # Print results
    print("\nShortest Path from Earth to Orion:")
    print(f"The Alien overlords should go: {earth_to_Orion_path} (Distance: {total_distance} lightyears)")


    print("\nTotal Distance the Alien overlords need to travel:", total_distance, "lightyears")


  

"""[0, 131, 0, 0, 0, 0, 481, 0, 0, 0, 0],
        [131, 0, 306, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 306, 0, 178, 362, 0, 0, 0, 0, 0, 0],
        [0, 0, 178, 0, 0, 172, 173, 0, 0, 0, 0],
        [0, 0, 362, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 172, 0, 0, 0, 201, 0, 217, 0],
        [481, 0, 0, 173, 0, 0, 0, 74, 0, 0, 0],
        [0, 0, 0, 0, 0, 201, 174, 0, 315, 262, 0],
        [0, 0, 0, 0, 0, 0, 0, 315, 0, 64, 178],
        [0, 0, 0, 0, 0, 217, 0, 262, 64, 0, 183],
        [0, 0, 0, 0, 0, 0, 0, 0, 178, 83, 0]"""
