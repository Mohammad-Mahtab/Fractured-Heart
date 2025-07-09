
dialog_tree_1 = {
    "start": {
        "text": "AHHHHHH! I HAVE NO MONEY PLEASE DONT HURT ME",
        "choices": {
            "Sir Calm down! I've been sent here to help you!": "help",
            "I will be leaving then": "final"
        }
    },
    "help": {
        "text": " AAAAA- oh [clears throat]  Pardon me for my theatrics right then, I was simply practicing for my audition as a damsel in distress #25. ",
        "choices": {
            "Right ! ": "next",
            "......": "next"
        }
    },
    "next": {
        "text": " Anyways, you must be the one who the guild sent to help retrieve the holy relic, right?",
        "choices": {
            "Yes, what exactly happened to the relic?": "relic",
            "No, I'm just a passing adventurer": "final"
        }
    },
    "relic": {
        "text": "We were just transporting the relic to a museum for a temporary exhibit but the wagon was ambushed by a bunch of plants!",
        "choices": {
            "I am so sorry to hear that": "sorry",
            " always knew that the vegetarians were onto something.": "sorry"
        }
    },
    "sorry": {
        "text": "Well yes. But there is good news however. During the ambush, the relic was dropped so we still have half the relic",
        "choices": {
            "Thats somewhat great.": "great",
            "What happened to the other half? ": "great"
        }
    },
    "great": {
        "text": "Those darn forest creatures made off with the other half though.",
        "choices": {
            "where can I find this relic?": "where",
            "Thank you very much ! I will find them !!": "final"
        }
    },
    "where": {
        "text": "The last I saw them , They were leading down south. I am pretty sure you can trace them down this path. I also remember a scout group following them . ",
        "choices": {
            "How does that scout look like or where would they even be? !": "scout",
            "Oh...you dont even know where they are? Fine ig thanks.": "final"
        }
    },
    "scout": {
        "text": "The leader of a group is girl dressed in red. I think her name is s.s.ssseryeh. Also , There is a scout base in the snow and its an igloo. ",
        "choices": {
            " I will get to that scout right away!": "final",
            " I will scout myself and then when i feel like it , i will find her. ": "final"
        }
    },

    "final": {
        "text": "BEST OF LUCK ON YOUR JOURNEY !! Come to the show when you are around next time , I may be a damsel. ",
        "choices": {"Bye":"end"}
    },

    "end": {
        "text": "",
        "choices": {}
    }
}

dialog_tree_2 = {
    "start": {
        "text": "Identify yourself bandit!",
        "choices": {
            "Calm down leader, I was sent by your friend to help find the relic": "help",
            "I won't . Bye": "final"
        }
    },
    "help": {
        "text": "Oh, I see, glad you decided to help because the monsters are too strong for us.",
        "choices": {
            "What is this relic exactly ?": "relic_info",
            "What happened to your team ?": "team_info"
        }
    },
    "relic_info": {
        "text": "It's a heart of a mythical hero which turned into a gemstone after he died. They said that he once drank 20 beers in 15 minutes! ",
        "choices": {
            "He is so rad!": "beer_story",
            "Did he ever do anything other than irresponsible drinking?": "beer_story"
        }
    },
    "beer_story": {
        "text": "He is still very highly regarded here !!  ",
        "choices": {
            "Well, Did your team take care of the monsters?": "team_info",
            "Whats next then ?": "monsters_drawn"
        }
    },
    "team_info": {
        "text": "Sadly, Our team suffered massive casulaties and many died. I have somehow managed to take refuge in our base here",
        "choices": {
            "I am extremely sorry for your loss.": "monsters_drawn",
            "What do we do now ?": "monsters_drawn"
        }
    },
    "monsters_drawn": {
        "text": "I do not know where they went at all. But there is a cherry tree farmer opposite to the pond. That old man knows everything. He once knew where my crumble cookie was while i never told anyone about it.  ",
        "choices": {
            "oh...I will find him then .": "final",
            "Why don't you come along with me ?": "find_info"
        }
    },
    "find_info": {
        "text": "You see , I would give my life for my people . And i would be leading charge here and taking you to him. But I had some snow shavings earlier and now my stomach is having acidic snow blizzard.",
        "choices": {
            "I'll just leave ": "final",
            "Whoever made you a leader needs to submit an Autism test.": "final"
        }
    },
    "final": {
        "text": "Hope you bring that relic back !",
        "choices": {
            "Goodbye": "end"
        }
    },
    "end": {
        "text": "",
        "choices": {}
    }
}

