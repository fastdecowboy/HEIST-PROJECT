from collections import deque

from assets.player import current_room
from assets.map import *

def fbs(rooms, origin, target):
    if origin == target:
        return origin
    if target not in rooms | origin not in rooms:
        return None
    queue = deque([origin])
    visited = set(origin)
    parent = {origin: None}
    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for direction, neighbor in rooms[current]["exits"].items():
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None

def new_police(current_room):
    path = fbs(rooms, room_lobby, current_room)
    if path is not None:
        return {"current": path.pop(0),"path": path}

def police_movement(all_police):
    new_police = []
    for police in all_police:
        if len(police["path"]) > 1:
            police["current"] = police["path"].pop(0)
        else:
            police["current"] = police["path"].pop(0)
            police["path"] = fbs(rooms, police["current"], current_room)
        new_police.append(police)
        
    return new_police
    