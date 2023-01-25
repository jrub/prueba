def valor_de(x):
  return x

def divisible_por_3(x):
  if x % 3== 0:
    return True

def divisible_por_5(x):
  if x % 5== 0:
    return True

def divisible_3_5(x):
  if x % 3== 0 and x % 5== 0:
    return True

def fizzbuzzer(x):
    if divisible_3_5(x):
      return "FizzBuzz"
    if divisible_por_3(x):
      return "Fizz"
    if divisible_por_5(x):
      return "Buzz"
    return x

for x in range(1,101):
  print(fizzbuzzer(x))