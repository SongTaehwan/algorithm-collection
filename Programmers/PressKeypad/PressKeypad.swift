//
//  PressKeypad.swift
//  PressKeypad
//
//  Created by 송태환 on 2022/05/29.
//

import XCTest

class PressKeypad: XCTestCase {

	func testSolution() {
		XCTAssertEqual(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"), "LRLLLRLLRRL")
		XCTAssertEqual(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"), "LRLLRRLLLRR")
		XCTAssertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"), "LLRLLRLLRL")
	}

}
