"""
1. more than 3 letters in a word send the first two word to the end add three random charectors at the start and at the end 
2. else simply reverse 
3. start and end every letter with p
exp:~
    input: i am a python programer 
    output: pip pmap pap phatthonpylipp phatogramerprlipp
"""
i=input("input: ")
encoder=False
if(encoder):
    print("-----------Encoder----------")
    r1="hat"
    r2="lip"
    coded=[]
    words=i.split(" ")
    for word in words:
        l=len(word)
        if(l==1):
            codedw="p"+word+"p"
            coded.append(codedw)
        elif(l==2):
            codedw="p"+ word[1]+word[0]+"p"
            coded.append(codedw)
        elif(l>=3):
            codedw="p"+r1+word[2:]+word[0]+word[1]+r2+"p"
            coded.append(codedw)
    print(" ".join(coded))
else:
    print("-----------Decoder----------")
    coded=[]
    words=i.split(" ")
    for word in words:
        l=len(word)
        if(l==3):
            codedw=word[1]
            coded.append(codedw)
        elif(l==4):
            codedw=word[2]+ word[1]
            coded.append(codedw)
        elif(l>=5):
            codedw=word[4:-4]
            codedw=codedw[-2]+codedw[-1]+codedw[:-2]
            coded.append(codedw)
    print(" ".join(coded))


