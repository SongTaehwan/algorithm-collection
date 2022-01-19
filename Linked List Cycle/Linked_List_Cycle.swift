//
//  Linked_List_Cycle.swift
//  Linked List Cycle
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest

/// [Check out the problem](https://leetcode.com/problems/linked-list-cycle/)
class Linked_List_Cycle: TestCase {
    func testHasCycle() {
        let list1 = LinkedList(head: Solution.createListNode([3,2,0,-4]))
        list1.tail?.next = list1.findNode(at: 1)
        XCTAssertEqual(sol.hasCycle(list1.head), true)

        let list2 = LinkedList(head: Solution.createListNode([1,2]))
        list2.tail?.next = list2.head
        XCTAssertEqual(sol.hasCycle(list2.head), true)
        
        let list3 = LinkedList(head: Solution.createListNode([1]))
        XCTAssertEqual(sol.hasCycle(list3.head), false)
    }

}
