from Queue import Priorityqueue
p=PriorityQueue()
p.put=((4,'amrutha'))
p.put=((2,'swathi'))
p.put=((1,'amar'))
next=p.get()
print("next")
print(p.empty ())
print(p.full ())
p.put((3,'sneha'))
print(p.get())
while not (p.empty ()):
    print(p.get ())
    print(p.empty ())