# https://leetcode.com/problems/water-and-jug-problem/description/

from collections import deque


class Solution:
    def canMeasureWater(self, X: int, Y: int, Z: int) -> bool:

        visited = set()

        queue = deque([(0, 0)])

        while queue:
            current_state = queue.popleft()
            a, b = current_state

            if a == Z or b == Z or a + b == Z:
                return True

            state = tuple(current_state)
            if state in visited:
                continue

            visited.add(state)

            # Pour operations
            queue.append((X, b))  # Fill jug X
            queue.append((a, Y))  # Fill jug Y
            queue.append((0, b))  # Empty jug X
            queue.append((a, 0))  # Empty jug Y

            # Transfer operations
            transfer_x_to_y = min(a, Y - b)
            queue.append((a - transfer_x_to_y, b + transfer_x_to_y))  # Pour from X to Y

            transfer_y_to_x = min(b, X - a)
            queue.append((a + transfer_y_to_x, b - transfer_y_to_x))  # Pour from Y to X

        return False

    def canMeasureWaterRecursive(X, Y, Z):
        visited = set()

        def dfs(a, b):
            if a == Z or b == Z or a + b == Z:
                return True

            state = (a, b)
            if state in visited:
                return False

            visited.add(state)

            # Pour operations
            if dfs(X, b):  # Fill jug X
                return True
            if dfs(a, Y):  # Fill jug Y
                return True
            if dfs(0, b):  # Empty jug X
                return True
            if dfs(a, 0):  # Empty jug Y
                return True

            # Transfer operations
            transfer_x_to_y = min(a, Y - b)
            if dfs(a - transfer_x_to_y, b + transfer_x_to_y):  # Pour from X to Y
                return True

            transfer_y_to_x = min(b, X - a)
            if dfs(a + transfer_y_to_x, b - transfer_y_to_x):  # Pour from Y to X
                return True

            return False

        return dfs(0, 0)


# ob = Solution()
#     # Example usage:
# X, Y, Z = 3, 5, 4
# print(ob.canMeasureWater(X, Y, Z))  # Output: True
#
# X, Y, Z = 2, 6, 5
# print(ob.canMeasureWater(X, Y, Z))  # Output: False

class Solution2:

    # 4 jugs

    def canMeasureWater(self, x, y, z, w, target):

        visited = set()

        initial_state = (0, 0, 0, 0)
        queue = deque([initial_state])

        while queue:
            current_state = queue.popleft()

            if target in current_state:
                return True

            if current_state in visited:
                continue

            visited.add(current_state)

            # Pour operations
            for i in range(4):
                for j in range(4):
                    if i != j:
                        poured = min(current_state[i], w - current_state[j])
                        new_state = list(current_state)
                        new_state[i] -= poured
                        new_state[j] += poured

                        # Check if the new state is valid
                        if all(0 <= val <= [x, y, z, w][idx] for idx, val in enumerate(new_state)):
                            if tuple(new_state) not in visited:
                                queue.append(tuple(new_state))

            # Empty operations
            for i in range(4):
                if current_state[i] > 0:
                    new_state = list(current_state)
                    new_state[i] = 0
                    if tuple(new_state) not in visited:
                        queue.append(tuple(new_state))

            # Fill operations
            for i in range(4):
                if current_state[i] < [x, y, z, w][i]:
                    new_state = list(current_state)
                    new_state[i] = [x, y, z, w][i]
                    if tuple(new_state) not in visited:
                        queue.append(tuple(new_state))

        return False

    def canMeasureWaterdfs(self, x, y, z, w, target):
        visited = set()

        def dfs(state):
            if target in state:
                return True

            if state in visited:
                return False

            visited.add(state)

            # Pour operations
            for i in range(4):
                for j in range(4):
                    if i != j:
                        poured = min(state[i], w - state[j])
                        new_state = list(state)
                        new_state[i] -= poured
                        new_state[j] += poured
                        if 0 <= new_state[i] <= x and 0 <= new_state[j] <= y:
                            if dfs(tuple(new_state)):
                                return True

            # Empty operations
            for i in range(4):
                if state[i] > 0:
                    new_state = list(state)
                    new_state[i] = 0
                    if dfs(tuple(new_state)):
                        return True

            # Fill operations
            for i in range(4):
                if state[i] < [x, y, z, w][i]:
                    new_state = list(state)
                    new_state[i] = [x, y, z, w][i]
                    if dfs(tuple(new_state)):
                        return True

            return False

        return dfs((0, 0, 0, 0))

    def canMeasureWaterX(self, x, y, z, w, target):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if z == target or z == x + y or z == x or z == y:
            return True

        if x + y + z < target or (x == 0 and y == 0) or gcd(x, y) == 0 or target % gcd(x, y) != z % gcd(x, y):
            return False

        return target <= w and (target % gcd(x, y) == 0)

    from collections import deque

    def water_balancing_jugs(self, entries, capacities, initial, final):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def pour(jug1, jug2):
            space = capacities[jug2] - initial[jug2]
            poured = min(initial[jug1], space)
            new_state = list(initial)
            new_state[jug1] -= poured
            new_state[jug2] += poured
            return tuple(new_state)

        def is_valid(state):
            return all(0 <= state[i] <= capacities[i] for i in range(4))

        def bfs():
            visited = set()
            queue = deque([(tuple(initial), 0)])

            while queue:
                current_state, steps = queue.popleft()

                if current_state == final:
                    return steps

                if current_state in visited:
                    continue

                visited.add(current_state)

                for i in range(4):
                    for j in range(4):
                        if i != j:
                            new_state = pour(i, j)

                            if is_valid(new_state) and new_state not in visited:
                                queue.append((new_state, steps + 1))

            return -1

        return bfs()


