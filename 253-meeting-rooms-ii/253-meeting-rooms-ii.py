class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort()
        rooms = []
        for i in intervals: 
            if rooms and rooms[0] <= i[0]:
                heapq.heapreplace(rooms, i[-1])
            else:
                heapq.heappush(rooms, i[-1])
        min_rooms = len(rooms)
        return min_rooms
        
                
        
            