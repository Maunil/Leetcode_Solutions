"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        
        rooms = 0
        flag = 0 
        
        end_list = []
        start_list = []
        
        for i in range(0, len(intervals)):
            start_list.append(intervals[i].start)
            end_list.append(intervals[i].end)
        
        start_list.sort()
        end_list.sort()
        
        for i in range(len(intervals)):
            
            if start_list[i] < end_list[flag]: 
                rooms = rooms + 1 
            else:
                flag = flag + 1 
            
        return rooms
            
        
        
        
        
            
        
    