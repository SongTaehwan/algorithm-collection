//
//  Tose_1.swift
//  Tose-1
//
//  Created by 송태환 on 2022/08/06.
//

import XCTest

class Tose_1: TestCase {
	func test() {
		let dateString = "2022-06-24T23:57:42"

		let inputFormatter = DateFormatter()
		inputFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
		inputFormatter.timeZone = TimeZone(abbreviation: "UTC")

		print(inputFormatter.date(from: dateString))

		let outputFormatter = DateFormatter()
		outputFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
		outputFormatter.timeZone = TimeZone(secondsFromGMT: 32400)
		print(outputFormatter.date(from: dateString))

		struct InstargramPost {
			let title: String = "제목"
			let description: String = "내용설명"
			private let date: Date = Date()

			var dateString: String {
				print(date)
				let formatter: DateFormatter = DateFormatter()
				formatter.locale = Locale(identifier: "ko_KR")
				//        formatter.dateFormat = "yyyy/MM/dd"
				formatter.dateStyle = .medium
				formatter.timeStyle = .full
				return formatter.string(from: self.date)
			}
		}

		print(InstargramPost().dateString)
	}

//	func testSolution() {
//		XCTAssertEqual(solution(
//		[
//			["2022-06-24T23:57:42", "정원", "민탁님"],
//			["2022-06-24T23:57:44", "정원", "생일이 얼마 안남으셨네요"],
//			["2022-06-24T23:57:54", "정원", "소감 한말씀 부탁드립니닼ㅋㅋㅋ"],
//			["2022-06-24T23:58:02", "금상", "오~ 민탁님 내일 생일이세요? 축하해요!"],
//			["2022-06-24T23:58:05", "민탁", "으악 감사해요 이렇게 늦은저녁까지 챙겨주시고ㅠㅠ!"],
//			["2022-06-24T23:58:34", "도현", "민탁님 축하드려요~~!"],
//			["2022-06-24T23:58:36", "도현", ""],
//			["2022-06-24T23:58:55", "금상", "민탁님"],
//			["2022-06-24T23:59:01", "금상", "생일기념 내일 뭐하시나요~"],
//			["2022-06-24T23:59:10", "정원", "가족과 여행?"],
//			["2022-06-24T23:59:12", "금상", "해외여행 가시는건가요!!"],
//			["2022-06-24T23:59:55", "민탁", "일주일쉬면서 가족하고 하와이갑니다~~ 축하감사해요 모두!"],
//			["2022-06-25T00:00:01", "정원", "이제 진짜 생일되셨네요!! 축하합니다!!"],
//			["2022-06-25T00:01:05", "민탁", ""]
//		]),
//		[
//			"[정원]",
//			"민탁님",
//			"생일이 얼마 안남으셨네요",
//			"소감 한말씀 부탁드립니닼ㅋㅋㅋ",
//			"(23:57)",
//			"[금상]",
//			"오~ 민탁님 내일 생일이세요? 축하해요!",
//			"(23:58)",
//			"[민탁]",
//			"으악 감사해요 이렇게 늦은저녁까지 챙겨주시고ㅠㅠ!",
//			"(23:58)",
//			"[도현]",
//			"민탁님 축하드려요~~!",
//			"<삭제된 메시지>",
//			"(23:58)",
//			"[금상]",
//			"민탁님",
//			"(23:58)",
//			"[금상]",
//			"생일기념 내일 뭐하시나요~",
//			"(23:59)",
//			"[정원]",
//			"가족과 여행?",
//			"(23:59)",
//			"[금상]",
//			"해외여행 가시는건가요!!",
//			"(23:59)",
//			"[민탁]",
//			"일주일쉬면서 가족하고 하와이갑니다~~ 축하감사해요 모두!",
//			"(23:59)",
//			"-- 2022-06-25 --",
//			"[정원]",
//			"이제 진짜 생일되셨네요!! 축하합니다!!",
//			"(00:00)",
//			"[민탁]",
//			"<삭제된 메시지>",
//			"(00:01)"
//		])
//	}
}

