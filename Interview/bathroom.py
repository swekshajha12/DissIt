'''
The system coding round is where the real test lies at Rubrik.
Strong fundamentals in concurrency are crucial to crack this round.
You should be capable of implementing concurrent handling or logic using fundamental datatypes such as mutex and locks.
While you don't need in-depth knowledge of operating systems or computer architecture,
understanding how to implement threads in your chosen programming language is essential.
Knowing about complex structures like BlockingQueue or ConcurrentHashMap is not necessary,
but understanding their implementation is vital.
Leetcode offers a good set of problems to practice concurrent programming.
Ensure that your implementation goes beyond pseudocode and can demonstrate your understanding of the concepts.


'''


'''
1. There is single Bathroom to be used in a Voting agency for both Democrats(D) and Republicans(R) *
This single Bathroom which can accomodate 3 people at most * each person takes f(N) secs to do his thing.
f(N) is a function of the person's name and returns varying number *
 CONDITION: At any given time, the bathroom cannot have a mixed set of people i.e.
 * CONDITION: Bathroom can have at most 3 people * these combinations aren't allowed (2D, 1R) or (1D,1R)
  * These are allowed (), (3D), (2D), (1R) i.e. pure Republicans or Pure Democrats
  * While the bathroom is occupied people are to wait in a queue
  * What is the most optimal system where you would manage people in this queue, so that
   * the most eligible person instants gets to use the bathroom whenever its has room, based on above conditions


2. calender invite send. thread sleeping and waking using priority queue

3. https://leetcode.com/problems/robot-bounded-in-circle/description/

4. Design microservices and design GPS system

5. Design Twitter with Notification service

6. Producer-Consumer Multi-Threaded problem

7. Task Scheduler with Multi-Threading

8. Binary search tree... Max heap

9.  System Coding round - a variation of leetcode: building H2O

10. Variation of leetcode: counting elements with Follow-ups on optimization

11. System design - related to Unique ID generation

12. concurrency, multithreading, mutex locks, semaphores, object oriented programing

13. FIFO heap with some questions

14. Develop sparse file system.

15. Develop task runner.

16. Design a service to generate global ID at web scale.

17. Design a notification service.

18. Design and implement a snapshot scheduler.

19. binary tree to ask about the counting the sum path of BST

20. Implement LRU Cache.

21.implement an autocomplete engine where the input is a prefix string, then a number
representing the min number of words that could come after it.
 For example, wa3 could represent wafer, water, or Washington. Gelat2 could represent gelatin,
 but not gelato. Return all of these autocomplete results in a list.

 22. Implement a thread safe queue

 23. minstack, complete binary tree

 24. Graph pblem, array search

 25. Find best path in a hill with mines.
 Maximums in a sliding window
 Interval intersection.

 26. Build a key-value data structure that allows the user to take a snapshot of the data. The user can read the key-value store from any snapshot.

 Structure has the normal key/value like methods plus something like
 snapshot = dataStructure.takeSnapshot()
 value = dataStructure.get(key, snapshot)
 void dataStructure.deleteSnapshot()
    sol  : This was pretty fun problem. Implemented this as a hash with the values being a list.
    Taking a snapshot returns the list index for every key in hash.

27. We have a large code base that needs to be compiled but the files must be parsed in dependency order (no file can be parsed until its dependencies have been parsed).

28. A 2d board-game starts out as all water tiles. The board has an API function uint addLand(x, y) which converts the tile at the coordinates x, y into land and returns the total number of islands in the world. Implement this function.

29. Implement an LRU cache

30. Find local maximum numbers in a integer array

31. Insert a node in a complete binary tree efficiently.

32. A table has some number of balls at various positions on a line segment. All are moving with same speed in one or the other direction. Wherever a collision occurs they change direction. A ball falls from the edges of the table. Find the time when all balls fall of the table given initial position of each ball and speeds.



'''