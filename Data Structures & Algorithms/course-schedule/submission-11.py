class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        visited = set()
        loop_not_found = True

        def find_cycle(v, edges):
            nonlocal loop_not_found
            # print('inside find_cycle', v, edges)
            for e in edges:
                # print(v, e)
                if (v, e) in visited:
                    # print('has been visited', (v,e))
                    loop_not_found = False
                    return True
                visited.add((v, e))
                find_cycle(e, adjlist[e])
                visited.remove((v, e))




        
        # build adjlist
        for item in range(numCourses):
            if item not in adjlist:
                adjlist[item] = []
        
        # print(adjlist)
        # fill element 
        for item in prerequisites:
            adjlist[item[1]].append(item[0])
        
        # print(adjlist)
        # print(adjlist[0])

        # return find_cycle()

        # loop over adjlist  
        for key, values in adjlist.items():
            # print('outside loop')
            # print(key, values)
            if loop_not_found:
                find_cycle(key, values)
        # for 
        # find_cycle(0, adjlist[0])

        return loop_not_found