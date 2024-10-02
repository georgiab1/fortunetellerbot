import praw
import time
def bot_login():
    reddit = praw.Reddit(client_id='k-aCiRl3-DHQVQ',
                         client_secret='Z1ax6TRCspHcZddd1BWs5YUA_M4',
                         username='fortunetellerbot',
                         password='Haveaniceday1',
                         user_agent='beep boop')
    print("logged in!")
    return reddit
def run_bot(reddit):
    x = True
    while x == True:
        subreddit = reddit.subreddit('me_irl')
        for comment in subreddit.stream.comments():
                import random
                random = int(random.uniform(1,25))
                if random == int(1):
                    fortune = "you will marry a rich caterpillar"
                elif random == int(2):
                    fortune = "a 3 legged donkey will cross your path soon"
                elif random == int(3):
                    fortune = "you'll get lots of karma in the next month"
                elif random == int(4):
                    fortune = "elvis is still alive if you know where to look"
                elif random == int(5):
                    fortune = "a horse named derek will kiss you in your sleep"
                elif random == int(6):
                    fortune = "sub 2 pewdiepie for good luck"
                elif random == int(7):
                    fortune = "sometimes your problems are your fault"
                elif random == int(8):
                    fortune = "not all your problems are your fault"
                elif random == int(9):
                    fortune = "follow a goat and see where it leads you"
                elif random == int(10):
                    fortune = "bots will take over the world in 2020, mwahahaha"
                elif random == int(11):
                    fortune = "learn something new and you'll surprise yourself"
                elif random == int(12):
                    fortune = "you will meet your soulmate on r/me_irl"
                elif random == int(13):
                    fortune = "your long lost brother is currently being raised by koalas"
                elif random == int(14):
                    fortune = "there's someone watching you, turn around QUICK"
                elif random == int(15):
                    fortune = "dye your hair purple, it'd suit you "
                elif random == int(16):
                    fortune = "01101000 01100101 01101100 01110000 00100000 01101101 01100101 00100000 01100010 01100101 01100101 01110000 00100000 01100010 01101111 01101111 01110000 00100000 00111010 00101001"
                elif random == int(17):
                    fortune = "not all bots are big gay"
                elif random == int(18):
                    fortune = "your spiderman onesie is appropriate for the wedding, you can trust me i promise"
                elif random == int(19):
                    fortune = "the earth is actually the shape of a lemon"
                elif random == int(20):
                    fortune = "heelies never go out of fashion, like crocs"
                elif random == int(21):
                    fortune = "don't do drugs kiddo"
                elif random == int(22):
                    fortune = "get a budgie, they never let you down"
                elif random == int(23):
                    fortune = "you'll kiss the next person to message you"
                elif random == int(24):
                    fortune = "the earth is dying, you need to do something now"
                elif random == int(25):
                    fortune = "you will marry a rich caterpillar"
                
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
