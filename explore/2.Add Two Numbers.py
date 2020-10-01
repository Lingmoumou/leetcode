

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode(0)
        ptr=result
        flag=False
        while(1):
            
            if l1 and l2:
                y=l1.val+l2.val
                l1=l1.next
                l2=l2.next
            elif l1:
                y=l1.val
                l1=l1.next
            elif l2:
                y=l2.val
                l2=l2.next
            else:
                break;

            if flag:
                y=y+1
                flag=False

            if y>=10 :
                ptr.next=ListNode(y-10)
                flag=True
            else:
                ptr.next=ListNode(y)

            ptr=ptr.next
            

        if flag:
            ptr.next=ListNode(1)
            ptr=ptr.next

        return result.next

    def addTwoNumbersWithCarry(self, l1, l2):
        result=ListNode(0)
        ptr=result
        carry=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sum=carry+x+y
            carry=int(sum/10)
            ptr.next=ListNode(sum%10)
            ptr=ptr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        if carry>0:
            ptr.next=ListNode(carry)
        
        return result.next



def stringToListNode(input):
    # Generate list from the input
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    s=Solution()
    l1=stringToListNode([3,4,9])
    l2=stringToListNode([4,6,5])
    
    print(listNodeToString(l1)+"->"+listNodeToString(l2))
    print(listNodeToString(s.addTwoNumbers(l1,l2)))
    print(listNodeToString(s.addTwoNumbersWithCarry(l1,l2)))

if __name__ == '__main__':
    main()         

