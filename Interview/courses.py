'''

here are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].


'''

from collections import defaultdict, deque


def findOrder(numCourses, prerequisites):
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


# Example usage:
numCourses1, prerequisites1 = 2, [[1, 0]]
print(findOrder(numCourses1, prerequisites1))  # Output: [0, 1]

numCourses2, prerequisites2 = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(numCourses2, prerequisites2))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
