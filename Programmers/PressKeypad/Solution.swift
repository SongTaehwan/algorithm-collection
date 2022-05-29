//
//  Solution.swift
//  PressKeypad
//
//  Created by 송태환 on 2022/05/29.
//

import Foundation

func countDistance(start: Int, destination: Int) -> Int {
	let keyPad = [
		[1,2,3],
		[4,5,6],
		[7,8,9],
		[-1,0,-2]
	]

	var startPosition = [0,0]
	var destinationPosition = [0,0]

	for i in 0...3 {
		for j in 0...2 {
			if start == keyPad[i][j] {
				startPosition[0] = i
				startPosition[1] = j
			}

			if destination == keyPad[i][j] {
				destinationPosition[0] = i
				destinationPosition[1] = j
			}
		}
	}

	var count = 0

	for i in 0...1 {
		count += startPosition[i] > destinationPosition[i] ? startPosition[i] - destinationPosition[i] : destinationPosition[i] - startPosition[i]
	}

	return count
}

func solution(_ numbers:[Int], _ hand:String) -> String {
	var result = ""
	var left = -1
	var right = -2

	for number in numbers {
		switch number {
		case 1,4,7:
			left = number
			result += "L"
			break
		case 3,6,9:
			right = number
			result += "R"
			break
		default:
			let countForLeft = countDistance(start: left, destination: number)
			let countForRight = countDistance(start: right, destination: number)

			if countForLeft == countForRight {
				if hand == "left" {
					left = number
					result += "L"
				} else {
					right = number
					result += "R"
				}

				break
			}

			if countForLeft < countForRight {
				left = number
				result += "L"
			} else {
				right = number
				result += "R"
			}

			break
		}
	}

	return result
}

func solution1(_ numbers:[Int], _ hand:String) -> String {
	var result = ""

	let keyPad = [
		[1,4,7,0],
		[2,5,8,0],
		[3,6,9,0]
	]

	var left = (row: 0, index: 3)
	var right = (row: 2, index: 3)

	for number in numbers {
		if number > 0 && number % 3 == 0 {
			result += "R"
			right.row = 2
			right.index = (number / 3) - 1
		} else if number > 0 && number % 3 == 1 {
			result += "L"
			left.row = 0
			left.index = (number - 1) / 3
		} else {
			let rowIndex = 1
			let row = keyPad[rowIndex]
			let index = row.firstIndex(of: number)!

			let (leftRowIndex, leftIndex) = left
			let (rightRowIndex, rightIndex) = right

			let leftOffset = rowIndex != leftRowIndex ? 1 : 0
			let rightOffset = rowIndex != rightRowIndex ? 1 : 0
			let distanceFromLeft = abs(abs(index - leftIndex) + leftOffset)
			let distanceFromRight = abs(abs(index - rightIndex) + rightOffset)

			if distanceFromLeft < distanceFromRight {
				result += "L"
				left.row = rowIndex
				left.index = index
			} else if distanceFromLeft > distanceFromRight {
				result += "R"
				right.row = rowIndex
				right.index = index
			} else if hand == "left" {
				result += "L"
				left.row = rowIndex
				left.index = index
			} else {
				result += "R"
				right.row = rowIndex
				right.index = index
			}
		}
	}

	return result
}
