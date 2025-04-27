# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self, item):
#         self.stack.append(item)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return "Stack is empty"
    
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             return "Stack is empty"
    
#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def display(self):
#         print(self.stack)

# # Example usage
# s = Stack()   # Capital S
# s.push(20)
# s.push(30)
# s.push(40)
# s.display()
# print("Popped out:", s.pop())
# s.display()

# ----------------------------------------------------------------------------------------

# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,item):
#         self.queue.append(item)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         else:
#             return "queue is empty"
#     def is_empty(self):
#         return len(self.queue)==0
#     def display(self):
#         return(self.queue)
#     def front(self):
#         if not self.is_empty():
#             return self.queue[0]
#         else:
#             return "queue is empty"
    
 
# q= Queue()
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.display
# print("popped",q.dequeue)
# q.display

# ----------------------------------------------------------------------------------------
def binary_search(arr, target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

array=[1,2,3,4,5,6,7]
tget=7
result=binary_search(array,tget)
if result==-1:
    print ("result not found")
else:
    print(f"value is at index {result}")
    

    

        
