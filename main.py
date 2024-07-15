import sys

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
        
    return requests

def fcfs(initial_position, requests):
    head_position = initial_position
    total_movement = 0
    for request in requests:
        total_movement += abs(head_position - request)
        head_position = request
        
    return total_movement

def optimized_fcfs(initial_position, requests):
    return fcfs(initial_position, requests)

def scan(initial_position, requests, total_cylinders):
    requests.sort()
    total_movement = 0
    head_position = initial_position
    if (max(requests) - initial_position) < (initial_position - min(requests)):
        left_part = [r for r in requests if r <= initial_position]
        right_part = [r for r in requests if r > initial_position]
        for request in reversed(left_part):
            total_movement += abs(request - head_position)
            head_position = request
        if right_part:
            total_movement += head_position
            total_movement += right_part[0]
            head_position = right_part[0]
        for request in right_part:
            total_movement += abs(request - head_position)
            head_position = request
            
    else:
        left_part = [r for r in requests if r <= initial_position]
        right_part = [r for r in requests if r > initial_position]
        for request in right_part:
            total_movement += abs(request - head_position)
            head_position = request
        if left_part:
            total_movement += (total_cylinders - 1 - head_position)
            total_movement += (total_cylinders - 1 - left_part[-1])
            head_position = left_part[-1]
        for request in reversed(left_part):
            total_movement += abs(request - head_position)
            head_position = request
            
    return total_movement

def optimized_scan(initial_position, requests, total_cylinders):
    requests.sort()
    total_movement = 0
    head_position = initial_position
    left_part = [r for r in requests if r <= initial_position]
    right_part = [r for r in requests if r > initial_position]
    for request in reversed(left_part):
        total_movement += abs(request - head_position)
        head_position = request
    for request in right_part:
        total_movement += abs(request - head_position)
        head_position = request
        
    return total_movement

def cscan(requests, initial_position, total_cylinders):
    total_movement = 0
    head_position = initial_position

    requests_above = [req for req in requests if req >= initial_position]
    requests_below = [req for req in requests if req < initial_position]

    for request in requests_above:
        total_movement += abs(request - head_position)
        head_position = request

    if requests_below:
        total_movement += total_cylinders - 1 - head_position  
        total_movement += total_cylinders - 1  
        head_position = 0

        for request in requests_below:
            total_movement += abs(request - head_position)
            head_position = request

    return total_movement

def optimized_cscan(requests, initial_position, total_cylinders):
    requests.sort()
    total_movement = 0
    head_position = initial_position
    
    index = 0 
    while index < len(requests) and requests[index] < initial_position:
        index += 1
    
    for i in range(index, len(requests)):
        total_movement += abs(requests[i] - head_position)
        head_position = requests[i]

    if index > 0: 
        total_movement += total_cylinders - 1 - head_position 
        total_movement += total_cylinders - 1  
        head_position = 0
        for i in range(index):
            total_movement += abs(requests[i] - head_position)
            head_position = requests[i]

    return total_movement
    
def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <initial_position> <file_path> <total_cylinders>")
        return

    initial_position = int(sys.argv[1])
    file_path = sys.argv[2]
    total_cylinders = int(sys.argv[3])

    requests_initial = read_requests(file_path)
    
    print("Total head movements for FCFS:", fcfs(requests_initial[:], initial_position))
    print("Total head movements for SCAN:", scan(requests_initial[:], initial_position, total_cylinders))
    print("Total head movements for C-SCAN:", cscan(requests_initial[:], initial_position, total_cylinders))
    print("Total optimal head movements for FCFS:", fcfs(sorted(requests_initial[:]), initial_position))
    print("Total optimal head movements for SCAN:", optimized_scan(requests_initial, initial_position, total_cylinders))
    print("Total optimal head movements for C-SCAN:", optimized_cscan(requests_initial, initial_position, total_cylinders))

if __name__ == "__main__":
    main()
