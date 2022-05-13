# 2606
# PR 220513 JAEMIN
# AUTH 220512 JAEMIN

vertex_cnt = int(input())
edge_cnt = int(input())

# [1, 2, 3, 4, 5, 6, 7]
vertex_list = list(range(1,vertex_cnt+1))

# [(1, 2), (2, 3), (1, 5), (5, 2), (5, 6), (4, 7)]
edge_list = [tuple(map(int,(input().split(" ")))) for _ in range(edge_cnt)]


# [[], [2, 9], [1, 3], [2, 4], [3], [6], [5], [8], [7, 9], [8, 1], []]
adjacency_list = [[] for _ in vertex_list]
adjacency_list.append([])

for edge in edge_list:
    adjacency_list[edge[0]].append(edge[1])
    adjacency_list[edge[1]].append(edge[0])

stack = [1]
visited_vertex = list()

while stack:
    current = stack.pop()
    for neighbor in adjacency_list[current]:
        if not neighbor in visited_vertex:
            stack.append(neighbor)
    visited_vertex.append(current)
print(len(set(visited_vertex))-1)
