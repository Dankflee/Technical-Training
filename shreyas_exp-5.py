class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)

        if u_parent == v_parent:
            return False
        
        if self.rank[u_parent] < self.rank[v_parent]:
            self.parent[u_parent] = v_parent
        elif self.rank[u_parent] > self.rank[v_parent]:
            self.parent[v_parent] = u_parent
        else:
            self.parent[v_parent] = u_parent
            self.rank[u_parent] += 1

        return True

def kruskal(edges, n):
    edges.sort(key=lambda x: (x[2], x[0], x[1]))  # Sort edges by weight, then by node u, then by node v
    disjoint_set = DisjointSet(n)
    min_weight = 0

    for edge in edges:
        u, v, wt = edge
        if disjoint_set.union(u, v):
            min_weight += wt

    return min_weight

# Example usage:
edges = [
    (1, 2, 2),
    (2, 3, 3),
    (3, 1, 5)
]
n = 3  # Number of nodes in the graph

min_weight = kruskal(edges, n)
print("Overall weight of the Really Special SubTree:", min_weight)
