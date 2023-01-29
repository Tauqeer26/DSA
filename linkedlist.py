class Node1:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        node=Node1(data,self.head)
        self.head=node
    def print(self):
        if self.head==None:
            print("linked list is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'--->'
            itr=itr.next

        print(llstr)
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node1(data,None)
            return 
        itr=self.head
        while itr.next:
            itr=itr.next
            print(itr.next)
        itr.next=Node1(data,None)
    def insert_mulitvalues(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remve_element(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head=self.head.next
            #good thing about python is that it will do the garbage collection for you automatically
            return
        count=0
        itr=self.head
        while itr:

            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_mulitvalues(['12','nice','brilliant'])
    ll.remve_element(1)
    #ll.insert_mulitvalues(['nice','good','great'])
    ll.print()
    print('Length of my List is',ll.get_length())