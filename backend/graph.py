class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[to_node].append((from_node, cost))

    def prim_mst(self):
        import heapq
        mst = []
        visited = set()
        min_heap = [(0, next(iter(self.edges)))]  # Start from any node

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            mst.append((node, cost))

            for neighbor, weight in self.edges.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

        return mst[1:]  # Exclude the starting node

