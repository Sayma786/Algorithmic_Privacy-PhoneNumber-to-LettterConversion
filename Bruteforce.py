from verify import result,verification
#space complexity = O(3^n)
#time complexity = O(4^n)
import time
start = time.time()

searches = 0
def letterCombinations(searches,digits):
    if len(digits) == 0:
        return []

    digitss = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    combinations = ['']
    for digit in digits:
        letters = digitss[digit]
        new_combinations = []
        for combo in combinations:
            for letter in letters:
                new_combinations.append(combo + letter)
                searches +=1
        combinations = new_combinations

    return searches,combinations

digits = input("Enter the string of digits: ")
searches,combination = letterCombinations(searches,digits)
print("Here's the combinations: {}".format(combination))
message = ""
for i in combination:
    message+=i
print("the letter combiantion:",message)
final_decmessage = result(combination)
res= verification(message,final_decmessage)
print(res)
end = time.time()
result = end - start
print("execution time",result)
print("searches",searches)