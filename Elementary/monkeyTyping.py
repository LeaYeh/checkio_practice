import re

count_words = lambda text, words: sum((i.lower() in text.lower()) for i in words)

""" [sol 3]
def count_words(text, words):
  return sum((i.lower() in text.lower()) for i in words)
"""
""" [sol 2]
  text = text.lower()
  count = 0
  for i in words:
    if re.search(i, text):
      count += 1
  return count
"""
""" [sol 1]
  record = {}
  for i in words:
    m = re.search(i, text, re.IGNORECASE)
    if m:
      if m.group() not in record:
        record[m.group()] = 1
  return len(record)
"""

if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
  assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
  assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
