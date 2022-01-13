//
//  Reserve_Integer.swift
//  Reserve Integer
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest
@testable import algorithms

/// [Check out the problem](https://leetcode.com/problems/reverse-integer/)
class Reserve_Integer: TestCase {
    func testReverseInteger() {
        XCTAssertEqual(sol.reverse(123), 321)
        XCTAssertEqual(sol.reverse(-123), -321)
        XCTAssertEqual(sol.reverse(120), 21)
        XCTAssertEqual(sol.reverse(1534236469), 0)
        
        XCTAssertEqual(sol.refactoredReverse(123), 321)
        XCTAssertEqual(sol.refactoredReverse(-123), -321)
        XCTAssertEqual(sol.refactoredReverse(120), 21)
        XCTAssertEqual(sol.refactoredReverse(1534236469), 0)
    }

}
