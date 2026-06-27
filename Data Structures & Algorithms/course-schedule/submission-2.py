class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## build graph
        graph = {}
        prereqlen = len(prerequisites)

        print(prerequisites)

        for item in prerequisites:
            if item[0] not in graph:
                graph[item[1]] = item[0]
        
        print(len(graph))
        print(graph)

        if not prereqlen:
            return True
        elif prereqlen != len(graph):
            return False
        elif numCourses == len(graph)*2:
            return True
        else:
            return False