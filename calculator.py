while True:
  user_input_1 = float(input('enter a first number: '))
  user_input_2 = float(input('enter a second number: '))

  user_calculation = input("""
  Enter a calculation
  + for addition
  - for substraction
  * for multiplication
  / for division
  """)

  if user_calculation == "+" :
   print(f"sum = {user_input_1 + user_input_2}")
  elif user_calculation == "-" : #put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
   print(f"difference = {user_input_1 - user_input_2}")
  elif user_calculation == "*" :
    print(f"multipication = {user_input_1 * user_input_2}")
  elif user_calculation == "/" :
   print(f"division = {user_input_1 / user_input_2}")
  else:
    print("invalid input")