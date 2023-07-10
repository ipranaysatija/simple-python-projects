print("Welcome to KBC,")
print("type the correct option in the input line(lower case),to quit enter '0'")

question = ["1:Who was the first prime minister of india? \na>>Nehru \nb>>Gandhi \nc>>Modi \nd>>Pranay \n",
            "2:The Samkhya School of Philosophy was founded by:\na>>Gautam Buddha \nb>>Mahipala \nc>>Gopala \nd>>Kapila \n ",
            "3:Pustaz grasslands are situated at? \na>>South Africa \nb>>China \nc>>Hungary \nd>>USA \n",
            "4:Right to emergency medical aid is a \na>>Legal Right \nb>>Illegal Right \nc>>Constitutional Right \nd>>Fundamental Right. \n",
            "5:On the recommendation of which of the given committee, the abolition of reservation of items for the small-scale sector in industry is considered?\na>>Lohia Committee \nb>>Narasimhan Committee \nc>>Ajit Kumar Committee \nd>>Abid Hussain Committee \n",
            "6:Chelaiya Samiti is related to which of the following?\na>>Banking sector \nb>>Insurance sector \nc>>Health Sector \nd>>Tax reforms \n",
            "7:Which of the given devices is used for counting blood cells?\na>>Hmelethometer \nb>>Spyscometer \nc>>Hemocytometer \nd>>Hamosytometer \n",
            "8:Which of the given is a disease caused by protozoa?\na>>Cancer \nb>>Typhoid \nc>>Kala-azar \nd>>Chicken Pox \n",
            ]
answers =["a","d","c","d","d","d","c","c" ]
prize = [0,1000,2000,5000,10000,20000,50000,80000,100000]
for n in range(len(question)):
 print("this question is for Rs.",prize[n+1]) 
 print(question[n])
 i=input("type the answer:")
 if(i=="0"):
   print("you decided to quit")
   print("Congratulations, you have won Rs:",prize[n])
   break
 else:
  if(i==answers[n]):
    print("correct")
  else:
    print("wrong,")
    print("Congratulations, you have won Rs:",prize[n])
    break
if(n==7):
 print("Congratulations, you have won Rs:",prize[n+1])
