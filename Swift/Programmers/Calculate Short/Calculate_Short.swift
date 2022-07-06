//
//  Calculate_Short.swift
//  Calculate Short
//
//  Created by 송태환 on 2022/04/26.
//

import XCTest

class Calculate_Short: TestCase {
	func testSolution() {
		XCTAssertEqual(solution(3, 20, 4), 10)
		XCTAssertEqual(refactor(3, 20, 4), 10)
	}
}

