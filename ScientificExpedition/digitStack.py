import re

def digit_stack(commands):
  stack, res = [], 0
  for command in commands:
    if command.startswith("PUSH"):
      stack.append(int(command.split()[1]))
    elif stack:
      res += stack[-1]
      if command == "POP":
        stack.pop()
  return res
""" [sol 1]
def digit_stack(commands):
  #map(lambda x: re.match("", x), commands)
  stack = []
  res = 0
  for command in commands:
    cmd = command.split()
    if cmd[0] == "PUSH":
      stack.append(int(cmd[1]))
    elif cmd[0] == "POP":
      res += stack.pop() if len(stack) else 0
    elif cmd[0] == "PEEK":
      res += stack[-1] if len(stack) else 0
  return res
"""
if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
            "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
  assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
  assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
  assert digit_stack([]) == 0, "Nothing"
