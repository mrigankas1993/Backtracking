#Backtracking all permutations of a string
'''17 CS 106B lecture Backtracking permute a string stanford university lecture  python implementation'''
string = "MARS"
global var
var = []
def helperPermutation(string, choosen):
    if len(string) == 0:
        join = ''.join(choosen)
        var.append(join)
        return
    for j in range(len(string)):
        choosen.append(string[j])
        string_new  = string.pop(j)
        helperPermutation(string, choosen)
        # un choose
        string.insert(j, choosen[len(choosen) - 1])
        choosen.pop()
def permutation(c):
    choosen = []
    helperPermutation(c, choosen)
    return
c = list(string)
permutation(c)
print(var)



        
    
        
        
        
        
        



