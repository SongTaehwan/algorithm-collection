//
//  Reverse_Bits.swift
//  Reverse Bits
//
//  Created by 송태환 on 2022/01/19.
//

import XCTest

class Reverse_Bits: TestCase {

    func testReverseBits() {
        XCTAssertEqual(sol.reverseBits(43261596), 964176192)
        XCTAssertEqual(sol.reverseBits(4294967293), 3221225471)
    }

}
