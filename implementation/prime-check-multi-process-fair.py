#! /usr/bin/python3

import concurrent.futures
from threading import current_thread
from math import floor, sqrt
import time


def is_prime(number: int) -> bool:
    # print(current_thread().name)
    if not (number & 1): return 0

    iteration = floor(sqrt(number)) + 1
    for i in range(3, iteration, 2):
        if not (number % i): return 0
    return 1

def main() -> int:
    h_range = 1_000_000
    # h_range = 100
    start_time = time.time()
    max_workers = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(is_prime, number) for number in range(h_range + 1)}
        total_prime = 0
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


# ThreadPoolExecutor-0_0
# ThreadPoolExecutor-0_0
# ThreadPoolExecutor-0_0
# ThreadPoolExecutor-0_1
# ThreadPoolExecutor-0_2
# ThreadPoolExecutor-0_3
# ThreadPoolExecutor-0_1
# ThreadPoolExecutor-0_4
# ThreadPoolExecutor-0_0
# ThreadPoolExecutor-0_3
# ThreadPoolExecutor-0_1
# Total execution time is 0.003612995147705078 where count of primes is 4

