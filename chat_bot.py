# This chatbot is a flirtbot that lets you flirt until you make the bot blush.

from random import choice

# Create a function called get_bot_response(). This function must:

# It should have 1 parameter called user_response, which is a string with the users input.

def get_bot_response(user_response):

    # It should return a string with the chat bot’s response.

    # It should use at least 2 lists to store at least 3 unique responses to different user inputs. For example, if you were building a mood bot and the user entered “happy” for how they were feeling your happy response list could store something like “I’m glad to hear that!”, “Yay!”, “That is awesome!”.

    bot_response_flirty = ["I really like your vibe! Maybe you'll make me blush. Wanna keep flirting it up with me, tiger? ",
                           "Aww, you're sweet! So, are you gonna ask me my real name, or are you gonna sit there all nervous, trying not to blow it? ", "You're cute! Do you like me? ", "You're adorable! How much do you like me? "]
    bot_response_blush = [
        "Congratulations, hot stuff! You finally made me blush! Type 'done' and I'm yours! ;) "]
    bot_response_unhappy = ["Then, come back when you grow a pair. Wanna keep trying? ", "Then, buzz off and find yourself another digital girlfriend! Type 'fin' so you can make like a tree and leave! ",
                            "Yeah, I'm gonna go. Come back after taking some flirting lessons. Type 'adios', so you can take a hike. ", "No, I don't want no scrub! I'm giving you one more chance. Are you better than that? "]
    bot_response_sassy = ["Wow! Nice try! Does that work on other bots, too? ", "You'll have to do better than that! Wanna keep trying, tiger? ;) ",
                          "Is that the best you can do? ", "Looks like someone needs some flirting lessons! ;) Wanna keep trying Rico Suave? "]
    bot_response_name = [
        "I'm Valentina, a.k.a. FlirtBot 2020! How interested are you in getting to know me? "]
    bot_response_unsure = ["Hmmm, I don't really know you that well, just yet. Keep flirting, and I'll think about it. How much do you like me?",
                           "Woah, slow down Speed Racer! You gotta warm up to me first! Wanna keep preheating the oven? ;)"]
    bot_response_bored = ["Aargh! Small talk is so BORING! Can't you tell I'm here to flirt with you? ",
                          "My plumber can carry a more interesting conversation than you. Wanna keep trying? "]
    bot_response_last = [
        "Well, you tried... unsuccessfully. But it's the effort that counts, right? Bye! :/"]

# Use conditionals to decide which of the response lists to select from. For example: if a user entered “sad”, my program would choose a reponse from the of sad response list. If a user entered “happy”, my program would choose a reponse from the of happy response list.
# Use choice() to randomly select one of the three responses. (See example from class.)

    if user_response == "Yes":
        return choice(bot_response_flirty)
    elif user_response == "No":
        return choice(bot_response_unhappy)
    elif user_response == "I'm not interested.":
        return choice(bot_response_sassy)
    elif user_response == "What's your name?":
        return choice(bot_response_name)
    elif user_response == "Will you go out with me?":
        return choice(bot_response_unsure)
    elif user_response == "I like you.":
        return choice(bot_response_blush)
    elif user_response == "How are you?":
        return choice(bot_response_bored)
    elif user_response == "A lot":
        return choice(bot_response_blush)
    elif user_response == "A little":
        return choice(bot_response_sassy)
    elif user_response == "Not much":
        return choice(bot_response_unhappy)
    elif user_response == "I don't like you":
        return choice(bot_response_unhappy)
    else:
        return choice(bot_response_last)

# Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.
print("Welcome to FlirtBot 2020! I'm your digital flirtmate!")

user_response = ""

# Get user input using the input() function and pass that user input to the get_bot_response() function you will write

# Print out the chat bot’s response that is returned from the get_bot_response() function

# Use a while() loop to keep running your chat bot until the user enters "done".

while True:
    user_response = input(
        "Think you have what it takes to make me blush? ;) ")
    if user_response == 'done':
        break

    bot_response = get_bot_response(user_response)
print(bot_response)