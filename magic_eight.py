import random

reponses = [ "It is certain", "It is decidedly so", "Without a doubt", 
"Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", 
"Outlook good", "Yes", "Signs point to ye", "Reply hazy try again", 
"Ask again later", "Better not tell you now", "Cannot predict now", 
"Concentrate and ask again", "Don't count on it", "My reply is no", 
"My sources say no", "Outlook not so good", "Very doubtful" ]



question = input("What is your question?")

if question == "Quit":
    break
elif question[-1] != "?":
    return ("Sorry, I can only answer questions!")
elif question = input("What is your question?"):
    print(random.choice(reponses))

