class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            cur_meet_end = intervals[i][-1]
            next_meet_start = intervals[i + 1][0]
            if cur_meet_end > next_meet_start:
                return False
        return True
            