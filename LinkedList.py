class Node:
  def __init__(self,dataval=None):
    self.dataval=dataval
    self.next=None
class Linkedlist:
  def __init__(self):
    self.headval=None
  def TraverseList(self):
    printval=self.headval
    while printval is not None:
      print(printval.dataval)
      printval=printval.next
  def Insertmid(self,mid,data):
    if mid is None:
      print("No data node found")
    else:
      new=Node(data)
      new.next=mid.next
      mid.next=new
  def insetbeg(self,data):
    NewNode=Node(data)
    NewNode.next=self.headval
    self.headval=NewNode
  def Reverse(self):
    prev=None
    current=self.headval
    while(current is not None):
      nex=current.next
      current.next=prev
      prev=current
      current=nex
    self.headval=prev


ll=Linkedlist()
ll.headval=Node("m")
e2=Node("t")
e3=Node("w")
ll.headval.next=e2
e2.next=e3
ll.insetbeg("S")
ll.Insertmid(e2,"fri")
# ll.TraverseList()
ll.Reverse()
ll.TraverseList()
