
find_message = lambda text: "".join(filter(str.isupper, text))

""" [sol 2]
find_message = lambda text:"".join(filter(lambda x : x.isupper(), text))
"""

""" [sol 1]
def find_message(text):
  msg = ""
  for i in text:
    if i.isupper():
      msg += i
  return msg
"""
if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
  assert find_message("hello world!") == "", "Nothing"
  assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
