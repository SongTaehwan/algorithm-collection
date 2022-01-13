//
//  Convert_Binary_Number_in_a_Linked_List_to_Integer.swift
//  Convert Binary Number in a Linked List to Integer
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest

class Convert_Binary_Number_in_a_Linked_List_to_Integer: TestCase {
    func testGetDecimalValue() {
        let head = Solution.createListNode([1,0,1])
        XCTAssertEqual(sol.getDecimalValue(head), 5)
        XCTAssertEqual(sol.refactored(head), 5)
    }

}
