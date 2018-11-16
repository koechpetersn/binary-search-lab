class Array():
  def __init__(self):
    pass
  def toTwenty(self):
    list1 = range(1,21)
    return list1
  def toForty(self):
    list2 = range(2,41,2)
    return list2
  def toOneThousand(self):
    list3 = range(10,1001,10)
    return list3



class binarySearch(Array):
  def __init__(self):
    pass
  
  
  def binarySearch(self,alist,item):

    first = 0
    last = len(alist)-1
    found = False
    

    while first<=last and not found:
      midpoint = (first + last)//2
      #print (midpoint)
      if alist[midpoint] == item:
        
        found = True
        m=midpoint
      else:
        if item < alist[midpoint]:
          last = midpoint-1
        else:
          first = midpoint+1
	
    return m
	


  def search(self,number):
    #self.count = 0
    self.index = self.binarySearch(alist,100)
    self.length = len(alist)
    return self.index,self.length

'''
numb=binarySearch()
alist=numb.toOneThousand()
print(numb.search(100))
'''

