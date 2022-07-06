//
//  Mock_Exam.swift
//  Mock Exam
//
//  Created by 송태환 on 2022/01/19.
//

import XCTest

class Mock_Exam: TestCase {

    func testSolution() {
//        XCTAssertEqual(solution([1,2,3,4,5,1,2,3,4,5]), [1])
        XCTAssertEqual(solution([1,3,2,4,2]), [1,2,3])
    }

}
