import random
import requests

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_link():    
    link = 'https://randomfox.ca/floof/'
    res = requests.get(link)
    data = res.json()
    return data['link']

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"
