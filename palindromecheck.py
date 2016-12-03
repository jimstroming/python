class Node(object):
    value = None
    nextnode = None

    


# Implement a function to check if a linked list is a palindrome

def checkpalindrome(headnode):
    base = 1
    forwardchecksum = 0
    backwardchecksum = 0
    currentnode = headnode
    while(currentnode != None):
        forwardchecksum += ord(currentnode.value) * base
        base = base*256
        backwardchecksum *= 256
        backwardchecksum += ord(currentnode.value)
        currentnode = currentnode.nextnode  
        print("forward checksum equals",forwardchecksum)
        print("backward checksum equals",backwardchecksum)
        
    if forwardchecksum == backwardchecksum:
        return True
    return False    
    
    
Node1 = Node()
Node2 = Node()
Node3 = Node()
Node1.value = "D"
Node1.nextnode = Node2
Node2.value = "o"
Node2.nextnode = Node3
Node3.value = " "
Node3.nextnode = Node4
Node4.value = "n"
Node4.nextnode = Node5
Node5.value = "o"
Node5.nextnode = Node6
Node6.value = "d"
Node6.nextnode = None

if checkpalindrome(Node1):
    print("wow is a palindrome")
else:
    print("wow is not a palindrome")  