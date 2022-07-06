//
//  Reverse_String.swift
//  Reverse String
//
//  Created by 송태환 on 2022/02/10.
//

import XCTest

class Reverse_String: TestCase {
    override func testSolution() {
        var s1: [Character] = ["h","e","l","l","o"]
        var s2: [Character] = ["H","a","n","n","a","h"]
        
        sol.reverseString(&s1)
        sol.reverseString(&s2)
        
        XCTAssertEqual(s1, ["o","l","l","e","h"])
        XCTAssertEqual(s2, ["h","a","n","n","a","H"])
    }
}
