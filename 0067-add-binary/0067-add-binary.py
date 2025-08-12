class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) >= len(b):
            longer = a
            smaller = b
        else:
            longer = b
            smaller = a
        
        rest = 0
        result = ""
        
        for i in range(len(longer)):
            #check if not the end
            sm_ix = len(smaller) - i - 1
            lg_ix = len(longer) - i - 1
            #make it 0 so it does not add more
            if(sm_ix < 0):
                sm_ix = 0
                smaller = "0"
            # 1 and 1      
            if int(smaller[sm_ix]) and int(longer[lg_ix]):
                result += str(rest)
                rest = 1
            # 1 and 0 or 0 and 1
            elif int(smaller[sm_ix]) or int(longer[lg_ix]):
                if rest == 1:
                    result += "0"
                    rest = 1
                else:
                    result += "1"
                    rest = 0
            # 0 and 0
            elif (int(smaller[sm_ix]) and int(longer[lg_ix])) == 0:
                result += str(rest)
                rest = 0
                
        result += str(rest)
        
        if result[::-1].lstrip('0') == "":
            return "0"
        else:
            return result[::-1].lstrip('0')