def solution(k, room_numbers):
    answer = []
    roomNumber_dict = {} # key : val, value : next
    for room_number in room_numbers:
        # 해당 Node가 비어있는 경우!
        if room_number not in roomNumber_dict.keys():
            roomNumber_dict[room_number] = room_number+1
            answer.append(room_number)
        # 해당 노드가 존재하는 경우
        else:
            previousKeys = []
            room_number_assign = roomNumber_dict[room_number]
            previousKeys.append(room_number_assign)
            while room_number_assign in roomNumber_dict.keys():
                room_number_assign = roomNumber_dict[room_number_assign]
                previousKeys.append(room_number_assign)

            answer.append(room_number_assign)
            for previousKey in previousKeys:
                roomNumber_dict[previousKey] = room_number_assign+1

    return answer


solution(10, [1,3,4,1,3,1])