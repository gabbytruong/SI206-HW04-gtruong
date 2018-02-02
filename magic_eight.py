import random

reponses = [ "It is certain", "It is decidedly so", "Without a doubt", 
"Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", 
"Outlook good", "Yes", "Signs point to ye", "Reply hazy try again", 
"Ask again later", "Better not tell you now", "Cannot predict now", 
"Concentrate and ask again", "Don't count on it", "My reply is no", 
"My sources say no", "Outlook not so good", "Very doubtful" ]

question = ''

while question != "Quit":
    question = input("What is your question?")
    if question[-1] != "?" and question != "Quit":
        print("Sorry, I can only answer questions!")
    elif question[-1] == "?":
        print(random.choice(reponses))
        #print (responses[random.rantint(0, len(responses)-1)])
    elif question == 'Quit':
        break
        
