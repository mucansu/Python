import random

test_numbers = 100
min_num = 1
max_num = 100

# List to keep track of past secret numbers
past_secrets = []


def automated_guesser(secret_number):
    # Initialize the range
    low, high = min_num, max_num
    attempts = 0

    if past_secrets:
        guess = sum(past_secrets) // len(past_secrets)
    else:
        guess = (low + high) // 2

    while low <= high:
        attempts += 1

        if guess == secret_number:
            past_secrets.append(secret_number)  # update past secrets list
            return attempts, True
        elif guess < secret_number:
            low = guess + 1
        else:
            high = guess - 1

        guess = (low + high) // 2
    past_secrets.append(secret_number)
    return attempts, False


def test_guesser(test_numbers=test_numbers):
    successes = 0
    total_attempts = 0
    max_attempts = 0
    for _ in range(test_numbers):
        secret_number = random.randint(min_num, max_num)
        attempts, success = automated_guesser(secret_number)
        total_attempts += attempts
        if success:
            successes += 1
        if attempts > max_attempts:
            max_attempts = attempts
    avg_attempts = total_attempts / test_numbers
    success_rate = (successes / test_numbers) * 100

    print(f"Out of {test_numbers} tests:")
    print(f"Success Rate: {success_rate}%")
    print(f"Average Attempts Needed: {avg_attempts}")
    print(f"Max Attempts Needed: {max_attempts}")


test_guesser()
