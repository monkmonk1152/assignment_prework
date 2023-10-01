# question_1

 def hello_user(user.name)
""" Greet user"""
 user_name = "monkmonk"
 print(" Hello" + user_name + " , "Welcome to coding")
hello_user

# question_2
 def first_odds():
     '''print odd numbers'''
 for odds in range(1, 101):
          if odds % 2 == 1:
                 print(odds)

# Question 3
 
 numbers = [5, 10, 3, 8, 2, 88, 109, 12654, 74, 12, 1006, 998]
 max_number = numbers
 print(max(numbers))

# question 4 
 def is_leap_year(year):
    if year % 4 == 0:
         if year % 100 == 0:
             if year % 400 == 0:
                 return True
             else:
                 return False
         else:
             return True
    else:
         return False
 print(is_leap_year(2023))
 print(is_leap_year(1980))
 print(is_leap_year(2004))
 print(is_leap_year(2017))

# question 5
def is_consecutive(a_list):
 sorted_list = sorted(a_list)
 for i in range(len(sorted_list) - 1):
        if sorted_list[i+1] - sorted_list[i] != 1:
            return False
        return True
numbers = [12, 13, 14, 15, 16, 17]
result = is_consecutive(numbers)
print(result)

numbers = [71, 22, 4, 15]
result = is_consecutive(numbers)
print(result)
