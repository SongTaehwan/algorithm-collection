//
//  Remove_the_least_number.swift
//  Remove the least number
//
//  Created by 송태환 on 2022/05/30.
//

import XCTest

class Remove_the_least_number: XCTestCase {

	func testSolution() {
		XCTAssertEqual(solution([4,3,2,1]), [4,3,2])
		XCTAssertEqual(solution([10]), [-1])
	}

}
