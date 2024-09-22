class EmojiStack:
    def __init__(self):
        self.cells = [0] * 256  # Initialize 256 cells
        self.pointer = 0  # Start with the pointer at the first cell

    def move_right(self):
        self.pointer = (self.pointer + 1) % 256

    def move_left(self):
        self.pointer = (self.pointer - 1) % 256

    def increment(self):
        self.cells[self.pointer] = (self.cells[self.pointer] + 1) % 256

    def decrement(self):
        self.cells[self.pointer] = (self.cells[self.pointer] - 1) % 256

    def print_ascii(self):
        print(chr(self.cells[self.pointer]), end='')

    def execute(self, instructions):
        i = 0
        while i < len(instructions):
            instruction = instructions[i]

            if instruction == "👉":
                self.move_right()
            elif instruction == "👈":
                self.move_left()
            elif instruction == "👍":
                self.increment()
            elif instruction == "👎":
                self.decrement()
            elif instruction == "💬":
                self.print_ascii()
            elif instruction.startswith("🔁"):
                # Extract the number of repetitions
                j = i + 1
                while j < len(instructions) and instructions[j].isdigit():
                    j += 1
                num = int(instructions[i + 1:j], 16)  # Convert the collected digits
                last_instruction = instructions[i - 1]

                for _ in range(num):
                    if last_instruction == "👉":
                        self.move_right()
                    elif last_instruction == "👈":
                        self.move_left()
                    elif last_instruction == "👍":
                        self.increment()
                    elif last_instruction == "👎":
                        self.decrement()
                    elif last_instruction == "💬":
                        self.print_ascii()

                # Skip to the end of the number
                i = j - 1  # -1 because we will increment i at the end

            i += 1  # Move to the next instruction

# Example emoji sequence
instructions = (
    "👉👉👉👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁08👍🔁34👈👈👈👈👈👈👈👈👈"
    "👈👍🔁48👉🔁15👍🔁5e👈🔁07👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍"
    "👍👍👉🔁02👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁02👍👍👍"
    "👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁04👍🔁5e"
    "👉👉👉👉👉👉👉👉👍🔁47👈🔁0f👍🔁46👉👉👉👉👉👉👉👉👉👉👉👉👉"
    "👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉"
)

# Create an instance of the EmojiStack and execute the instructions
emoji_stack = EmojiStack()
emoji_stack.execute(instructions)
