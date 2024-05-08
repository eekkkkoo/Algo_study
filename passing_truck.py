def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    weight_now = 0
    while bridge:
        weight_now -= bridge.pop(0)
        if truck_weights:
            if weight_now + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                weight_now += truck
            else:
                bridge.append(0)
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))