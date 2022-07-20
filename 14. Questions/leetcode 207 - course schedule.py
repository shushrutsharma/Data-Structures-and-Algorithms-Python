# course schedule | leetcode 207 | https://leetcode.com/problems/course-schedule/
# method: depth first search

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        # init prequisite map
        preqMap = {}
        for i in range(numCourses):
            preqMap[i] = []
       
        # add mentioned prerequisites 
        for crs, pre in prerequisites:
            preqMap[crs].append(pre)
          
        # init visit set
        visitSet = set()
        
        # dfs
        def checkPreq(crs):
            
            # if course is already visited 
            if crs in visitSet:
                return False 
           
            # if no prequisites left
            if preqMap[crs] == []:
                return True
           
            # visiting this course
            visitSet.add(crs)
            
            # checking each prerequisite
            for pre in preqMap[crs]:
                if not checkPreq(pre): return False
            
            # all prerequisites are doable
            visitSet.remove(crs)
            preqMap[crs] = []
            return True
        
        # check prerequisites for each course
        for crs in range(numCourses):
            if not checkPreq(crs): return False
           
        return True
