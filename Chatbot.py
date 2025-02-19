import random

print("Hi ! have a good day. How can I help you today\n")
name=input("What's your name\n")
in_p =input("say hi to start a chat or press exit to end the chat\n")

if in_p=="hi":
    response_=input("What can I help you with Tv shows recommendation or coding projects in python\n"
                    ).lower()

    if response_=="Tv shows":
        show_list=["Shameless","Young Sheldon","Suits"]
        show_response=random.choice(show_list)
        print(f"I recommend you watching {show_response}")

    elif response_=="coding projects":
        coding_pro=["ChatBot","Hangman Game","Treasure Hunt Game"]
        code_response=random.choice(coding_pro)
        print(f"You should start with {code_response}")

    











else:
    print(f"Have a good day, Bye {name}")



