# Password Generator Using Python 3
import random
pass_char = 'ABCDEFGHUJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+<>?:"{}|,./;]["=-`'

print('Welcome to our Password generator system.')
def passwordGen(num):
    if num >= 1:
        len_pass = num
        pass_gen = ''.join(random.sample(pass_char, len_pass))
        print("your password is:", pass_gen)
        
num_e = int(input("Enter the num for passoword generator "))
passwordGen(num_e)

if num_e >= 1:
    while True:
        option = input('Would like to generate another password Y or N? ')

        if option == 'Y':
            def passwordGen(num):
                if num >= 1:
                    len_pass = num
                    pass_gen = ''.join(random.sample(pass_char, len_pass))
                    print("your password is:", pass_gen)
                elif num <= 0:
                    print("Please enter number greater than 1")

            n = int(input("Enter the length for passoword generator "))
            passwordGen(n)
        elif option == 'N':
            print("THANKYOU VISTI AGAIN")
            break
else:
  print("Number Should be greater than 1")
  while True:
      option = input('Would like to generate another password Y or N? ')

      if option == 'Y':
          def passwordGen(num):
              if num >= 1:
                  len_pass = num
                  pass_gen = ''.join(random.sample(pass_char, len_pass))
                  print("your password is:", pass_gen)
              elif num <= 0:
                  print("Please enter number greater than 1")

          n = int(input("Enter the length for passoword generator "))
          passwordGen(n)
      elif option == 'N':
          print("THANKYOU VISTI AGAIN")
          break
