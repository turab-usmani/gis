import random

MAX_LEVEL = 4  # height of the skip list
P = 0.5         # probability for random level generation

# function to create a node as a dictionary with x, y, and name
def create_node(x, y, name, level):
    return {
        "x": x,
        "y": y,
        "name": name,
        "forward": [None] * (level + 1)
    }

# function to generate a random level
def random_level():
    level = 0
    while random.random() < P and level < MAX_LEVEL:
        level += 1
    return level

# insert function
def insert(skiplist, x, y, name):
    update = [None] * (MAX_LEVEL + 1)
    current = skiplist["header"]


    for i in reversed(range(skiplist["level"] + 1)):
        while current["forward"][i] and (current["forward"][i]["x"] < x or 
                                         (current["forward"][i]["x"] == x and current["forward"][i]["y"] < y)):
            current = current["forward"][i]
        update[i] = current


    current = current["forward"][0]

    # if node on a coordinate exists give msg
    if current and current["x"] == x and current["y"] == y:
        print(f"Cannot insert {name}, Node with coordinates ({x}, {y}) already exists. Name: {current['name']}")
        return -1

    # if node does not exist, insert it
    rlevel = random_level()
    if rlevel > skiplist["level"]:
        for i in range(skiplist["level"] + 1, rlevel + 1):
            update[i] = skiplist["header"]
        skiplist["level"] = rlevel

    new_node = create_node(x, y, name, rlevel)
    for i in range(rlevel + 1):
        new_node["forward"][i] = update[i]["forward"][i]
        update[i]["forward"][i] = new_node

    print(f"Inserted node with coordinates ({x}, {y}) and name: {name}")


# Search function 
def search(skiplist, x, y):
    current = skiplist["header"]
    for i in reversed(range(skiplist["level"] + 1)):
        while current["forward"][i] and (current["forward"][i]["x"] < x or
                                         (current["forward"][i]["x"] == x and current["forward"][i]["y"] < y)):
            current = current["forward"][i]
    current = current["forward"][0]
    if current and current["x"] == x and current["y"] == y:
        return current["name"]
    return None

# Display function  skip lists
def display(skiplist):
    print("Skip List:")
    for i in range(skiplist["level"] + 1):
        print(f"Level {i}:", end=" ")
        node = skiplist["header"]["forward"][i]
        while node:
            print(f"({node['x']}, {node['y']}, {node['name']})", end=" -> ")
            node = node["forward"][i]
        print("None")

# Initialize skip list
def initialize_skiplist():
    return {
        "header": create_node(None, None, None, MAX_LEVEL),  # Header node
        "level": 0
    }
