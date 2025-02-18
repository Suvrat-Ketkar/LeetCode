struct ListNode {
    int val;
    ListNode *next;
     ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(); // Dummy node to simplify result list management
        ListNode* current = dummy; // Pointer to the current node in the result list
        int carry = 0; // To store the carry value during addition

        // Traverse both lists
        while (l1 != nullptr || l2 != nullptr || carry > 0) {
            int sum = carry; // Start with the carry value

            // Add values from l1 and l2 if they exist
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            carry = sum / 10; // Carry is the tens place
            int digit = sum % 10; // The digit to store is the ones place

            // Create a new node with the calculated digit and attach it
            current->next = new ListNode(digit);
            current = current->next;
        }

        // Return the head of the result list
        return dummy->next;
    }
};
