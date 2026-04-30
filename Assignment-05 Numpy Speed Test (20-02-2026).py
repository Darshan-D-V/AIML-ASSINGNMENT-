import time
import numpy as np

# Create 1 million numbers
n = 1_000_000

# Python list
py_list = list(range(n))

# NumPy array
np_array = np.arange(n)

# --- Python List Operation (Squaring) ---
start = time.time()
py_result = [x**2 for x in py_list]
end = time.time()
py_time = end - start

# --- NumPy Array Operation (Squaring) ---
start = time.time()
np_result = np_array ** 2
end = time.time()
np_time = end - start

# Results
print("Python List Time:", py_time)
print("NumPy Array Time:", np_time)
print("Speed Difference:", py_time / np_time)