# Read input
# entries = int(input())
# capacities = [int(input()) for _ in range(4)]
# initial = [int(input()) for _ in range(4)]
# final = [int(input()) for _ in range(4)]
#
# ob = Solution2()
# result = ob.water_balancing_jugs(entries, capacities, initial, final)
# print(result)

# Example usage:
# entries = 12
# capacities = [13, 12, 10, 5]
# initial = [6, 6, 0, 0]
# final = [12,0,0,0]
#
# ob = Solution2()
# result = ob.water_balancing_jugs(entries, capacities, initial, final)
# print(result)


# x, y, z, w, k = 2, 5, 6, 7, 10
# jugs=[2, 5, 6, 7]
# ob = Solution2()
# print(ob.canMeasureWaterX(x,y,z,w, k))  # Output: True
#
# x,y,z,w=3, 5, 6, 7
# target = 4
# print(ob.canMeasureWaterX(x,y,z,w, target))  # Output: True
#
# x,y,z,w=2, 4, 5, 8
# target = 3
# print(ob.canMeasureWaterX(x,y,z,w, target))  # Output: False


from collections import deque


def water_balancing_steps(capacities, initial, final):
    if sum(initial) != sum(final):
        return -1  # Total water content must be the same in the initial and final states

    visited = set()
    queue = deque([(initial, 0)])

    while queue:
        current_state, steps = queue.popleft()
        visited.add(tuple(current_state))

        if current_state == final:
            return steps

        for i in range(len(capacities)):
            for j in range(len(capacities)):
                if i != j:
                    pour = min(current_state[i], capacities[j] - current_state[j])
                    new_state = list(current_state)
                    new_state[i] -= pour
                    new_state[j] += pour

                    if tuple(new_state) not in visited:
                        queue.append((new_state, steps + 1))
                        visited.add(tuple(new_state))

    return -1  # No solution found


# Example usage:
capacities = [13, 12, 10, 5]
initial_state = [6, 6, 0, 0]
final_state = [12, 0, 0, 0]

result = water_balancing_steps(capacities, initial_state, final_state)
print(result)


def water_balancing_steps_opt(capacities, initial, final):
    total_water = sum(initial)
    if total_water != sum(final):
        return -1  # Total water content must be the same in the initial and final states

    visited = set()
    queue = deque([(tuple(initial), 0)])

    while queue:
        current_state, steps = queue.popleft()
        visited.add(current_state)

        if current_state == tuple(final):
            return steps

        for i in range(len(capacities)):
            for j in range(len(capacities)):
                if i != j:
                    pour = min(current_state[i], capacities[j] - current_state[j])
                    new_state = list(current_state)
                    new_state[i] -= pour
                    new_state[j] += pour
                    new_state_tuple = tuple(new_state)

                    if new_state_tuple not in visited:
                        queue.append((new_state_tuple, steps + 1))
                        visited.add(new_state_tuple)

    return -1  # No solution found


# Example usage:
capacities = [13, 12, 10, 5]
initial_state = [6, 6, 0, 0]
final_state = [12, 0, 0, 0]
result = water_balancing_steps_opt(capacities, initial_state, final_state)
print(result)
