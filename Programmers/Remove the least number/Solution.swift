//
//  Solution.swift
//  Remove the least number
//
//  Created by 송태환 on 2022/05/30.
//

import Foundation

func solution(_ arr:[Int]) -> [Int] {
	let min = arr.sorted(by: <).first!
	return arr.count == 1 ? [-1] : arr.compactMap { $0 != min ? $0 : nil }
}
