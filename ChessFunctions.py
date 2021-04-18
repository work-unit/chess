#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
def get_encoded_board(x):
    num_squares = range(64)

    x = str(x).replace(' ','').replace('\n','')
    #Black Player Feature Vectors
    b_rook  = [1 if x[i]=='r' else 0 for i in num_squares]
    b_night = [1 if x[i]=='n' else 0 for i in num_squares]
    b_bish  = [1 if x[i]=='b' else 0 for i in num_squares]
    b_queen = [1 if x[i]=='q' else 0 for i in num_squares]
    b_king  = [1 if x[i]=='k' else 0 for i in num_squares]
    b_pawn  = [1 if x[i]=='p' else 0 for i in num_squares]

    #White Player Feature Vectors
    w_rook  = [1 if x[i]=='R' else 0 for i in num_squares]
    w_night = [1 if x[i]=='N' else 0 for i in num_squares]
    w_bish  = [1 if x[i]=='B' else 0 for i in num_squares]
    w_queen = [1 if x[i]=='Q' else 0 for i in num_squares]
    w_king  = [1 if x[i]=='K' else 0 for i in num_squares]
    w_pawn  = [1 if x[i]=='P' else 0 for i in num_squares]

    feature_list = np.array(b_rook+b_night+b_bish+b_queen
                +b_king+b_pawn+w_rook+w_night+w_bish
                +w_queen+w_king+w_pawn).reshape([1,768])
    return(feature_list)


# In[ ]:




