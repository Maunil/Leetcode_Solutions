class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        first_s = ""
        second_s = ""
        counter = 0 
    
        for i in range(len(S) - 1,-1,-1):
            if S[i] == "#":
                counter = counter + 1 
            
            elif S[i] != "#" and counter == 0:
                first_s = str(S[i]) + first_s
        
            elif S[i] != "#":
                counter = counter - 1 
        
        counter = 0 
        
        for i in range(len(T) - 1,-1,-1):
            if T[i] == "#":
                counter = counter + 1 
            
            elif T[i] != "#" and counter == 0:
                second_s = str(T[i]) + second_s
        
            elif T[i] != "#":
                counter = counter - 1 
                
        
        if first_s == second_s:
            return True 
        
        return False
        