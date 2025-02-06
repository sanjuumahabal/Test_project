import os

num1 = int(os.getenv("NUM1", 0))  # Default value is 0 if NUM1 is not set
num2 = int(os.getenv("NUM2", 0))  # Default value is 0 if NUM2 is not set

print(f"Sum: {num1 + num2}")
