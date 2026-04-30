# Function to implement FizzBuzz and count occurrences
def fizzbuzz_counter():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz", end=" ")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz", end=" ")
            buzz_count += 1
        else:
            print(i, end=" ")

    # Printing counts
    print("\n\n--- Counts ---")
    print("Fizz count:", fizz_count)
    print("Buzz count:", buzz_count)
    print("FizzBuzz count:", fizzbuzz_count)

# Calling the function
fizzbuzz_counter()