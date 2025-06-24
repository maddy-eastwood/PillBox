<h1 style="text-align: center;"> PillBox</p>

<h3 style="text-align: center"> Welcome to PillBox! </h3>

**By: Madeleine Eastwood**

**Demo Video:** coming soon

**About:** Using just Python programming and the Pygame module, I reimagined a 2-player, vintage game from the 70's known as Pillbox.
During a conversation about our favorite games, a family friend of mine told me about how he used to play Pillbox. 
I recreated the game based on his description and the skills I learned in my physics and programming fundamentals
classes. This game utilizes projectile motion equations to model real-life trajectories in a pixel-based coordinate system. 

**How to play:** After clicking the start button, a simple playing field is randomly generated, containing a mountain
between two bases. The goal is to strategically choose an angle and speed with which to fire your bullet to accurately
hit the other player's base on the opposite side of the mountain. If you succeed, you gain 100 points, 
and a new playing field is automatically generated. Players take turns in firing their bullets, so part of the game is 
to remember why your bullet missed the last attempt and figure out how to alter its trajectory toward the base.
The first player to reach 1000 points can be considered the winner! However, the game will continue as usual as I 
wanted players to be able to determine how long they want to play. The Restart button will reset the entire game.

**How to run the code:** In this repo, click on the ` <> Code ` button and then select "Download ZIP".
To run this game, you just need pill_box_main.py, pill_box_classes.py, and to have Python and Pygame installed.
Once you've put the two Python files into a folder of your choosing, create a virtual environment by following these instructions:
1. Open your terminal or command-line interface
2. Navigate to the directory where you placed pill_box_main.py and pill_box_classes.py
3. To create a virtual environment, run this line: `python -m venv pb_venv` or `python3 -m venv pb_venv`
4. To activate the virtual environment, Mac users run: `source pb_venv/bin/activate` and Windows users run: `pb_venv\Scripts\activate`
5. Install dependency: `pip install -r requirements.txt`


**GUI Size:** On lines 8 and 9 in pill_box_main.py, you can edit the width and height of the GUI in pixels to fit your screen as you wish.