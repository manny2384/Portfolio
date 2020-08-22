import re
import random
class Bot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    def __init__(self):
        self.question = 'question'
        # list of intents to match questions from the user 
        self.myAnswers = {'describe_yourself': r'what.*are.*.you.*(like|interests|hobbies).*',
        'yes_intent': r'.*(yes|yeah|sure).*(\w+)?',
        'this_bot': r'.*what.*(type|programming|this).*bot.*',
        'skill_intent': r".*(your|what|tell).*(skills|programming|languages).*(you|.*)"
        }
        
    def greet(self):
        print('Start by greeting : ')

    def chat(self, question):
        print('you asked :' + question)
        question = question.lower()
        if(question in self.negative_responses):
            print('negative response: no need for further conversation')
            return 'Okay, Have a nice day'
        else:
            print('need to respond to ' + question)
            return self.match_reply(question) 
            
        

    def check(self):
        print('Bot class reached')

    def match_reply(self, question):
        for key, value in self.myAnswers.items():
            intent = key
            regex = value
            found_match = re.match(regex, question) #look for matching expression of question in regex
            print(intent + ' : ' + regex)

            # following return a random choice of responses based on intent found
            if(found_match and intent=='describe_yourself'): # if a match is found with describe_yourself intent
                print('Matched Intent ' + intent)
                return self.describe_intent()
            elif(found_match and intent == 'this_bot'):
                print('Matched Intent ' + intent)
                return self.this_bot()
            elif(found_match and intent == 'skill_intent'):
                print('Matched Intent ' + intent)
                return self.skill_intent()
            elif(found_match and intent == 'yes_intent'):
                print('Matched Intent ' + intent)
                return self.yes_intent()

        if not found_match: # if no match is found re-prompt for a question
            print("Sorry, I couldn't understand your question")
            return "Sorry, I couldn't understand your question"

    def describe_intent(self):
        responses = ("My name is Emmanuel and I'm a computer science student at Cal State East Bay. I hope to develope my skills in ML and AI.",
            "My name is Emmanuel and right now I'm trying to learn more about ML and AI",
            "My name is Emmanuel and I'm looking for an internship where I can learn more about ML and AI")
        return random.choice(responses)

    def this_bot(self):
        responses = ("I am a bot programmed in python using Rule based format along with libraries such as re",
            "I am a Rule-Based bot programmed in python. My creator is currently learning more about bots and flask in order to sophisticate me",
            )
        return random.choice(responses)

    def skill_intent(self):
        responses = ("Some of my skills are: C/C++, Java, HTML, CSS, JS, Python, React, Nodejs",
        "Most of my skills revolve around web-dev such as: React, NodeJs and MySQL.", 
        "Throughout my school career I've mostly programmed algorithms in Java or C++. I like to use web languages more for content creation",
        "I have a few projects that show some of my skills using React, Nodejs, MySQL, HTML and CSS. This portfolio consist of a mix of JS and python"+
        " along with flask for the backend.")
        return random.choice(responses)
    
    def yes_intent(self):
        responses = ("Great, what can I do for you?", "Awesome, what were you looking for?", 
        "Nice, Is there anything you want to know about me?")
        return random.choice(responses)