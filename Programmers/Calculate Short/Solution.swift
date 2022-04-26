//
//  Solution.swift
//  Caulate Short
//
//  Created by 송태환 on 2022/04/26.
//

import Foundation

/// [Checkout the problem](https://programmers.co.kr/learn/courses/30/lessons/82612?language=swift)
func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64 {
	let sum = (1...count).reduce(into: 0) { $0 += price * $1 }
	return Int64(max(0, sum - money))
}

func refactor(_ price:Int, _ money:Int, _ count:Int) -> Int64 {
	let sum = price * (count * (count + 1) / 2)
	return Int64(max(0, sum - money))
}
