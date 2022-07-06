//
//  Middle_of_the_Linked_List.swift
//  Middle of the Linked List
//
//  Created by 송태환 on 2022/04/08.
//

import XCTest

class Middle_of_the_Linked_List: TestCase {
    override func testSolution() {
        let list1 = createLinkedList([1,2,3,4,5])
        let result1 = LinkedList(head: sol.middleNode(list1.head)!)
        XCTAssertEqual(result1.getValues(), [3,4,5])
        
        let list2 = createLinkedList([1,2,3,4,5,6])
        let result2 = LinkedList(head: sol.middleNode(list2.head)!)
        XCTAssertEqual(result2.getValues(), [4,5,6])
    }
    
    func testSolutionRefactored() {
        let list1 = createLinkedList([1,2,3,4,5])
        let result1 = LinkedList(head: sol.refactor(list1.head)!)
        XCTAssertEqual(result1.getValues(), [3,4,5])
        
        let list2 = createLinkedList([1,2,3,4,5,6])
        let result2 = LinkedList(head: sol.refactor(list2.head)!)
        XCTAssertEqual(result2.getValues(), [4,5,6])
    }
}

