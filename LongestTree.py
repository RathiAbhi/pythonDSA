from collections import defaultdict, deque

def findLargestTreeRoot(forest):
    # Step 1: Find root nodes
    all_nodes = set()
    children = set()
    for child, parent in forest.items():
        all_nodes.add(parent)
        all_nodes.add(child)
        children.add(child)
    root_nodes = all_nodes - children  # Nodes that are not children are roots

    # Step 2: Create adjacency list
    adjacency_list = defaultdict(list)
    for child, parent in forest.items():
        adjacency_list[parent].append(child)

    # Step 3: BFS to count nodes in each tree
    def bfs_count_nodes(root):
        visited = set()
        queue = deque([root])
        count = 0
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                count += 1
                queue.extend(adjacency_list[node])
        return count

    # Step 4: Find the largest tree root
    max_count = -1
    largest_root = None
    for root in root_nodes:
        node_count = bfs_count_nodes(root)
        if node_count > max_count or (node_count == max_count and root < largest_root):
            max_count = node_count
            largest_root = root

    return largest_root

# Example Input
forest = {1: 2, 3: 4}
print(findLargestTreeRoot(forest))  # Output: 2