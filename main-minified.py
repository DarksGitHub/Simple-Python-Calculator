w='Another? Y/N: '
v='18'
u='17'
t='16'
s='14'
r='13'
q='Formula: d/2=r'
p='12'
o='11'
n='10'
m='9'
l='8'
k='7'
j='6'
i='5'
h='3'
g='1'
b='Circumference: '
a=')'
Z='The Square Root Of:'
Y='Area: '
X='Radius: '
W='Diameter: '
V='4'
S='^'
R='('
P='~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
O='/'
K='*'
G='2'
F=float
E=input
D='='
A=print
from pdb import Restart as T
def c(x,y):return x+y
def d(x,y):return x-y
def e(x,y):return x*y
def f(x,y):return x/y
C=3.14
A(P)
A('Select operation by typing the number')
A(P)
A('1. Add')
A('2. Subtract')
A('3. Multiply')
A('4. Divide')
A('5. Exponent/To The Power Of')
A('18. Square Root')
A(P)
A('6. Calculate The Circumference Of A Circle If You Have Diameter')
A('7. Calculate The Circumference Of A Circle If You Have Radius')
A('8. Calculate The Circumference Of A Circle If You Have Area')
A(P)
A('9. Calculate The Area Of A Circle If You Have Diameter')
A('10. Calculate The Area Of A Circle If You Have Radius')
A('11. Calculate The Area Of A Circle If You Have Circumference')
A(P)
A('12. Calculate The Radius Of A Circle If You Have Diameter')
A('13. Calculate The Radius Of A Circle If You Have Area')
A('14. Calculate The Radius Of A Circle If You Have Circumference')
A(P)
A('15. Calculate The Diameter Of A Circle If You Have Radius')
A('16. Calculate The Diameter Of A Circle If You Have Area')
A('17. Calculate The Diameter Of A Circle If You Have Circumference')
A(P)
while True:
	B=E('Choice: ')
	if B in(g,G,h,V,i):I=F(E('First Number: '));L=F(E('Second Number: '))
	if B in j:
		J=F(E(W))
		if B==j:A(J,K,C,D,J*C,'(Formula: C = pi*d)')
	if B in k:
		H=F(E(X));J=H*2
		if B==k:A(H,K,G,D,J,K,C,D(J*C),'Formula: r*2=d*pi=c ')
	if B in l:
		N=F(E(Y))
		if B==l:A(G,K,Z,R,C,K,N,a,D,2*(C*N)**0.5,'Formula: 2V--(pi*a)=c (The V-- Is Supposed To Be The Square Root Symbol)')
	if B in m:
		J=F(E(W));H=J/2
		if B==m:A(J,O,G,H,S,G,K,C,D,H**2*3.14,'Formula: d/2=r^2*pi=a')
	if B in n:
		H=F(E(X))
		if B==n:A(H,S,G,K,C,D(H**2*3.14),'Formula: r^2*pi=a')
	if B in o:
		M=F(E(b))
		if B==o:A(M,S,G,O,V,K,C,D,M**2/(4*C),'Formula #1: c^2/4*pi=a');A('Or Another Way Of Writing The Problem:');A(C,'[',M,O,R,G,C,']',S,G,D,M**2/(4*C),'Formula #2: pi[c/(2*pi)]^2=a')
	if B in p:
		J=F(E(W));H=J/2
		if B==p:A(J,O,G,D,H,q)
	if B in r:
		N=F(E(Y))
		if B==r:A(Z,N,O,C,D,0.5**(N/C),'Formula: a/2*piV-- (The V-- Is Supposed To Be The Square Root Symbol)')
	if B in s:
		M=F(E(b))
		if B==s:A(M,O,R,G,K,C,a,D,M/(2*C),'Formula: c/2*pi=r')
	if B in'15':
		H=F(E(X))
		if B==15:A(H,K,G,D(H*2),q)
	if B in t:
		N=F(E(Y))
		if B==t:A(Z,R,N,O,C,a,D(0.5**(N/C)),'Formula: V--(a/pi)=r (The V-- Is Supposed To Be The Square Root Symbol)')
	if B in u:
		M=F(E(b));U=M/(2*C)
		if B==u:A(M,O,R,G,C,D,U,K,G,D,U*2,'Formula: c/2*pi=?*2=d')
	if B in v:
		x=F(E('Number: '))
		if B==v:A('The Square Root Of',I,D,I**0.5,'Formula #1: Number^0.5, Formula #2: V--Number (The V-- Is Supposed To Be The Square Root Symbol)')
	if B==g:A(I,'+',L,D,c(I,L))
	if B==G:A(I,'-',L,D,d(I,L))
	if B==h:A(I,K,L,D,e(I,L))
	if B==V:A(I,O,L,D,f(I,L))
	if B==i:A(I,S,L,D,I**L)
	Q=E(w)
	if Q=='N':break
	if Q=='Y':T
	if Q=='n':break
	if Q=='y':T
	else:A("Invalid Input (Type Y Meaning Yes And N Meaning No, Not The Full Word Because The Program Won't Recognize The Input :)");Q=E(w)
