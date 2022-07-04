import random
words=[]
n=int(input("Number of words to get random word from (min 6 letters):  "))
for i in range(0,n):
   l=str(input())
   words.append(l)
v=random.randint(0,n)
stri=words[v-1]
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabets)
l=len(stri)
count1=0
count2=0
for char in stri.lower():
    user_input=input("\t\tGuess the alphabets  ")
    if user_input in alphabets:
        if user_input in stri.lower():
            count1+=1  #number of characters in stri are
            print("Go on, you playing nice!! ")
        else:
            count2+=1  #number of characters not in stri are
            print("wrong!! Keep trying!")
        alphabets.remove(user_input)
    else:
        print("char not in alphabets")
if count2>3:
    print("You Lost!!")
else:
    print("You Won!!\n The word was "+stri )



