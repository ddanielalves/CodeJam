import numpy as np
import sys
from scipy.special import expit, logit

getint = lambda: int(input())
getints = lambda: [int(a) for a in input().split()]
getm = lambda L: [[int(a) for a in input().split()] for l in range(L)]
outp = lambda i,r: print('Case #{}: {}'.format(i, r))

def solve():
    PLAYERS = 100
    QUESTIONS = 10_000 

    M = np.zeros((PLAYERS, QUESTIONS))
    
    for i in range(PLAYERS):
        line = input()
        aux = list(line)[:QUESTIONS]
        M[i, :] = aux
        
    prob = M.mean(axis = 0)
    difficulty = -logit(prob)

    prob = M.mean(axis = 1)
    skill = logit(prob)

    player_mask = prob > 0.5
    p_len = player_mask.sum()
    
    extreme_question_mask = difficulty > 1.7
    extreme_question_mask |= difficulty < -1.7
    q_len = extreme_question_mask.sum()
    
    probabilities = expit(skill[player_mask].reshape((p_len, 1)) - difficulty[extreme_question_mask].reshape(1,q_len))
    expected_result = np.sum(probabilities, axis = 1)
    
    expected_diff = np.abs(expected_result - M[player_mask][:, extreme_question_mask].sum(axis = 1))
    idx_masked = np.argmax(expected_diff)
    
    # Unmask
    idx_unmasked = np.where(player_mask)[0][idx_masked]
    
    return idx_unmasked + 1

    
if __name__ == "__main__":
    t = int(input())
    _ = input()
    for i in range(1, t+1):
        r = solve()
        outp(i,r)
        