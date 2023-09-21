"""Write a function that accepts a fight string consisting of only small letters and return
who wins the fight. When the left side wins, the Left side wins!, when the right side
wins, the Right side wins!, in other cases, Let's fight again!.
Left side letters
w - 4
p - 3
b - 2
s - 1
t - 0 (pretty word)
Right side letters
m - 4
q - 3
d - 2
z - 1
j - 0 (pretty word)
The other letters don't have power and are only victims.
The priest units t and j change the adjacent letters from hostile letters to friendly
letters with the same power.
alphabet_war("z") #=> "z" => "Right side wins!"
Explanation:
Letter z belongs to the right side letters and the left side has no letter so the right side
wins.
alphabet_war("tz") #=> "ts" => "Left side wins!"
Explanation:
Letter t is a pretty letter belonging to the left side. Pretty letters convert hostile letters
to friendly letters with the same power. Z is a hostile letter with power 1. T will convert
it to s a friendly letter with the same power.
"""

def fight_game(sentence):
    left_score = sum(4 if char == 'w' else 3 if char == 'p' else 2 if char == 'b' else 1 if char == 's' else 0 for char in sentence)
    right_score = sum(4 if char == 'm' else 3 if char == 'q' else 2 if char == 'd' else 1 if char == 'z' else 0 for char in sentence)
    
    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"

print(fight_game('ts'))
