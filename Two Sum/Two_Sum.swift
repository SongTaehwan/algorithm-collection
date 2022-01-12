//
//  Palindrome_Number_Test.swift
//  Palindrome Number Test
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest
@testable import algorithms

class Two_Sum: XCTestCase {
    var sol: Solution!

    override func setUpWithError() throws {
        try super.setUpWithError()
        sol = Solution()
    }

    override func tearDownWithError() throws {
        try super.tearDownWithError()
        sol = nil
    }
    
    func testTwoSum() {
        XCTAssertEqual(sol.twoSum([2,7,11,15], 9), [0, 1])
        XCTAssertEqual(sol.twoSum([3,2,4], 6), [1,2])
        XCTAssertEqual(sol.twoSum([3,3], 6), [0, 1])
    }
    
}
