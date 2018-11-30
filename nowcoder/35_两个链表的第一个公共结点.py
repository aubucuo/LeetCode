class Solution:
    def FindFirstCommonNode(self, head1, head2):
        # write code here
        list1 = []
        list2 = []
        node1 = head1
        node2 = head2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next