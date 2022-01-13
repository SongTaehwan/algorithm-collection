//
//  Remove_Duplicates_from_Sorted_List.swift
//  Remove Duplicates from Sorted List
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest
@testable import algorithms

/// [Check out the problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
class Remove_Duplicates_from_Sorted_List: TestCase {
    func testDeleteDuplicates() {
        let head1 = Solution.createListNode([1,1,2])
        XCTAssertEqual(Solution.getNodeResult(sol.deleteDuplicates(head1)), [1,2])
        XCTAssertEqual(Solution.getNodeResult(sol.deleteDuplicatesWithHashMap(head1)), [1,2])

        let head2 = Solution.createListNode([1,1,2,3,3])
        XCTAssertEqual(Solution.getNodeResult(sol.deleteDuplicates(head2)), [1,2,3])
        XCTAssertEqual(Solution.getNodeResult(sol.deleteDuplicatesWithHashMap(head2)), [1,2,3])
        
        let head3 = Solution.createListNode([1,1,1])
        XCTAssertEqual(Solution.getNodeResult(sol.deleteDuplicates(head3)), [1])
        XCTAssertEqual(Solution.getNodeResult(sol.deleteDuplicatesWithHashMap(head3)), [1])
    }
}
