# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
# if message != 'quit':
#  print(message)

    # At 1, we define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit'). Then we set
# up a variable message 2 to store whatever value the user enters. We define
# message as an empty string, "", so Python has something to check the first
# time it reaches the while line. The first time the program runs and Python
# reaches the while statement, it needs to compare the value of message to
# 'quit', but no user input has been entered yet. If Python has nothing to
# compare, it won’t be able to continue running the program. To solve this
# problem, we make sure to give message an initial value. Although it’s just an
# empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work. This while loop 3 runs as long as
# the value of message is not 'quit'.
# The first time through the loop, message is just an empty string, so Python
# enters the loop. At message = input(prompt), Python displays the prompt and
# waits for the user to enter their input. Whatever they enter is stored in message
# and printed; then, Python reevaluates the condition in the while statement.
# As long as the user has not entered the word 'quit', the prompt is displayed
# again and Python waits for more input. When the user finally enters 'quit',
# Python stops executing the while loop and the program ends

# flag fuction
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print(message)

# We set the variable active to True u so the program starts in an active
# state. Doing so makes the while statement simpler because no comparison is
# made in the while statement itself; the logic is taken care of in other parts of
# the program. As long as the active variable remains True, the loop will continue running v.
# In the if statement inside the while loop, we check the value of message
# once the user enters their input. If the user enters 'quit' w, we set active
# to False, and the while loop stops. If the user enters anything other than
# 'quit' x, we print their input as a message.
# This program has the same output as the previous example where we
# placed the conditional test directly in the while statement. But now that we
# have a flag to indicate whether the overall program is in an active state, it
# would be easy to add more tests (such as elif statements) for events that
# should cause active to become False. This is useful in complicated programs
# like games in which there may be many events that should each make the
# program stop running. When any of these events causes the active flag to
# become False, the main game loop will exit, a Game Over message can be
# displayed, and the player can be given the option to play again