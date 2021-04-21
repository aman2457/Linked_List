#Creating Node Class
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    

#Creating a class for Singly Link List
class SinglyLinkList:
    #Initializing the Link List
    def __init__(self):
        self.head = None
    
    #Utility Function for Print The Nodes
    def printList(self):
        llValues = []
        temp = self.head
        if self.head is None:
            return llValues
        else:
            while temp is not None:
                llValues.append(temp.data)
                temp = temp.next
        
        return llValues
    



    #Function which add a node as the first Node .(Push)
    def push(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    

    
    #It insert the node at the last of the node. (append)
    def append(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        
        while (temp.next):
            temp = temp.next
        
        temp.next = newNode
        
    #It insert the given data after the specific element.
    def insert(self,afterElement,newData):
        temp = self.head
        temp2 = self.head
        while (temp is not None) and (temp.data != afterElement):
                temp2 = temp
                temp = temp.next
            
        if temp is None:
            return -1
        else:
            newNode = Node(newData)
            newNode.next = temp.next
            temp.next = newNode
        
    
    #It remove the element from the linklist
    def remove(self,element):
        temp = self.head
        
        
        if temp is not None:
            if temp.data == element:
                self.head = temp.next
                return
        
        while (temp is not None) and (temp.data != element):
                temp2 = temp
                temp = temp.next
            
        if temp is None:
            return -1
        
        else:
            temp2.next = temp.next
            return 
    
    #A universal function which delete the entire Linklist in One go
    def delete(self):
        temp = self.head
        
        while temp:
            nextRef = temp.next
            del temp.data
            temp = nextRef
        return 
    
    
    #return the length of the Linklist
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count  
   
    #return True if Found else False.
    def search(self,key):
        temp = self.head
        pos = 0
        if temp.data == key:
            return True
        
        while temp:
            pos += 1
            if temp.data == key:
                #print('Element is at position {}'.format(pos))
                return True
            temp = temp.next
        return False
    
    #return the element located at the Nth Position in the linklist
    def getNth(self,n):
        temp = self.head
        count = 0
        
        if n <= 0 or n > self.length():
            return -1
        
        while temp:
            count += 1
            if count == n:
                return temp.data
            temp = temp.next
            
    #return the element located at the Nth Position from the last in the linklist    
    def getNthFromLast(self,n):
        length = self.length()
        temp = self.head
        i = 0
        if n > length:
            return -1
        while i < (length-n):
            temp = temp.next
            i += 1
        return temp.data
    
    #return the Middile Element of the linklist, if len is even then ceil(mid) element is given
    def midElement(self):
        length = self.length()
        mid = ((length)//2)+1
        temp = self.head
        i = 1 
        while i < mid:
            temp = temp.next
            i += 1
        return temp.data
    
    #return the count of the given Key
    def count(self,key):
        temp = self.head
        count = 0
        while temp is not None:
            if temp.data == key:
                count += 1
            temp = temp.next
        return count     
        
    
    #it will check if the linklist contains any loop
    def checkLoop(self):
        tempSlow = self.head
        tempFast = self.head
        
        while tempSlow != None and tempFast != None:
            tempSlow = tempSlow.next
            tempFast = tempFast.next.next
            
            if tempSlow == tempFast:
                return True
        return False  
    
    #first it will check if the linklist contains any loop then return length of the loop
    def lengthOfLoop(self):
        tempSlow = self.head
        tempFast = self.head
        flag = None
        while tempSlow != None and tempFast != None:
            tempSlow = tempSlow.next
            tempFast = tempFast.next.next
            
            if tempSlow == tempFast:
                flag = tempSlow.data
                break
            
        if flag == None:
            return 'No Loop'
        else:
            count = 1
            temp = tempSlow.next
            while temp.data != flag:
                count += 1
                temp = temp.next
        return count    
    
    #check if the Linklist is Palindrome or not
    def isPalindrome(self):
        temp = self.head
        
        isPalin = False
        
        stack = []
        
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        
        temp2 = self.head
        
        while temp2 is not None:
            element = stack.pop()
            if temp2.data == element:
                isPalin = True
            else:
                isPalin = False
                break
            temp2 = temp2.next
        return isPalin
    
    #return the unqiue elements of the sorted linklist
    def uniqueSorted(self):
        temp = self.head
        temp2 = None
        
        while temp.next is not None:
            if temp.next.data == temp.data:
                temp2 = temp.next
                temp.next = temp2.next
            
            else:
                temp = temp.next
        ref = self.head
        return ref

    #return the even element followed by the odd elements
    #Time complexity: O(n)
    def segregateEvenOdd(self):
        temp = self.head
        
        evenStart = None
        
        evenEnd = None
        
        oddStart = None
        
        oddEnd = None
        
        while temp is not None:
            value = temp.data
            
            if (value % 2 == 0):
                if evenStart == None:
                    evenStart = temp
                    evenEnd = evenStart
                else:
                    evenEnd.next = temp
                    evenEnd = evenEnd.next
            else:
                if oddStart == None:
                    oddStart = temp
                    oddEnd = oddStart
                else:
                    oddEnd.next = temp
                    oddEnd = oddEnd.next
                    
            temp = temp.next
            
        if evenStart == None or oddStart == None:
            return
        
        else:
            evenEnd.next = oddStart
            oddEnd = None
        
        self.head = evenStart

        
    
    
    
    
    #modify the existing LinkList in reverseOrder
    def reverseList(self):
        prev = None
        temp = self.head
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev 
        
    
#return True if the caller and given argument LinkList is Identical
def isIdentical(ll1,ll2):
    isIdentical = False
    a = ll1.head
    b = ll2.head
        
    if ll1.length() != ll2.length():
        return isIdentical
        
    else:
        while (a is not None) and (b is not None):
            if a.data == b.data:
                isIdentical = True
                
            else:
                isIdentical = False
                return isIdentical
                
            a = a.next
            b = b.next
        
    return isIdentical        




def mergeTwoLists(l1 ,l2):
    l3 = Node()
    temp1 = l1
    temp2 = l2
    while (temp1 is not None) and (temp2 is not None):
        if temp1.data  < temp2.data:
            l3.next = ListNode(temp1.data)
            l3 = l3.next
            temp1 = temp1.next
        else:
            l3.next = ListNode(temp2.data)
            l3 = l3.next
            temp2 = temp2.next
        
    if temp1 is not None:
        while temp1 is not None:
            l3.next =ListNode(temp1.data)
            l3 = l3.next
            temp1 = temp1.next
        
    if temp2 is not None:
        while temp2 is not None:
            l3.next = ListNode(temp2.data)
            l3 = l3.next
            temp2 = temp2.next
       
    return l3.next

