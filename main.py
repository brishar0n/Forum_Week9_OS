import sys

# Function to read requests from a file
def read_requests(file_name):
    with open(file_name, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

# First-Come, First-Served (FCFS) algorithm
def fcfs(initial_position, requests):
    head_position = initial_position
    total_movement = 0
    for request in requests:
        total_movement += abs(head_position - request)
        head_position = request
    return total_movement

# SCAN (Elevator) algorithm
def scan(initial_position, requests):
    requests.sort()
    head_position = initial_position
    total_movement = 0

    # Separate requests into two lists: left and right of the initial position
    left = [r for r in requests if r < initial_position]
    right = [r for r in requests if r >= initial_position]

    # Move right first, then to the end, and then left
    for request in right:
        total_movement += abs(head_position - request)
        head_position = request
    if right:
        total_movement += abs(head_position - 4999)
        head_position = 4999
    for request in reversed(left):
        total_movement += abs(head_position - request)
        head_position = request

    return total_movement

# Circular SCAN (C-SCAN) algorithm
def c_scan(initial_position, requests):
    requests.sort()
    head_position = initial_position
    total_movement = 0

    # Separate requests into two lists: left and right of the initial position
    left = [r for r in requests if r < initial_position]
    right = [r for r in requests if r >= initial_position]

    # Move right, then to the end, jump to start, and move right again
    for request in right:
        total_movement += abs(head_position - request)
        head_position = request
    if right:
        total_movement += abs(head_position - 4999)
        total_movement += 4999  # Jump to the start
        head_position = 0
    for request in left:
        total_movement += abs(head_position - request)
        head_position = request

    return total_movement

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_position> <request_file>")
        return

    initial_position = int(sys.argv[1])
    request_file = sys.argv[2]
    requests = read_requests(request_file)

    fcfs_movement = fcfs(initial_position, requests)
    scan_movement = scan(initial_position, requests)
    c_scan_movement = c_scan(initial_position, requests)

    print(f"FCFS Total Head Movement: {fcfs_movement}")
    print(f"SCAN Total Head Movement: {scan_movement}")
    print(f"C-SCAN Total Head Movement: {c_scan_movement}")

if __name__ == "__main__":
    main()