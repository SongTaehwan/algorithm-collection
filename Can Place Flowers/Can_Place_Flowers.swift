//
//  Can_Place_Flowers.swift
//  Can Place Flowers
//
//  Created by 송태환 on 2022/01/18.
//

import XCTest

class Can_Place_Flowers: TestCase {
    func testCanPlaceFlowers() {
//        XCTAssertEqual(sol.canPlaceFlowers([1,0,0,0,1], 1), true)
//        XCTAssertEqual(sol.canPlaceFlowers([1,0,0,0,1], 2), false)
//        XCTAssertEqual(sol.canPlaceFlowers([0,0,1,0,0], 1), true)
        XCTAssertEqual(sol.canPlaceFlowers([0,0,0,0,0,1,0,0], 0), true)
    }

}
