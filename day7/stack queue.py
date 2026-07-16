# day07/stack_queue.py

# -----------------------------
# Stack Implementation
# -----------------------------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


# -----------------------------
# Queue Implementation
# -----------------------------
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


# --------------------------------------------------
# Balanced Brackets using Stack
# Time Complexity: O(n)
# --------------------------------------------------
def balanced_brackets(s):
    stack = Stack()

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            if stack.is_empty():
                return False

            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


# --------------------------------------------------
# Maximum Sliding Window Sum using Queue
# Time Complexity: O(n)
# --------------------------------------------------
def max_sliding_window_sum(nums, k):
    q = Queue()

    current_sum = 0
    max_sum = float("-inf")

    for num in nums:
        q.enqueue(num)
        current_sum += num

        if len(q.items) > k:
            current_sum -= q.dequeue()

        if len(q.items) == k:
            max_sum = max(max_sum, current_sum)

    return max_sum


# -----------------------------
# TEST CASES
# -----------------------------

# Stack Tests
stack = Stack()

stack.push(10)
stack.push(20)

assert stack.peek() == 20
assert stack.pop() == 20
assert stack.pop() == 10
assert stack.is_empty()

# Queue Tests
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

assert queue.front() == 1
assert queue.dequeue() == 1
assert queue.front() == 2

# Balanced Brackets Tests
assert balanced_brackets("()") == True
assert balanced_brackets("([]{})") == True
assert balanced_brackets("(]") == False
assert balanced_brackets("(((") == False

# Sliding Window Tests
assert max_sliding_window_sum([1,2,3,4,5],2) == 9
assert max_sliding_window_sum([2,1,5,1,3,2],3) == 9
assert max_sliding_window_sum([10,5,2,7,8,7],3) == 22

print("All Stack and Queue tests passed!")