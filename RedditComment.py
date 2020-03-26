import praw

def bot_login():
             r = praw.Reddit(client_id='ougxKi-FzIOTPQ',
                     client_secret='ThKbnVIp-xWzDxgQA0Rer-tFcDY',
                     user_agent='/u/f_amin_2',
                     password="Hamburg040",
                     username="f_amin_2")
             return r

def run_bot(r):
    links_list=[]
    for comment in r.subreddit('all').comments(limit=25):
        if "u/f_amin_2" in comment.body:
            print ("Gefunden")
            comment_body="u/f_amin_2 u/_1234: Hallo"
            username=comment_body.replace("u/f_amin_2", "")
            username=username.split(":",1)[0].lstrip()
            term=comment_body.replace("u/f_amin_2", "")
            term=comment_body.split(":")[1].lstrip()
            for submission in reddit.redditor(username).comments.top("all"):
                if term in comment_body:
                    links_list.append("https://www.reddit.com/r/" + str(comment.subreddit) + "/comments/" + comment.link_id[3:])
                    x=x+1
            if x.equals(0):
                comment.reply("Thank you for your request.\n"+username+"never said"+term+".\n______________________________________________________________\n^Feedback? ^Go ^to ^r/CommentHistoryCheck")
            if x.equals(1):
                comment.reply("Thank you for your request.\n"+username+"said"+term+"once. Here is the link:\n"+links_list+"\n_________________________________________________________________\n^Feedback? ^Go ^to ^r/CommentHistoryCheck")
            else:
                comment.reply("Thank you for your request.\n"+username+"said"+term+x+"-times. Here are the links:\n"+links_list+"\n_________________________________________________________________\n^Feedback? ^Go ^to ^r/CommentHistoryCheck")
r = bot_login()
run_bot(r)