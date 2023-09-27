# https://leetcode.com/problems/course-schedule/description/

# This question is a dag topographical sort question in disguise
# To solve this, we'll use kahn's algorithm

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites and numCourses != 0:
            return True

        graph = defaultdict(list)
        in_degrees = defaultdict(int)

        # create the graph
        for node1, node2 in prerequisites:
            graph[node2].append(node1)

        # calculate in degrees for each node
        for vertex in graph:
            if vertex not in in_degrees:
                in_degrees[vertex] = 0
            for neighbor in graph[vertex]:
                in_degrees[neighbor] += 1

        # create a queue to track vertex with 0 indegree
        queue = deque([vertex for vertex in graph if in_degrees[vertex] == 0])

        courses_completed = 0
        while queue:
            current_vertex = queue.popleft()
            # if a node can be traversed that means that a course can be completed or
            # number of orders that can be followed would be the number of courses the
            # student can take
            courses_completed += 1

            for neighbor in graph[current_vertex]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        if courses_completed >= numCourses or (courses_completed < numCourses and courses_completed == len(graph)):
            return True
        return False

    def canFinishCycleApproach(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # simpler approach, check for cycle in the graph
        # if there's any cycle that means, there would be
        # atleast 1 node that can't be visited
        # hence can't complete all the courses
        # as numCourses>ai,bi
        if not prerequisites and numCourses != 0:
            return True

        graph = defaultdict(list)
        in_degrees = defaultdict(int)

        # create the graph
        for node1, node2 in prerequisites:
            graph[node2].append(node1)

        # calculate in degrees for each node
        for vertex in graph:
            if vertex not in in_degrees:
                in_degrees[vertex] = 0
            for neighbor in graph[vertex]:
                in_degrees[neighbor] += 1

        # create a queue to track vertex with 0 indegree
        queue = deque([vertex for vertex in graph if in_degrees[vertex] == 0])
        topo_sort = []
        courses_completed = 0
        while queue:
            current_vertex = queue.popleft()
            # if a node can be traversed that means that a course can be completed or
            # number of orders that can be followed would be the number of courses the
            # student can take
            topo_sort.append(current_vertex)

            for neighbor in graph[current_vertex]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        if len(topo_sort) == len(graph):
            return True
        return False

num_courses = 1
prerequisites = [[1, 0]]
ob = Solution()
print(ob.canFinish(num_courses, prerequisites))
