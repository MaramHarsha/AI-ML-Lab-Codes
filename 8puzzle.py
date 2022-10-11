def print_f(matrix):
    for i in range(9):
        if i%3 == 0 and i > 0:7

        
        print("")
        
        print(str(matrix[i])+" ", end ="")
 
def count(s):
    c = 0
    goal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]

    for i in range(9):
        if s[i] != 0 and s[i] != goal[i]:
            c += 1
            
   
    return c
 
def move(ar, p, st):
    rh = 9999
    
    store_st = st.copy()
    
    for i in range(len(ar)):
        
        dupl_st = st.copy()
        
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = 0
        
        tmp_rh = count(dupl_st)
        
        if tmp_rh < rh:
            rh = tmp_rh
            store_st = dupl_st.copy()
      
    return store_st, rh

initial = [1, 2, 3, 
         0, 5, 6,
         4, 7, 8]
 
h = count(initial)

Level = 1
 
print_f(initial)
print("\n*********")
 
while h>0:
    pos = int(initial.index(0))
    
    Level += 1
   
    if pos == 0:
        arr = [1, 3]
        initial, h = move(arr, pos, initial)
        
    elif pos == 1:
        arr = [0, 2, 4]
        initial, h = move(arr, pos, initial)
        
    elif pos==2:
        arr = [1, 5]
        initial, h = move(arr, pos, initial)
        
    elif pos==3:
        arr = [0, 4, 6]
        initial, h = move(arr, pos, initial)
        
    elif pos==4:
        arr = [1, 3, 5, 7]
        initial, h = move(arr, pos, initial)
        
    elif pos==5:
        arr = [2, 4, 8]
        initial, h = move(arr, pos, initial)
        
    elif pos==6:
        arr = [3, 7]
        initial, h = move(arr, pos, initial)
        
    elif pos==7:
        arr = [4, 6, 8]
        initial, h = move(arr, pos, initial)
        

    elif pos==8:
        arr = [5, 6]
        initial, h = move(arr, pos, initial)
    
   
    print_f(initial)
    print("\n ********")
