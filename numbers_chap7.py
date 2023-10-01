# import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#     print(current_number)

# x = 1
# while x <= 5:
#  print(x)
#  x += 1

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
 current_user = unconfirmed_users.pop()
 print("Verifying user: " + current_user.title())
 confirmed_users.append(current_user)
 print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
 print(confirmed_user.title())
