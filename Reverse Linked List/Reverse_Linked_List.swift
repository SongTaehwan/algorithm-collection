//
//  Reverse_Linked_List.swift
//  Reverse Linked List
//
//  Created by 송태환 on 2022/02/17.
//

import XCTest

class Reverse_Linked_List: TestCase {
    override func testSolution() {
        let list1 = createLinkedList([1,2,3,4,5])
        let result1 = LinkedList(head: sol.reverseList(list1.head)!)
        XCTAssertEqual(result1.getValues(), [5,4,3,2,1])
    }
}

