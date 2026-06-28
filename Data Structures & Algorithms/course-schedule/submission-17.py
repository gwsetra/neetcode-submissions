class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        visited = set()
        loop_not_found = True

        def find_cycle(v, edges):
            if not edges:
                return True
            
            # print('inside find_cycle', v, edges)
            for e in edges:
                # print(v, e)
                if (v, e) in visited:
                    # print('cycle found')

                    return False
                visited.add((v, e))
                resultx = find_cycle(e, adjlist[e])
                # print('resultx::', resultx)
                if not resultx:
                    return False
                visited.remove((v, e))
            
            return True

        def check_all_element():
            for key, values in adjlist.items():
                # print('start outer element', key, values)
                # if loop_not_found:
                result = find_cycle(key, values)
                # print('result::', result)
                if  result == False:
                    return False
            return True

        

        for item in range(numCourses):
            if item not in adjlist:
                adjlist[item] = []
        

        for item in prerequisites:
            if item[1] == item[0]:
                return False
            adjlist[item[1]].append(item[0])
        # print(adjlist)


        return check_all_element()