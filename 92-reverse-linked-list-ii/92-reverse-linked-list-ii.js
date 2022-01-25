/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
const reverseBetween = (head, left, right) => {
//   if (left===right) return head;
//   let prev = null;
//   let curr = head;
//   let i = 0;
  
//   while (curr && i < left - 1) {
//     prev = curr;
//     curr = curr.next;
//     i++;
//   }
  
//   let lastNodeOfFirstPart = prev;
//   let lastNodeOfSublist = curr;
//   let next = null;
//   i = 0;
  
//   while (curr && i < right - left + 1) {
//     next = curr.next;
//     curr.next = prev;
//     prev = curr;
//     curr = next;
//     i++;
//   }
  
//   if (lastNodeOfFirstPart !== null) {
//     lastNodeOfFirstPart = prev;
//   } else {
//     head = prev;
//   }
  
//   lastNodeOfSublist.next = curr;
//   return head;
  let current = head, 
      start = head, 
      i = 1;

  while (i < left) {
      start = current
      current = current.next;
      i++;
  }

  let reversedList = null,  
      tail = current;

  while(i >= left && i <= right) {
      const next = current.next;
      current.next = reversedList;
      reversedList = current;
      current = next;
      i++
  }

  start.next = reversedList;
  tail.next = current;


  return left > 1 ? head : reversedList
};