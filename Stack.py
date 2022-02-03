class Stack:
  def __init__(self):
    self.stack=[]
  def add(self,data):
    if data not in self.stack:
      self.stack.append(data)
      return True
    else:
      return False
  def remove(self):
    if len(self.stack)!=0:
      self.stack.pop()
      return True
    else:
      return False
  def peek(self):
    if len(self.stack)!=0:
      print(self.stack[-1])
  def Traverse(self):
    if len(self.stack)!=0:
      print(self.stack)
    else:
      print("list is empty")
ss=Stack()
for i in range(int(input())):
  ss.add(input())
ss.Traverse()
ss.remove()
ss.Traverse()
