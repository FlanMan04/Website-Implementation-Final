import random
from pyscript import web, when, display

actions= ["rock", "paper", "scissors"]
opponent = ""

output_div = web.page["output"]


rock_img = "https://static.jojowiki.com/images/8/82/latest/20191015214548/Angelo_Rock_tourist_card.png"
paper_img = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzJ1MnNndDg4dDkxNmFrM3dobDkyaXJ4MDEyd2R3N2g2Mzloa2g5cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YTHKCCAa1AH4BMGtwu/giphy.gif"
scissors_img ="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/212_f2.png"

@when("click", "#Rock")
async def rock(event):
    opponent = random.choice(actions)

    if opponent == "rock" :
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center ; align-items:center; gap:30px;">
            <img src="{rock_img}" width="150">
            <h2>VS</h2>
            <img src="{rock_img}" width="150">
            <h2> You Tied </h2>
        </div>
        """
    elif opponent == "paper" :
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{rock_img}" width="150">
            <h2>VS</h2>
            <img src="{paper_img}" width="150">
            <h2> You Lost </h2>
        </div>
        """
    else : 
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{rock_img}" width="150">
            <h2>VS</h2>
            <img src="{scissors_img}" width="150">
            <h2> You Won </h2>
        </div>
        """

@when("click", "#Paper")
async def paper(event):
    opponent = random.choice(actions)
    if opponent == "paper" :
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{paper_img}" width="150">
            <h2>VS</h2>
            <img src="{paper_img}" width="150">
            <h2> You Tied </h2> 
        </div>
        """
    elif opponent == "scissors" :
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{paper_img}" width="150">
            <h2>VS</h2>
            <img src="{scissors_img}" width="150">
            <h2> You Lost </h2> 
        </div>
        """
    else : 
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{paper_img}" width="150">
            <h2>VS</h2>
            <img src="{rock_img}" width="150">      
            <h2> You Won </h2>
        </div>
  
        """
@when("click", "#Scissors")
async def scissors(event):
    opponent = random.choice(actions)
    if opponent == "scissors" :
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{scissors_img}" width="150">
            <h2>VS</h2>
            <img src="{scissors_img}" width="150">
            <h2> You Tied </h2>
        </div>
        """
    elif opponent == "rock" :
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{scissors_img}" width="150">
            <h2>VS</h2>
            <img src="{rock_img}" width="150">
            <h2> You Lost </h2>
        </div>
        """
    else : 
        output_div.innerHTML = f"""
        <div style="display:flex; justify-content: center; align-items:center; gap: 30px;">
            <img src="{scissors_img}" width="150">
            <h2>VS</h2>
            <img src="{paper_img}" width="150">
            <h2> You Won </h2>
        </div>
        """