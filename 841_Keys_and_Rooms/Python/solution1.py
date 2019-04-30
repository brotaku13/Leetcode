"""
Runtime: 80 ms, faster than 5.57% of Python3 online submissions for Keys and Rooms.
Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Keys and Rooms.
"""

import queue
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        found_keys = [0] * len(rooms)
        to_visit = queue.Queue()
        to_visit.put(0)
        
        while not to_visit.empty():
            room = to_visit.get()
            found_keys[room] = 1
            for key in rooms[room]:
                if found_keys[key] == 0:
                    to_visit.put(key)
                    
        for k in found_keys:
            if k == 0:
                return False
        return True