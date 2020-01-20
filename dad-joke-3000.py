import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000")
header = colored(header, color="green")
print(header)

def search():
    user_input = input("\nWhat do you want to hear a dad joke about? ")
    jokes(user_input)
    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("\nDo you want to hear another? Y/N: ")
    if again.lower() in ('yes', 'y'):
        return search() #Calling yourself
    else:
        print("OK, GOODBYE!")

def jokes(user_input):
    url = "https://icanhazdadjoke.com/search"

    res = requests.get(
        url, 
        headers={"Accept": "application/json"},
        params={"term": user_input}
    ).json()

    num_jokes = res["total_jokes"]
    results = res["results"]

    if num_jokes > 1:
        print(f"\nI found {num_jokes} jokes! Here's a random one: ")
        print(colored(choice(results)["joke"], color="green"))
    elif num_jokes == 1:
        print("\nFound one joke! Here it is: ")
        print(colored(results[0]["joke"], color="green"))
    else:
        print(f"\nSorry, couldn't find a joke about {user_input}.")

#Running main game
search()
