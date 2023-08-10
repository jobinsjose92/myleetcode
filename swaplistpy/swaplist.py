class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to serve as the new head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            first_node = current.next
            second_node = current.next.next
            
            # Swapping
            first_node.next = second_node.next
            second_node.next = first_node
            current.next = second_node
            
            current = current.next.next
        
        return dummy.next
def create_linked_list(values):
    head = ListNode()
    current = head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Main function
if __name__ == "__main__":
    # Create the linked list
    linked_list_values = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(linked_list_values)
    
    # Print the original linked list
    print("Original linked list:")
    print_linked_list(linked_list)
    
    # Create a Solution instance
    solution = Solution()
    
    # Swap adjacent nodes
    new_head = solution.swapPairs(linked_list)
    
    # Print the swapped linked list
    print("Swapped linked list:")
    print_linked_list(new_head)