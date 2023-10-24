# https://leetcode.com/problems/course-schedule-ii/description/

# This question is a variation of course schedule 1
# Here we first identify if it's possible to complete the courses
# if yes, then we return the topological sort value
# otherwise an empty array

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Build a graph to represent the course dependencies
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses that have no prerequisites
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])

        order = []

        # Perform topological sorting
        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # If all courses can be taken, return the order; otherwise, return an empty array
        return order if len(order) == numCourses else []


ob = Solution()
# print(ob.findOrder(2, [[1,0]]))
# print(ob.findOrder(3, []))
# print(ob.findOrder(3, [[1,0]]))
print(ob.findOrder(4, [[3, 0], [0, 1]]))
