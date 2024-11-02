import praw
import time
import random
def bot_login():
    reddit = praw.Reddit(client_id='k-aCiRl3-DHQVQ',
                         client_secret='Z1ax6TRCspHcZddd1BWs5YUA_M4',
                         username='fortunetellerbot',
                         password='Haveaniceday1',
                         user_agent='beep boop')
    print("logged in!")
    return reddit
def run_bot(reddit):
    fortune_list = ["you will marry a rich caterpillar","a 3 legged donkey will cross your path soon","bots will take over the world in 2020, mwahahaha",
                    "elvis is still alive if you know where to look","don't do drugs, stay in school","get a budgie, they never let you down", "not all bots are bad :(",
                    "your spiderman onesie is appropriate for the wedding, you can trust me i promise","01101000 01100101 01101100 01110000 00100000 01101101 01100101 00100000 01100010 01100101 01100101 01110000 00100000 01100010 01101111 01101111 01110000 00100000 00111010 00101001",
                    "the earth is actually the shape of a lemon","heelies never go out of fashion, like crocs","the earth is dying in 3.... 2... 1... wait nevermind",
                    "a horse named derek will kiss you in your sleep","sub 2 pewdiepie for good luck", "sometimes your problems are your fault","not all your problems are your fault",
                    "follow a goat and see where it leads you","have a nice day!!","learn something new and you'll surprise yourself","you will meet your soulmate on a canoe",
                    "your long lost brother is being raised by koalas","there's someone watching you, turn around QUICK","not all bots are trying to take over the world... I am though >:)","dye your hair purple, it'd suit you "]
    x = True
    while x == True:
        subreddit = reddit.subreddit('me_irl')
        for comment in subreddit.stream.comments():
                random = int(random.uniform(0,24))
                fortune = fortune_list[random
                if "fortune teller" in comment.body:
                    print("script found")
                    comment.reply("beep boop your fortune is: '" + fortune + " ' if im being a bad bot, tag me to give feedback- fortunetellerbot :)")
                    print("fortune told")
                if "Fortune teller" in comment.body:
                    print("script found")
                    comment.reply("beep boop your fortune is: '" + fortune + " ' if im being a bad bot, tag me to give feedback- fortunetellerbot :)")
                    print("fortune told")
                elif "u/fortunetellerbot" in comment.body:
                    print("script found")
                    comment.reply("thanks for your feedback, i'll tag my creator so she can respond u/not_verycool")

reddit = bot_login()
run_bot(reddit)
