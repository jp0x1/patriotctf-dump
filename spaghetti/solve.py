from z3 import *

# Initialize Z3 solver
solver = Solver()

# Define the Fibonacci sequence up to the 14th element (15 elements total)
fib = [BitVec(f'fib_{i}', 64) for i in range(15)]

# Add Fibonacci constraints
solver.add(fib[0] == 0)
solver.add(fib[1] == 1)
for i in range(2, 15):
    solver.add(fib[i] == fib[i-1] + fib[i-2])

# Ensure the solver checks for a solution
if solver.check() == sat:
    model = solver.model()

    # Retrieve the Fibonacci values
    fib_values = [model.eval(fib[i]).as_long() for i in range(15)]

    # Convert Fibonacci values to strings and concatenate them
    fib_str = ''.join(map(str, fib_values))

    # Final flag format with "ITALY_" and Fibonacci concatenation
    flag = f"PCTF{{ITALY_{fib_str}}}"

    print("Flag found:", flag)
else:
    print("No solution found.")
