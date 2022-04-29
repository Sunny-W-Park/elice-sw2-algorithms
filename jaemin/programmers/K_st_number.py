# K번째수
# PR 220429 JAEMIN
# AUTH 220429 JAEMIN
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    # return [sorted(array[round[0]-1:round[1]])[round[2]-1] for round in commands]# round 중첩리스트 내부 리스트

    result = list()
    for round in commands:
        start_index = round[0]-1
        end_index = round[1]-1
        select_index = round[2]-1
        
        splitted_list = array[start_index:end_index+1]
        sorted_list = sorted(splitted_list)
        
        answer = sorted_list[select_index] 
        result.append(answer)
    return result