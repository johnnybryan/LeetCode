/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
const reorderList = (head) => {
  if (!head || !head.next) return;
  
  let slow = head,
    fast = head;
  
  while (fast && fast.next) { // find midpoint of linked list
    slow = slow.next;
    fast = fast.next.next;
  }
  
  let part2 = slow.next;
  slow.next = null; // new tail
  
  let prev = null,
    cur = part2;
  
  while (cur) { // reverse second half of linked list
    let next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }
  
  part2 = prev;
  
  while (head && part2) { // merge lists into one
    let p1 = head.next;
    let p2 = part2.next;
    head.next = part2;
    head.next.next = p1;
    part2 = p2;
    head = p1;
  }
  
  return head;
};