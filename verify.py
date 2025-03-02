import rsa

def result(combination):
    original_dyc = ""
    publicKey, privateKey = rsa.newkeys(512)
    x= len(combination)
    i = 0
    j= 10
    while j <= x:
        j =i+10
        print(i)
        print(j)
        message1 = combination[i:j]
        final_message = ""
        for z in message1:
            final_message += z
        encMessage1 = rsa.encrypt(final_message.encode(), publicKey)
        print("encrpted_data:",encMessage1)
        decrpt_msg1 = rsa.decrypt(encMessage1, privateKey).decode()
        print("decrpt_msg1:",decrpt_msg1)
        original_dyc += decrpt_msg1
        i += 10
    return original_dyc
def verification(message,final_decmessage):
     if message == final_decmessage:
         return "VERIFICATION IS SUCCESSFUL!! NO CORUPTION IS DONE"
     return "YES THEIR IS SOME ERROR PLEASE CHECK IT!!"