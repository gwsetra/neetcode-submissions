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
                    print('inside loop not found')
                    loop_not_found = False

                    return False
                visited.add((v, e))
                return find_cycle(e, adjlist[e])
                visited.remove((v, e))
            
            return True

        def check_all_element():
            for key, values in adjlist.items():
                if loop_not_found:
                    return find_cycle(key, values)
            return False

        

        for item in range(numCourses):
            if item not in adjlist:
                adjlist[item] = []
        
        for item in prerequisites:
            adjlist[item[1]].append(item[0])
    


        return check_all_element()