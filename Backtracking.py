from verify import result,verification
#space complexity = O(n)
#time complexity = O(m^n)
import time
start = time.time()
searches = 0
def letterCombinations(digits):
    if len(digits) == 0:
        return []
    searches = 0
    res=[]
    digitss={"2":"abc",
             "3":"def",
             "4":"ghi",
             "5":"jkl",
             "6":"mno",
             "7":"pqrs",
             "8":"tuv",
             "9":"wxyz"}
    def backtracking(i, cur):
        if len(cur)==len(digits):
            res.append(cur)
            return
        for c in digitss[digits[i]]:
            backtracking(i+1,cur+c)
    backtracking(0,"")
    return searches,res

digits = input("enter the string:")
searches,combination = letterCombinations(digits)
print("here's the combinatio:{}".format(combination))
message = ""
for i in combination:
    message+=i
print("the letter combiantion:",message)
final_decmessage = result(combination)
res = verification(message,final_decmessage)
print(res)
end = time.time()
result = end - start
print("execution time",result)
print("searches:",len(combination))