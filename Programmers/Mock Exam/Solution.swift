//
//  Solution.swift
//  Reverse Bits
//
//  Created by 송태환 on 2022/01/19.
//

import Foundation

/// [Check out the problem](https://programmers.co.kr/learn/courses/30/lessons/42840)
func solution(_ answers:[Int]) -> [Int] {
    let examinee2 = [2,1,2,3,2,4,2,5]
    let examinee3 = [3,1,2,4,5]
    var dict = [Int: Int]()

    for (i, answer) in answers.enumerated() {
        if (i % 5) + 1 == answer {
            dict[1, default: 0] += 1
        }

        if examinee2[i % 8] == answer {
            dict[2, default: 0] += 1
        }

        if examinee3[(i/2) % 5]  == answer {
            dict[3, default: 0] += 1
        }
    }
    
    let maxValue = dict.values.max()
    return dict.filter { $0.value == maxValue }.keys.sorted()
}
