import numpy as np


# Flatten any board into a single string
def flatten_board(x):
    return(str(x).replace(' ','').replace('\n',''))

# Encode any board to get its board state
def get_encoded_board(x):
    '''Must pass a flattened board'''
    num_squares = range(64)
    
    #Black Player Feature Vectors
    b_rook  = [1 if x[i]=='r' else 0 for i in num_squares]
    b_night = [1 if x[i]=='n' else 0 for i in num_squares]
    b_bish  = [1 if x[i]=='b' else 0 for i in num_squares]
    b_queen = [1 if x[i]=='q' else 0 for i in num_squares]
    b_king  = [1 if x[i]=='k' else 0 for i in num_squares]
    b_pawn  = [1 if x[i]=='p' else 0 for i in num_squares]
    b_value = [(sum(b_rook)*5 + sum(b_night)*3 + sum(b_bish)*3
           + sum(b_queen)*9 + sum(b_pawn)*1
          )]
    
    #White Player Feature Vectors
    w_rook  = [1 if x[i]=='R' else 0 for i in num_squares]
    w_night = [1 if x[i]=='N' else 0 for i in num_squares]
    w_bish  = [1 if x[i]=='B' else 0 for i in num_squares]
    w_queen = [1 if x[i]=='Q' else 0 for i in num_squares]
    w_king  = [1 if x[i]=='K' else 0 for i in num_squares]
    w_pawn  = [1 if x[i]=='P' else 0 for i in num_squares]
    w_value = [(sum(w_rook)*5 + sum(w_night)*3 + sum(w_bish)*3
           + sum(w_queen)*9 + sum(w_pawn)*1
          )]

    feature_list = (b_rook+b_night+b_bish+b_queen
                +b_king+b_pawn+w_rook+w_night+w_bish
                +w_queen+w_king+w_pawn+b_value+w_value)
    
    return(feature_list)




