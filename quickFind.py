class QuickFind(object):
    def create(self,length):
        listTest = []
        for i in range(0,length):
            listTest.append(i)
        return listTest

    def connect(self,q,p):
        if l1[q] == l1[p]:
            return True
        else:
            return False

    def union(self,q,p):
        changed = l1[q]
        for i in range(0,len(l1)):
            if l1[i] == changed:
                l1[i] = l1[p]
        return l1

 

quickFind = QuickFind()
l1 = quickFind.create(10)
print(quickFind.union(1,2))
print(quickFind.union(2,3))
print(quickFind.connect(2,3))
