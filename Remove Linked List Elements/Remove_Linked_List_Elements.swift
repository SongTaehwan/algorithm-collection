//
//  Remove_Linked_List_Elements.swift
//  Remove Linked List Elements
//
//  Created by 송태환 on 2022/04/07.
//

import XCTest

class Remove_Linked_List_Elements: TestCase {
    override func testSolution() {
        let list1 = createLinkedList([1,2,6,3,4,5,6])
        let result1 = LinkedList(head: sol.removeElements(list1.head, 6)!)
        XCTAssertEqual(result1.getValues(), [1,2,3,4,5])
        
        let list2 = createLinkedList([])
        let result2 = LinkedList(head: sol.removeElements(list2.head, 1)!)
        XCTAssertEqual(result2.getValues(), [])
        
        let list3 = createLinkedList([7,7,7,7])
        let result3 = LinkedList(head: sol.removeElements(list3.head, 7)!)
        XCTAssertEqual(result3.getValues(), [])
    }
}

