print("Welcome to my calculaor!")
print("Enter an expression like 5+3 or 10*2")
print("Press 0 to reset or e to exit")
Result=0
while True:
  expression=input("Enter an expression")
  if expression=="0":
    Result=0
    print("reset")
    continue
  elif expression=="e":
    print("Exit")
    break
  try:
    Result=float(eval(expression))
    print("Result:",Result)
  except:
    print("Error:Invalid Input!")
       
