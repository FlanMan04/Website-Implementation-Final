# Introduction
This is a repository containing all the work made for my Programming Languages Class from the "Recinto de Mayaguez". Here you will find 7 varying programs made with the express purpose of practicing and acquainting myself with 4 distinct programming paradigms and HTML/CSS.

Each paradigm brought its own sets of challanges, some mostly from setting them up and others from working with the syntax, oddly enough the hardest and most annoying hurdle was CSS styling.

# Instructions
This entire project is meant to run on a local host running on the project folder.
Locate yourself within the project folder and open a terminal and run the following command: On python I suggest using 'python -m http.server 8000' or alternatively if using JavaScript 'npx serve --port 8000'.

## Website Rundowns
- Turn-Based RPG  
Simple Role-Playing Game simulator written in TypeScript that has you select who in a party of 4 get to attack against a goblin. Everytime someone attacks, the goblin will at random, choose one character to attack and the party may have members die by having their health reduced to zero. If all members die, you lose. The objective is to reduce the opponent health to zero, which is not difficult at all.  
- JoJo Family Tree  
This is a family relations program written in Tau Prolog inspired by JoJo's Bizarre Adventure, known for having an extensive family tree. I was able to display parent, uncle, children, sibling relationships and some of their iterations. But not be able to properly display spouse to spouse relationships due to how complicated the family tree may be at times. Simply click on Character1 then on Character2 to find out what their relationship is. (ex. Jotaro and Jolyne, Dio and Shizuka, Jonathan and Joseph)
- Rock Paper Scissors  
Written in PyScript this is a simple Rock, Paper, Scissors program (was my first program in the project). You are met with 3 buttons labeled after the actions in the children's game. Once your selection is made, the program will automatically choose what is meant to counter your choice, with text that will indicate whether you won, lost, or tied. The Rock image is from JoJo's Bizarre Adventure, as well as the paper's option, and the Scissors option has a picture of Mega-Scizor from the pokemon franchise attached to it.
- CV Display
Written in PyScript, this is a rudimentary Curriculum Vitae manager that stores all your CV data directly in the browser's local storage (as JSON). It includes over ten categories (Personal, Work, Education, Skills, Languages, Certifications, Projects, Awards, Volunteering, Publications, References). You can add, edit, or delete entries at will, and each entry has a visibility toggle to show or hide it from the live resume. The resume preview updates instantly on the right side of the page, grouping visible entries by category. A "Download PDF" button uses html2pdf to capture that preview and save it as a PDF file. It's not the prettiest, but it gets the job done and everything stays in your browser.
- Factorial Calculator  
Probably the simplest in concept yet hardest to execute was my ClojureScript program that represents a calculator that only does factorials. Simply type or alternatively click the buttons on screen to see the factorial of the inputted number on screen (with a limit of up to 170, since anything larger does not compute). The program has a clear button and a delete button for freeing up the input slot.
- Clicker Game  
Written in PyScript, this is a simple clicker game fully inspired by Deltarune. Probably my best looking program, it features sprites, sounds, and music from Deltarune, a game I love. The objective is to click on the image of "Handsome Lancer" and you'll gain splats, of which you can buy splat multiplier bonuses with next to the shopkeeper, Seam. The audio of the program activates upon the first click of "Handsome Lancer". There is no end goal to the program, only to gain splats and spend splats, to gain even more splats.
- Tic-Tac-Toe  
Written in PyScript, the program alternates between Player X and O to fill a 3x3 grid, with the option to reset at any time. Players must click the grid they want to add their shape to. The program recognizes when their is a tie and a victor, it will then ask you to reset the board.

# Acknowlegments

JoJo's Bizarre Adventure
Created by: Hirohiko Araki.

Manga Publisher: Serialized by Shueisha (in Weekly Shōnen Jump) and published in North America by VIZ Media.

Copyright Holder: © LUCKY LAND COMMUNICATIONS / SHUEISHA. General Copyright: ©Hirohiko Araki & LUCKY LAND COMMUNICATIONS / SHUEISHA.

Anime Production Committee: The anime's copyright is held by the "JOJO's Animation SBR Project".

Official Website: jojo-portal.com.


Deltarune
Created by: Toby Fox.

Copyright & Trademark: © Toby Fox 2018-2021. DELTARUNE® is a trademark of Royal Sciences, LLC in the U.S..

Official Website: deltarune.com (Japanese site also available at deltarune.jp).


Pokémon
Original Copyright: © Nintendo / Creatures Inc. / GAME FREAK inc. from 1995 to present.

Management Company: The Pokémon Company (and internationally, The Pokémon Company International) manages the brand.

Trademark: "Pokémon," "Pokémon character names," "Nintendo Switch," are trademarks of Nintendo. In Japan, trademarks are also held by Creatures Inc. and GAME FREAK inc..

Official Website: pokemon.com.

The concepts of these programs were solely mine, elaboration of any codes and feedback was provided by [Kaizanor](github.com/Kaizanor) and []
For transparency, CSS styling was done with the help of AI and https://yoksel.github.io/flex-cheatsheet/
