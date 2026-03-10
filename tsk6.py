def build_graph(n, m):
    """
    Builds graph of cities and roads.
    
    Arguments:
        n: number of cities
        m: number of roads
    
    Returns:
        dict: graph as adjacency list
    """
    graph = {}
    
    for i in range(m):
        city1, city2, distance = input().split()
        distance = int(distance)
        
        if city1 in graph:
            graph[city1].append((city2, distance))
        else:
            graph[city1] = [(city2, distance)]
        
        if city2 in graph:
            graph[city2].append((city1, distance))
        else:
            graph[city2] = [(city1, distance)]
    
    return graph


def find_shortest_path(graph, start, end):
    """
    Finds shortest path using Dijkstra's algorithm.
    
    Arguments:
        graph: city graph
        start: starting city
        end: destination city
    
    Returns:
        int: shortest distance
    """
    if start not in graph or end not in graph:
        return -1
    
    distances = {}
    visited = {}
    
    for city in graph:
        distances[city] = 999999 
        visited[city] = False
    
    distances[start] = 0
    
    for i in range(len(graph)):
        # Find unvisited city with minimum distance
        min_distance = 999999
        min_city = None
        
        for city in graph:
            if not visited[city] and distances[city] < min_distance:
                min_distance = distances[city]
                min_city = city
        
        if min_city is None:
            break
        
        visited[min_city] = True
        

        for neighbor, distance in graph[min_city]:
            new_distance = distances[min_city] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    
    return distances[end]


def main():
    """Main function"""
    n = int(input())  
    m = int(input())  
    
    graph = build_graph(n, m)
    
    last_line = input().split()
    city1 = last_line[0]
    city2 = last_line[1]
    
    result = find_shortest_path(graph, city1, city2)
    print(result)


if __name__ == "__main__":
    main()
