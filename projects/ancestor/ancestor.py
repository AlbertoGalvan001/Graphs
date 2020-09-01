# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

# ```
# Example input
#   6

#   1 3
#   2 3
#   3 6
#   5 6
#   5 7
#   4 5
#   4 8
#   8 9
#   11 8
#   10 1
# Example output
#   10
# ```

# Clarifications:
# * The input will not be empty.
# * There are no cycles in the input.
# * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# * IDs will always be positive integers.
# * A parent may have any number of children.


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)                 


def earliest_ancestor(ancestors, starting_node):
    paths = [starting_node]
    final_paths = []
    largest_paths = []
    ancestor_graph = {}
    ancestor_stack = Stack()

    ancestor_stack.push(paths)

    for parent_child in ancestors:
        if parent_child[1] in ancestor_graph:
            ancestor_graph[parent_child[1]].add(parent_child[0])
        else:
            ancestor_graph[parent_child[1]] = {parent_child[0]} 

    while ancestor_stack.size():
        current_path = ancestor_stack.pop()  
        current_node = current_path[-1]     

        if current_node not in ancestor_graph:
            final_paths.append(current_path)

        else:
            neighbors = ancestor_graph[current_node]
            for neighbor in neighbors:
                new_path = current_path[:] 
                new_path.append(neighbor)
                ancestor_stack.push(new_path)    

    if len(final_paths[0]) == 1:
        return -1

    for path in final_paths:
        if len(largest_paths) == 0:
            largest_paths.append(path) 
        else:
            if len(path) > len(largest_paths[0]):
                largest_paths = []
                largest_paths.append(path) 

            elif len(path) == len(largest_paths[0]):
                largest_paths.append(path)   

    min_value = largest_paths[0][-1]

    for path in largest_paths:
        if path[-1] < min_value:
            min_value = path[-1] 

    return min_value                                       