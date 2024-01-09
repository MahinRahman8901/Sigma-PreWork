from datetime import date

def AgeCalculator(caclDate):
  days = 365.2425
  age = int((date.today() - caclDate).days / days)
  return age

print(AgeCalculator(date(2001, 8, 9)))
