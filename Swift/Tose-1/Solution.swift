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

func getDate(_ date: String, with format: String) -> String {
	let dateFormatter = DateFormatter()
	dateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"

	let dateObj = dateFormatter.date(from: date)!
	dateFormatter.dateFormat = format

	return dateFormatter.string(from: dateObj)
}

func solution(_ messages:[[String]]) -> [String] {
	guard messages.count != 0 else { return [] }

	let dateFormatter = DateFormatter()

	var result: [String] = []
	var previousSender = ""
	var previousDate = messages[0][0]

	for message in messages {
		guard message.count == 3 else { break }

		let date = message[0]
		let sender = message[1]
		let content = message[2]

		if sender != previousSender {
			if !previousSender.isEmpty {
				let dateTime = getDate(previousDate, with: "(HH:mm)")
				result.append(dateTime)
			}

			let prevDay = getDate(previousDate, with: "dd")
			let currentDay = getDate(date, with: "dd")

			if prevDay != currentDay {
				result.append(getDate(date, with: "-- yyyy-MM-dd --"))
			}

			result.append("[\(sender)]")
			previousSender = sender

		}

		result.append(content.isEmpty ? "<삭제된 메시지>" : content)

		previousDate = date
		previousSender = sender
	}

	result.append(getDate(messages[messages.count - 1][0], with: "(HH:mm)"))

	return result
}
