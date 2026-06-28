class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        visited = set()

        def find_cycle(v, edges):
            if not edges:
                return True

            for e in edges:
                if (v, e) in visited:

                    return False
                visited.add((v, e))
                if not find_cycle(e, adjlist[e]):
                    return False
                visited.remove((v, e))
            
            return True

        def check_all_element():
            for key, values in adjlist.items():
                if find_cycle(key, values) == False:
                    return False
            return True

        for item in range(numCourses):
            if item not in adjlist:
                adjlist[item] = []
        
        for item in prerequisites:
            if item[1] == item[0]:
                return False
            adjlist[item[1]].append(item[0])

        return check_all_element()