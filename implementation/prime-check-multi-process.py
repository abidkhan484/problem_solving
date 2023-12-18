#! /usr/bin/python3

import concurrent.futures
from threading import current_thread
from math import floor, sqrt
import time

def is_prime(number: int) -> bool:
    if not (number & 1): return 0

    iteration = floor(sqrt(number)) + 1
    for i in range(3, iteration, 2):
        if not (number % i): return 0
    return 1

def prime_count_in_range_with_process_execution_time(start: int, end: int) -> int:
    start_time = time.time()
    total = sum(is_prime(number) for number in range(start, end+1))
    end_time = time.time()
    print(f"Execution time is {end_time - start_time} \
          where count of primes is {total}\
            and start {start} end {end}")

    return total

def main() -> int:
    max_workers = 10
    h_range = 10_000_000
    start_time = time.time()

    total_prime = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        difference = h_range // max_workers
        futures = {executor.submit(prime_count_in_range_with_process_execution_time, i*difference, (i+1)*difference) for i in range(max_workers)}

        for prime_count in concurrent.futures.as_completed(futures):
            try:
                total_prime += prime_count.result()
            except Exception as e:
                print(f"An error occurred: {e}")

    end_time = time.time()
    print(f"Total execution time is {end_time - start_time} \
            where count of primes is {total_prime}")

if __name__ == '__main__':
    main()


# Execution time is 13.428580284118652 where count of primes is 78498 and start 0 end 1000000
# Execution time is 20.32423686981201 where count of primes is 70435 and start 1000000 end 2000000
# Execution time is 25.322699308395386 where count of primes is 67883 and start 2000000 end 3000000
# Execution time is 27.458441495895386 where count of primes is 66330 and start 3000000 end 4000000
# Execution time is 29.976609706878662 where count of primes is 65367 and start 4000000 end 5000000
# Execution time is 31.90796446800232 where count of primes is 64336 and start 5000000 end 6000000
# Execution time is 32.69068694114685 where count of primes is 63799 and start 6000000 end 7000000
# Execution time is 34.158379316329956 where count of primes is 63129 and start 7000000 end 8000000
# Execution time is 34.51458287239075 where count of primes is 62712 and start 8000000 end 9000000
# Execution time is 35.21281599998474 where count of primes is 62090 and start 9000000 end 10000000
# Total execution time is 35.29995679855347 where count of primes is 664579



