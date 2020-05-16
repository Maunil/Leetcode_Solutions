class Solution:   
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letter = []
        
        for i in range(len(logs)):
            tokens = logs[i].split()
            
            if tokens[1].isdigit():
                digits.append(logs[i])
            else:
                letter.append(tokens)
        
        letter.sort(key = lambda letter: letter[0])
        letter.sort(key = lambda letter: letter[1:])
        
        for i in range(len(letter)):
            logs[i] = " ".join(letter[i])
        
        for i in range(len(digits)):
            logs[i + len(letter)] = digits[i]
            
        return logs 