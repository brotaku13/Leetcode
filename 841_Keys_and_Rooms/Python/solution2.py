"""
Runtime: 44 ms, faster than 44.03% of Python3 online submissions for Keys and Rooms.
Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Keys and Rooms.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        visited = set(dfs)
        while dfs:
            room = dfs.pop()
            for key in rooms[room]:
                if key not in visited:
                    dfs.append(key)
                    visited.add(key)
                    if len(visited) == len(rooms):
                        return True
                    
        return len(rooms) == len(visited)
                    