import random

def calculate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x ** 2 + y ** 2) <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples

if __name__ == "__main__":
    num_samples = 1000000  # Adjust this value based on your desired precision
    pi_approximation = calculate_pi(num_samples)
    print("Approximated value of pi:", pi_approximation)
