def help(bot, prefix, cmds):
    bot.send_message("Registered commands: " + ", ".join(
        [f"{prefix}{cmd}" for cmd in sorted(cmds.keys())]
    ))


def hello(bot, user, *args):
    bot.send_message(f"Hey {user['name']}!!!")


def greet(bot, user, *args):
    if 'everyone' in args:
        message = f"Hello @everyone... Hope everyone having a great day and in good health..." \
                  f" A special thanks to @Vultplay for giving us this beautiful content and" \
                  f" a platform for these beautiful peoples... <3"
        bot.send_message(message)
    elif 'vult' in args:
        message = f"hi Vult... How are you today??? How is the day going so far?"
        bot.send_message(message)
    elif 'jackie' in args:
        message = f"hey Sensei... How are you??? ^_^"
        bot.send_message(message)
    elif 'cure' in args:
        message = f"hey @Curefitz ... HeyGuys HeyGuys HeyGuys"
        bot.send_message(message)
    elif 'diva' in args:
        message = f"Hello gorgeous @Divaa_Deluxe... Hope you are having a great day and in good health..." \
                  f"I'm Ami's assistant looking after your Agarita... Watering the plant as scheduled..."
        bot.send_message(message)
    elif 'blue' in args:
        message = f"Hey @Bluemanchew... Do you wanna hear the dabba da da ba de dabba song??? Go to YouTube!!! LUL LUL LUL"
        bot.send_message(message)
    else:
        message = f"hello... HeyGuys HeyGuys HeyGuys"
        bot.send_message(message)
