
shapemap_j1 = {
    'A' : 'rock',
    'B' : 'paper',
    'C' : 'scissors'
}

shapemap_j2 = {
    'X' : 'rock',
    'Y' : 'paper',
    'Z' : 'scissors'
}

shapemap_j2_reversed =  {v: k for k, v in shapemap_j2.items()}

scoremap_ending = {
    'X' : "loose",
    'Y' : "draw" ,
    'Z' : "win"
} 

scoremap_shape = {
    'rock' : 1,
    'paper' : 2,
    'scissors' : 3
}

# tuples ('A','B') with 'A' wins over 'B'
win_situations = [('rock','scissors'),('paper','rock'),('scissors','paper')]

def roundScore(j1,j2):
    shape_j1 = shapemap_j1[j1]
    shape_j2 = shapemap_j2[j2]
    score = scoremap_shape[shape_j2]
    if shape_j1 == shape_j2 : 
        score+=3
    elif (shape_j2,shape_j1) in win_situations:
        score+=6
    return score
    
def roundScoreWithJ2AsIndication(j1,j2):
    ending = scoremap_ending[j2]
    if ending == 'draw':
        return roundScore(j1,shapemap_j2_reversed[shapemap_j1[j1]])
    shape_j1 = shapemap_j1[j1]
    if ending == 'win':
        for (s1,s2) in win_situations:
            if s2 == shape_j1:
                return roundScore(j1,shapemap_j2_reversed[s1])
    elif ending == 'loose':
        for (s1,s2) in win_situations:
            if s1 == shape_j1:
                return roundScore(j1,shapemap_j2_reversed[s2])


f = open("inputday2.txt", "r")
score_total = 0
for s in f:
    j1 = ''
    j2 = ''
    for c in s:
        if c.isalpha():
            if j1=='':
                j1 = c
            else :
                j2 = c
    game_score = roundScoreWithJ2AsIndication(j1,j2) # part1 : roundScore(j1,j2)
    score_total += game_score

print(score_total)