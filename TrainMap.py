from collections import deque

class RailNetwork:
    def __init__(self):
        self.graph = {}

    def add_station(self, station_name):
        if station_name not in self.graph:
            self.graph[station_name] = []

    def add_connection(self, station1, station2):
        self.add_station(station1)
        self.add_station(station2)
        self.graph[station1].append(station2)
        self.graph[station2].append(station1)

    def shortestPath(self, fromStationName, toStationName):
        if fromStationName not in self.graph or toStationName not in self.graph:
            return f"One or both stations not found in the network."
        if fromStationName == toStationName:
            return [fromStationName]

        # BFS setup
        queue = deque([fromStationName])
        visited = set([fromStationName])
        predecessors = {fromStationName: None}

        while queue:
            current_station = queue.popleft()

            # Check neighbors
            for neighbor in self.graph[current_station]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    predecessors[neighbor] = current_station
                    queue.append(neighbor)

                    # Stop BFS when destination is found
                    if neighbor == toStationName:
                        return self._reconstruct_path(predecessors, fromStationName, toStationName)

        return f"No path exists between {fromStationName} and {toStationName}."

    def _reconstruct_path(self, predecessors, start, end):
        path = []
        current = end
        while current:
            path.append(current)
            current = predecessors[current]
        return path[::-1]  # Reverse the path to start from the source

# Example Usage
rail_network = RailNetwork()
rail_network.add_connection("A", "B")
rail_network.add_connection("B", "C")
rail_network.add_connection("A", "D")
rail_network.add_connection("D", "E")
rail_network.add_connection("E", "C")

print(rail_network.shortestPath("A", "C"))  # Output: ['A', 'B', 'C']
print(rail_network.shortestPath("A", "E"))  # Output: ['A', 'D', 'E']
print(rail_network.shortestPath("A", "Z"))  # Output: "One or both stations not found in the network."