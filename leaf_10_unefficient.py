from turtle import *
import random
bgcolor('black')
#speed(0)
tracer(0, 0)
a,b,c=0,0,0
backward(750)
while b<16000:
	a=a+1+c
	values=(1,0,0,0,0,0,-1)
	q=(random.choice(values))
	if a>17:
		up()
		home()
		backward(750)
		down()
		a=1
		b=b+1
		c=0
		color('forestgreen')
	if q!=0:
		c=c+1
	if a==1 and c==0:
		color('lawngreen')
	if a==2 and c==0:
		color('yellow')
	if a==3 and c==0:
		color('orange')
	if a==4 and c==0:
		color('orangered')
	if a==5 and c==0:
		color('red')
	if a==6 and c==0:
		color('darkred')
	if a==7 and c==0:
		color('darkorchid')
	if a==8 and c==0:
		color('blue')
	if a==9 and c==0:
		color('darkblue')
	if a==10 and c==0:
		color('steelblue')
	if a==11 and c==0:
		color('white')
	width(8/a+0.5)
	right(q*45-2+a/2)
	forward(1600/(1.8*(a+3)+24*c))
