from pyvis.network import Network


def get_connections(f: str) -> dict:
    connections = {}
    with open(f) as ifile:
        for line in ifile:
            conn = line.strip().split(':')
            key = conn[0].strip()
            conn = conn[1].split()
            if key not in connections:
                connections[key] = set([c.strip() for c in conn])
            else:
                other_connections = connections[key]
                for c in conn:
                    other_connections.add(c)
                connections[key] = other_connections
            for c in connections[key]:
                other_connections = connections.get(c, set())
                other_connections.add(key)
                connections[c] = other_connections

    return connections


def visit(connections: dict, visited: set, parent: str):
    visited.add(parent)
    for adjacent in connections[parent]:
        if adjacent in visited:
            continue
        visited.add(adjacent)
        visit(connections, visited, adjacent)
    return len(visited)


def calculate(connections: dict):
    cuts = [("vkp", "kfr"), ("vnm", "qpp"), ("rhk", "bff")]
    for cut in cuts:
        connections[cut[0]].remove(cut[1])
        connections[cut[1]].remove(cut[0])
    left = visit(connections, set(), cuts[0][0])
    right = visit(connections, set(), cuts[0][1])
    return right * left


def plot(output: str, graph: dict):
    net = Network()
    for node, connections in graph.items():
        net.add_node(node, label=node)
        for connection in connections:
            net.add_node(connection, label=connection)
            net.add_edge(node, connection)
    net.toggle_physics(True)
    net.show(output)


graph = get_connections("day_25.txt")
# plot("25.html", graph)
print(calculate(graph))
