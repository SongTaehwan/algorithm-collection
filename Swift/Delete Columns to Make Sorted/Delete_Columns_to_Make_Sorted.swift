//
//  Delete_Columns_to_Make_Sorted.swift
//  Delete Columns to Make Sorted
//
//  Created by 송태환 on 2022/02/25.
//

import XCTest

class Delete_Columns_to_Make_Sorted: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.minDeletionSize(["cba","daf","ghi"]), 1)
        XCTAssertEqual(sol.minDeletionSize(["a","b"]), 0)
        XCTAssertEqual(sol.minDeletionSize(["zyx","wvu","tsr"]), 3)
    }
}

