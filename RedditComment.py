import praw

def bot_login():
             reddit = praw.Reddit(client_id='ougxKi-FzIOTPQ',
                     client_secret='ThKbnVIp-xWzDxgQA0Rer-tFcDY',
                     user_agent='/u/CommentCheckBot',
                     password="Hamburg040",
                     username="CommentCheckBot")
             return reddit

def run_bot(r):
    links_list=[]
    for comment in r.subreddit('CommentCheckBot').comments(limit=None):
        if "u/CommentCheckBot" in comment.body:
            if not comment.saved:
                comment.save()
                kommentar=comment
                print("Gefunden")
                username=comment.body.replace("u/CommentCheckBot", "", 1)
                if "u/" in username:
                    username=username.replace("u/", "")
                    username=username.split(":",1)[0].lstrip()
                    print(username)
                    term=comment.body.replace("u/CommentCheckBot", "", 1)
                    term=term.replace(username, "")
                    term=term.replace("u/", "")
                    term=term.replace(" : ", "")
                    term=" "+term+" "
                    print(term)
                    for comment in reddit.redditor(username).comments.top(limit=None):
                        if term in comment.body:
                            links_list.append("https://www.reddit.com/r/" + str(comment.subreddit) + "/comments/" + comment.link_id[3:])
                            list_length=len(links_list)
                    if list_length == 0:
                        kommentar.reply("Thank you for your request.\n"+username+" didn't say"+str(term)+" in his top 1000 comments.\n______________________________________________________________\n^Feedback? Go to r/CommentHistoryCheck")
                        print("Done")
                    if list_length == 1:
                        print( ", ".join( repr(e) for e in links_list ) )
                        kommentar.reply("Thank you for your request.\nu/"+username+" said "+str(term)+" once. Here is the link:\n"+str(links_list)[1:-1]+"\n_________________________________________________________________\n^Feedback? Go to r/CommentCheckBot")
                        print("Done")
                        links_list.clear()
                    else:
                        print( ", ".join( repr(e) for e in links_list ) )
                        kommentar.reply("Thank you for your request.\nu/"+username+" said "+str(term)+" "+str(list_length)+" times. Here are the links:\n"+str(links_list)[1:-1]+"\n_________________________________________________________________\nFeedback? Go to r/CommentCheckBot")
                        print("Done")
                        links_list.clear()
            else:
                print("schon gemacht")

reddit = bot_login()
run_bot(reddit)
