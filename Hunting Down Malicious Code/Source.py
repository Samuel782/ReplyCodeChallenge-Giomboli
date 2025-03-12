def read_input_file(file_path):
    with open(file_path, 'r') as file:
        # Read number of test cases
        C = int(file.readline().strip())  # First line is the number of test cases
        test_cases = []

        # Iterate through each test case
        for _ in range(C):
            # Read the number of logs for the current test case
            Ni = int(file.readline().strip())
            logs = []

            # Read the Ni lines of logs
            for _ in range(Ni):
                log = file.readline().strip()
                logs.append(log)

            # Append the test case (Ni and the corresponding logs)
            test_cases.append((Ni, logs))

    return test_cases

# Example usage
input_file = 'input.txt'  # Replace with the path to your input file
test_cases = read_input_file(input_file)

# Printing the parsed test cases for validation
for idx, (Ni, logs) in enumerate(test_cases):
    print(f"Test Case {idx+1}:")
    print(f"Number of logs: {Ni}")
    for log in logs:
        print(f"  {log}")