dialog_tree_3 = {
    "start": {
        "text": " GOODDDDDD ISSS GOODDD!! YOU SAVED ME BOYYY !!!",
        "choices": {
            "yea....": "wounded",
            "Beat it old man ! I am not hearing you.":"final"
        }
    },
    "wounded": {
        "text": "*cough cough* THANKKK YOUUU SOO MUCCCHHHH !!! ",
        "choices": {
            "Your welcome but i don't have time for this !": "ambushed",
            "Well welll wellll , Wheres my reward at ?": "reward"
        }
    },
    "ambushed": {
        "text": "THATS RIGHTTT !!! ",
        "choices": {"Where did the monsters tak-- ":"son",
            "Tell me please ": "son"
        }
    },
    "reward": {
        "text": "YES ! I MUST REWARD YOU !!! BUTTTT BEFORE THAT , I NEED YOU TO DO SOMETHING URGENT !! ",
        "choices": {
            " What is it !! I will do it ! ": "son",
            " Whaaa ?? Gon make me work for saving your life gramps .": "son"
        }
    },
    "son": {
        "text": "THE MONSTERSSSSS AREE AFTERR MY SON !! THEY WERE CHASING HIMM ALL AROUNDD . I TOLD HIM TO RUN FAST AND GET TO THE BAMBOOSS AT THE END OF THIS TRAIL !  ",
        "choices": {
            " Sir I do not even know who your son is. I can no-": "who",
            " No wayyyy. Baiiiii": "final"
        }
    },
    "who": {
        "text": "He is Bob..... I forgot how he looks like.....WAIT HE DOESN'T LOOK !! HE DOESN'T HAVE AN EYE",
        "choices": {
            " Alright, I will try to find him": "final",
            " Yea . He is dead already . He is not surviving with one eye":"eye"
        }
    },

    "eye": {
        "text": "Let me tell you more about him , maybe you know him. ",
        "choices": {
            " No..Sir...No": "Final"
        }
    },
    "final": {
        "text": "NOO , Listen to meee ....",
        "choices": {
            "I will be on my way": "end"
        }
    },
    "end": {
        "text": "",
        "choices": {}
    }
}

dialog_tree_4 = {
    "start": {
        "text": " BAMBOOO BAMBOO BAMBOOOO , DAD SAID BAMBOOOOO.",
        "choices": {
            "Are you okay ?": "wounded",
            "Both dad and son are mental":"wounded"
        }
    },
    "wounded": {
        "text": "*cries* SOMEONEEEE FINALLYYYYY. ",
        "choices": {
            "Its fine now , dont worry": "ambushed",
            "Stop crying already.": "reward"
        }
    },
    "ambushed": {
        "text": "Is my dad alright ?!!  ",
        "choices": {
            "He is well and fine":"find",
            "Go find him yourself ! Tell me where the monsters at?": "find"
        }
    },
    "reward": {
        "text": "I am soo sorryyy !! I THOUGHT I WAS GOING TO DIE.  ",
        "choices": {
            " You are not going to die , but tbh with your one eye does it really matter.": "matter",
            " Quick now ! I am here to get rid of the monsters !": "find"
        }
    },
    "matter": {
        "text": " Hey.y.yyyy . My mom said I looked furiously amicable in the eye patch tho. ",
        "choices": {
            "Its fine ig . Where are the monsters now": "find",
        }
    },
    "find": {
        "text": "Okayyyy . The monsters grouped together and went north. I have lived here forever , so i know where they could have gone. ",
        "choices": {
            " Where ?": "where",
        }
    },

    "where": {
        "text": " There is a Big warehouse to the left of the bamboo forest up north. They most probably have kept the thing they were carrying in there. ",
        "choices": {
            "Nows the real deall ": "holiday",
            "Finally I will get the relic.":"holiday"
        }
    },
    "holiday": {
        "text": " Oh also , after you are done . My dads cherry forest is to the left of the warehouse . You can chill out there after this. ",
        "choices": {
            "You talk a lot ": "final",
            "Thank you":"holiday"
        }
    },
    
    "final": {
        "text": "Well goodluck now then.",
        "choices": {
            "Bye Bob": "end"
        }
    },
    "end": {
        "text": "",
        "choices": {}
    }
}





class DialogManager:
    def __init__(self, tree):
        self.tree = tree
        self.current_node = "start"

    def get_current_dialog(self):
        return self.tree[self.current_node]["text"]

    def get_choices(self):
        return self.tree[self.current_node]["choices"]

    def choose(self, choice):
        if choice in self.get_choices():
            self.current_node = self.get_choices()[choice]

    def is_end(self):
        return self.current_node == "end"

