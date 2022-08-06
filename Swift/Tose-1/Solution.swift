//
//  Solution.swift
//  Tose-1
//
//  Created by 송태환 on 2022/08/06.
//

import Foundation

// 시간, 작성자, 메시지
// 1. 같은 분 단위면 메시지 묶기
// 2. 다른 날짜 판별 및 구분선 추가

func solution(_ messages:[[String]]) -> [String] {
	guard messages.count != 0 else { return [] }

	let dateFormatter = DateFormatter()
	let dateFormatterForDateComparison = DateFormatter()
	let inputDateFormatter = DateFormatter()
	let outputDateFormatter = DateFormatter()

	dateFormatterForDateComparison.timeZone = TimeZone(abbreviation: "UTC")
	dateFormatterForDateComparison.dateFormat = "yyyy-MM-dd'T'HH:mm"

	inputDateFormatter.timeZone = TimeZone(abbreviation: "UTC")
	inputDateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"

	outputDateFormatter.timeZone = TimeZone(abbreviation: "UTC")
	outputDateFormatter.dateFormat = "(HH:mm)"

	dateFormatter.dateFormat = "YYYY-MM-dd"

	var result: [String] = []
	var author = ""
	var date = inputDateFormatter.date(from: messages.first!.first!)!

	for i in 0..<messages.count {
		let data = messages[i]
		let currentMessageDate = inputDateFormatter.date(from: data[0])!
		let prevDay = dateFormatter.string(from: date).components(separatedBy: "-")
		let currentDay = dateFormatter.string(from: currentMessageDate).components(separatedBy: "-")

		print(date, currentMessageDate)
		print(prevDay, currentDay)

		if prevDay != currentDay {
			result.append("-- \(dateFormatter.string(from: currentMessageDate)) --")
			date = currentMessageDate
		}

		if author != data[1] {
			result.append("[\(data[1])]")
			author = data[1]
		}

		if data[2] == "" {
			result.append("<삭제된 메시지>")
		} else {
			result.append(data[2])
		}

		let previousMessageDateString = dateFormatterForDateComparison.string(from: date)
		let currentMessageDateString = dateFormatterForDateComparison.string(from: currentMessageDate)

		if previousMessageDateString != currentMessageDateString {
			let dateForEndOfMessage = outputDateFormatter.string(from: currentMessageDate)
			result.append(dateForEndOfMessage)
			date = currentMessageDate
		}
	}

	print(result)

	return result
}
