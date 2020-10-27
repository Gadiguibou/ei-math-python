#eimath2.py
import random
#The variables for the final results are created
result3=0
result4=0
result5=0
#The number of repetition n is set here
n=100000000
#The deck of cards used is created
a=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
#Here, the for loop of a game of war starts
for x in xrange(n):
	#The deck is shuffled
	random.shuffle(a)
	#The deck is split evenly between the two players J1 and J2
	J1=a[:26]
	J2=a[-26:]
	#The variable for the result of each turn is created
	#TEST J1=[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14]
	result1=0
	if J1[0] > J2[0]:
		result1=1
	elif J1[0] < J2[0]:
		result1=2
	i=1
	while J1[i]>J2[i] and result1==1 or J1[i]<J2[i] and result1==2:
		if i==2:
			result3+=1
			if result1==1:
				result4+=1
			else:
				result5+=1
			break
		i+=1
print "RESULT3: "+str(result3)
print "Result4: "+str(result4)
print "Result5: "+str(result5)
print "n = "+str(n)