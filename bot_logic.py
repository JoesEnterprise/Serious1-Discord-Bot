import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coinflip():
    num = random.randint(1,2)
    if num == 1 :
        return "Heads"
    else:
        return "Tails"
    
def roll_dice():
    return "the dice is", random.randint(1,6)

#def write(ctx, *, my_string: str):
    with open('text.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
        
#def read(ctx):
    with open('text.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        ctx.send(document)
        
#def min(ctx, left: int, right: int):
    """Adds two numbers together."""
    ctx.send(left - right)

#def times(ctx, left: int, right: int):
    """Adds two numbers together."""
    ctx.send(left*right)
    
#def divide(ctx, left: int, right: int):
    """Adds two numbers together."""
    ctx.send(left/right)
    
#def exp(ctx, left: int, right: int):
    """Adds two numbers together."""
    ctx.send(left**right)
    
#def add(ctx, *, my_string: str):
    with open('text.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)