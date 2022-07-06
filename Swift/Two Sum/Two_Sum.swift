//
//  Two_Sum.swift
//  Two Sum
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest

/// [Check out the problem](https://leetcode.com/problems/two-sum/)
class Two_Sum: TestCase {
    func testTwoSum() {
        XCTAssertEqual(sol.twoSum([2,7,11,15], 9), [0, 1])
        XCTAssertEqual(sol.twoSum([3,2,4], 6), [1,2])
        XCTAssertEqual(sol.twoSum([3,3], 6), [0, 1])
    }
    
}
