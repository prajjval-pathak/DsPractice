class Qd:
  def __init__(self):
    self.queue=[]
  def Add(self,data):
    if data not in self.queue:
      self.queue.insert(0,data)
  def dequeue(self):
    if len(self.queue)!=0:
      self.queue.pop()
  def Traverse_queue(self):
    for i in self.queue:
      print(i)
qu=Qd()
qu.Add("MOn")
qu.Add("TUE")
qu.Add("hello")
qu.dequeue()
qu.Traverse_queue()


