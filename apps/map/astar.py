from heapdict import heapdict
from models import Edge

def euclidian_distance(start, end):
  return start.coordinates.distance(end.coordinates)

def bidirectional_astar(start, goal, edge_f=euclidian_distance, heuristic_f=euclidian_distance):
  # This implementation assumes that edge_f is consistent, meaning that edge_f(v, w) = edge_f(w, v).
  
  
  def _itersearch(start, goal, neighbor_f, explored, parents):
    frontier = heapdict({start: heuristic_f(start, goal)})
    distances = {start: 0}
  
    while frontier:
      node, node_distance = frontier.popitem()
      explored.add(node)
      
      for adj in neighbor_f(node):
        if adj in explored:
          continue
  
        adj_distance = node_distance + edge_f(node, adj)
  
        # Found a better path, so adj's position in the priority queue needs to be updated.
        if adj not in frontier or adj_distance < distances[adj]:
          frontier[adj] = adj_distance + heuristic_f(adj, goal)
          distances[adj] = adj_distance
          parents[adj] = node  

      yield node

  forward_explored = set()
  forward_parents = {}
  forward = _itersearch(
      start,
      goal,
      lambda node: (edge.node_sink for edge in Edge.objects.filter(node_src=node)), 
      forward_explored,
      forward_parents)
  
  reverse_explored = set()
  reverse_parents = {}
  reverse = _itersearch(
      goal,
      start,
      lambda node: (edge.node_src for edge in Edge.objects.filter(node_sink=node)),
      reverse_explored,
      reverse_parents)

  try:
    direction = True 
    while True:
      if direction:
        node = forward.next()
        if node in reverse_explored:
          return reconstruct_path(forward_parents, reverse_parents, start, node, goal)
      else:
        node = reverse.next()
        if node in forward_explored:
          return reconstruct_path(forward_parents, reverse_parents, start, node, goal)
  
      direction = not direction
      
  except StopIteration:
    return []

def reconstruct_path(f_parents, r_parents, start, middle, goal):
  path = [middle]
  
  # Build forward path
  node = middle
  while node != start:
    node = f_parents[node]
    path.insert(0, node)
  
  # Build reverse path
  node = middle 
  while node != goal:
    node = r_parents[node]
    path.append(node)
    
  return path

