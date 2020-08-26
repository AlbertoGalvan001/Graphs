
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