import heapq
# ---------------- Student Details ---------------- #
print("Nikita Saharan")
print("2401840008\n")

# Ticket class
class Ticket:
    def __init__(self, tid, name, issue, priority):
        self.id, self.name, self.issue, self.priority = tid, name, issue, priority
        self.next = None
    def __repr__(self):
        return f"Ticket({self.id}, {self.name}, {self.issue}, P={self.priority})"

# Linked List
class TicketList:
    def __init__(self): self.head = None
    def insert(self, t):
        if not self.head: self.head = t
        else:
            cur = self.head
            while cur.next: cur = cur.next
            cur.next = t
        print("Added:", t)
    def delete(self, tid):
        cur, prev = self.head, None
        while cur:
            if cur.id == tid:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                print("Deleted:", cur); return
            prev, cur = cur, cur.next
        print("Not Found")
    def retrieve(self, tid):
        cur = self.head
        while cur:
            if cur.id == tid: return vars(cur)
            cur = cur.next
        return None

# Stack for Undo
class Stack:
    def __init__(self): self.s = []
    def push(self, x): self.s.append(x)
    def pop(self): return self.s.pop() if self.s else None

# Priority Queue
class PriorityQ:
    def __init__(self): self.q = []
    def add(self, t): heapq.heappush(self.q, (t.priority, t))
    def get(self): return heapq.heappop(self.q)[1] if self.q else None

# Circular Queue
class CircularQ:
    def __init__(self, size): self.q, self.f, self.r, self.n = [None]*size, -1, -1, size
    def add(self, t):
        if (self.r+1)%self.n == self.f: return print("Full")
        if self.f == -1: self.f = 0
        self.r = (self.r+1)%self.n; self.q[self.r] = t
    def get(self):
        if self.f == -1: return None
        t = self.q[self.f]
        if self.f == self.r: self.f = self.r = -1
        else: self.f = (self.f+1)%self.n
        return t

# Polynomial Linked List compare
class Poly:
    def __init__(self,c,e): self.c,self.e,self.next=c,e,None
def compareBilling(p1,p2):
    out=[]
    while p1 and p2:
        if p1.e==p2.e: out.append((p1.c-p2.c,p1.e)); p1,p2=p1.next,p2.next
        elif p1.e>p2.e: out.append((p1.c,p1.e)); p1=p1.next
        else: out.append((-p2.c,p2.e)); p2=p2.next
    return out

# Demo
if __name__=="__main__":
    tl, st, pq, cq = TicketList(), Stack(), PriorityQ(), CircularQ(3)
    t1, t2 = Ticket(1,"Alice","Login",1), Ticket(2,"Bob","Payment",2)
    tl.insert(t1); tl.insert(t2); st.push(("insert",t2))

    print("\nRetrieve 1:", tl.retrieve(1))
    act=st.pop();
    if act: tl.delete(act[1].id)

    pq.add(t1); pq.add(t2)
    print("\nUrgent:", pq.get())

    cq.add(t1); cq.add(t2)
    print("\nRound Robin:", cq.get())
