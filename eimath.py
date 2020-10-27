import random
import time
#The variables for the final results are created
result3=0
result4=0
result5=0
#The number of repetition n is set here
n=2000000000
#The deck of cards used is created
a=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
#Here, the for loop of a game of war starts
for x in range(0, n):
	#The deck is shuffled
	random.shuffle(a)
	#The deck is split evenly between the two players J1 and J2
	J1=a[:26]
	J2=a[-26:]
	#The variable for the result of each turn is created
	result1=""
	#Here the for loop iterates through each pair of cards to verify the outcome.
	#If J1 wins a 1 is noted in result1, if J2 wins, a 2 and if it's a draw, a 0.
	for i in range(0,26):
		if J1[i] > J2[i]:
			result1+="1"
		elif J1[i] < J2[i]:
			result1+="2"
		else:
			result1+="0"
	#The variable for the second result is initialized determining the winner of the game after 26 turns (len(a)/2)
	result2=0
	ev1="11111111111111111111111111"
	ev2="22222222222222222222222222"
	#If the winner after 26 turns is J1 result2 becomes 1 and if J2 wins it becomes 2
	if result1==ev1:
		result2=1
	elif result1==ev2:
		result2=2
	#The number of wins after 26 turns is counted in result 3
	if result2==1 or result2==2:
		result3+=1
	if result2==1:
		result4+=1
	if result2==2:
		result5+=1
print "RESULT3: "+str(result3)
print "Result4: "+str(result4)
print "Result5: "+str(result5)
print "n = "+str(n)
