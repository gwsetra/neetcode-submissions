class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## build graph
        graph = {}
        visited = set()
        courses = []
        loop_not_found = True

        def dfs(v, e):
            nonlocal loop_not_found
            # print('inside dfs')
            # print(v, e)
            if (v,e) in visited:
                # print('had been visited before')
                loop_not_found = False
            else:
                visited.add((v,e))
                # print('ill visit', v,e, graph[e])

                for item2 in graph[e]:
                    dfs(e, item2)
                visited.remove((v,e))

                
                

        # build courses
        for item in range(numCourses):
            graph[item] = []

        for item in prerequisites:
            graph[item[1]].append(item[0])
        
        # print(graph)
        for v, e in graph.items():
            # print(v, e)
            for e2 in e:
                # print(v, e2)
                dfs(v, e2)

        # print('visited', visited)
        return loop_not_found