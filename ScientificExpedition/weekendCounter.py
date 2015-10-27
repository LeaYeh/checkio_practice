from datetime import date
import datetime

def checkio(from_date, to_date):
  fd = date.toordinal(from_date)
  td = date.toordinal(to_date)
  count = sum(map(lambda x: date.isoweekday(date.fromordinal(x)) >= 6, 
                  range(fd, td + 1)))
  return count

""" [sol 2]
def checkio(from_date, to_date):
  td = datetime.timedelta(days=1)
  i = from_date
  count = 0
  while i <= to_date:
    if date.isoweekday(i) >= 6:
      count += 1
    i = i + td
  return count
"""
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
  assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
  assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
  assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

