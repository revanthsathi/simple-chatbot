
a=input("hello,can you tell me your name")
print("hi"+a)
print("iam your chat bot")
print("i will also check your daily activites and time tables to continue with the chat")
b=input("do you want to chat with me")
if('yes' in b):
    print("ok lets chat")
    b1=input("how is your day going?")
    if('good' in b1 or 'fine' in b1):
        print("awesome")
        b2=input("have you eaten your food")
        if('yes'  in b2):
            print("good lets continue with the chat")
            b3=input("do you know any programming languages?")
            if('yes' in b3):
                print("good")
                b4=input("do you want to play a math game with me")
                if('yes' in b4):
                    print("ok lets start")
                    print("solve the equation and answer the question")
                    print("a+a+a=39,b+b-a=25,6+c+b=50")
                    b5=int(input("find a+b+c"))
                    if b5==57:
                        print("you are correct")
                    else:
                        print("recheck the answer")
                        print("this was a simple chatbot so message me when you bored again bye")
                else:
                    print("ohno,iam sorry i can play only math game here")
                    print("message me anytime later,bye")
            else:
                print("you can learn them when you are free,there are useful")
                b4=input("do you want to play a math game with me")
                if('yes' in b4):
                    print("ok lets start")
                    print("solve the equation and answer the question")
                    print("a+a+a=39,b+b-a=25,6+c+b=50")
                    b5=int(input("find a+b+c"))
                    if b5==57:
                        print("you are correct")
                    else:
                        print("recheck the answer")
                        print("message me anytime later,bye")
                else:
                    print("ohno,iam sorry i can play only math game here")
                    print("this was a simple chatbot so message me when you bored again bye")
        else:
            print("hey,why didnt you ate still its time go eat first then we can continue the chat")
    else:
        print("hooo iam sorry")
        b2= input("have you eaten your food")
        if('yes'  in b2):
            print("good lets continue with the chat")
            b4=input("do you want to play a math game with me")
            if('yes' in b4):
                    print("ok lets start")
                    print("solve the equation and answer the question")
                    print("a+a+a=39,b+b-a=25,6+c+b=50")
                    b5=int(input("find a+b+c"))
                    if b5==57:
                        print("you are correct")
                    else:
                        print("recheck the answer")
                        print("this was a simple chatbot so message me when you bored again bye")
            else:
                print("ohno,iam sorry i can play only math game here")    

        else:
            print("hey,why didnt you ate still its time go eat first then we can continue the chat")
else:
    c=input("are you bored")
    if('yes' in c):
        print("you can chat with me than")
        d=input("so,what will you do will you chat with me")
        if('yes' in d):
            print("if you want to chat you can open this from start and say yes")
        else:
            print("ok then come back you want to chat,bye")        
    else:
        print("ok then come back when you are bored chat,bye")


