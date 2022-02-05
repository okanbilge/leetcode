# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:50:08 2022

@author: Okan
"""

list1 = [1,3,5]
list2 = [2,4,6]

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

list1=ListNode(1)
list1.next=ListNode(3)
list1.next.next=ListNode(5)
list2=ListNode(2)
list2.next=ListNode(4)
list2.next.next=ListNode(6)
list2.next.next.next=ListNode(7)
list2.next.next.next.next=ListNode(8)
list2.next.next.next.next.next=ListNode(9)



def mergeTwoLists(list1,list2):
    
    if (list1== None and list2== None):
        return None
    elif list1==None:
        return list2
    elif list2==None:
        return list1
    
    
    list3=ListNode()
    dummy=ListNode()
    list3=dummy


    while list1!= None and list2!= None:
        

        if list1.val<list2.val:
           dummy.val=list1.val
           list1 = list1.next
        else:
            dummy.val=list2.val
            list2 = list2.next
        
        if list1==None:
            dummy.next=list2
            
        elif list2==None:
            dummy.next=list1
        else:
            dummy.next=ListNode()
            dummy=dummy.next
    
    return list3           
    
t1=mergeTwoLists(list1,list2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
