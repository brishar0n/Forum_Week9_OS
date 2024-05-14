import random

def generate_requests(file_name, num_requests, max_cylinder):
    requests = [random.randint(0, max_cylinder) for _ in range(num_requests)]
    with open(file_name, 'w') as file:
        for request in requests:
            file.write(f"{request}\n")

if __name__ == "__main__":
    generate_requests("requests.txt", 1000, 4999)
