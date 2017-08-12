00		NOP			4
01 n n		LD BC,nn		10
02		LD (BC),A		7
03		INC BC			6
04		INC B			4
05		DEC B			4
06 n		LD B,n			7
07		RLCA			4
08		EX AF,AF'		4
09		ADD HL,BC		11
0A		LD A,(BC)		7
0B		DEC BC			6
0C		INC C			4
0D		DEC C			4
0E n		LD C,n			7
0F		RRCA			4
10 e		DJNZ (PC+e)		8/13
11 n n		LD DE,nn		10
12		LD (DE),A		7
13		INC DE			6
14		INC D			4
15		DEC D			4
16 n		LD D,n			7
17		RLA			4
18 e		JR (PC+e)		12
19		ADD HL,DE		11
1A		LD A,(DE)		7
1B		DEC DE			6
1C		INC E			4
1D		DEC E			4
1E n		LD E,n			7
1F		RRA			4
20 e		JR NZ,(PC+e)		12/7
21 n n		LD HL,nn		10
22 n n		LD (nn),HL		16
23		INC HL			6
24		INC H			4
25		DEC H			4
26 n		LD H,n			7
27		DAA			4
28 e		JR Z,(PC+e)		12/7
29		ADD HL,HL		11
2A n n		LD HL,(nn)		16
2B		DEC HL			6
2C		INC L			4
2D		DEC L			4
2E n		LD L,n			7
2F		CPL			4
30 e		JR NC,(PC+e)		12/7
31 n n		LD SP,nn		10
32 n n		LD (nn),A		13
33		INC SP			6
34		INC (HL)		11
35		DEC (HL)		11
36 n		LD (HL),n		10
37		SCF			4
38 e		JR c,(PC+e)		12/7
39		ADD HL,SP		11
3A n n		LD A,(nn)		13
3B		DEC SP			6
3C		INC A			4
3D		DEC A			4
3E n		LD A,n			7
3F		CCF			4
40		LD B,B			4
41		LD B,C			4
42		LD B,D			4
43		LD B,E			4
44		LD B,H			4
45		LD B,L			4
46		LD B,(HL)		7
47		LD B,A			4
48		LD C,B			4
49		LD C,C			4
4A		LD C,D			4
4B		LD C,E			4
4C		LD C,H			4
4D		LD C,L			4
4E		LD C,(HL)		7
4F		LD C,A			4
50		LD D,B			4
51		LD D,C			4
52		LD D,D			4
53		LD D,E			4
54		LD D,H			4
55		LD D,L			4
56		LD D,(HL)		7
57		LD D,A			4
58		LD E,B			4
59		LD E,C			4
5A		LD E,D			4
5B		LD E,E			4
5C		LD E,H			4
5D		LD E,L			4
5E		LD E,(HL)		7
5F		LD E,A			4
60		LD H,B			4
61		LD H,C			4
62		LD H,D			4
63		LD H,E			4
64		LD H,H			4
65		LD H,L			4
66		LD H,(HL)		7
67		LD H,A			4
68		LD L,B			4
69		LD L,C			4
6A		LD L,D			4
6B		LD L,E			4
6C		LD L,H			4
6D		LD L,L			4
6E		LD L,(HL)		7
6F		LD L,A			4
70		LD (HL),B		7
71		LD (HL),C		7
72		LD (HL),D		7
73		LD (HL),E		7
74		LD (HL),H		7
75		LD (HL),L		7
76		HALT			4
77		LD (HL),A		7
78		LD A,B			4
79		LD A,C			4
7A		LD A,D			4
7B		LD A,E			4
7C		LD A,H			4
7D		LD A,L			4
7E		LD A,(HL)		7
7F		LD A,A			4
80		ADD A,B			4
81		ADD A,C			4
82		ADD A,D			4
83		ADD A,E			4
84		ADD A,H			4
85		ADD A,L			4
86		ADD A,(HL)		7
87		ADD A,A			4
88		ADC A,B			4
89		ADC A,C			4
8A		ADC A,D			4
8B		ADC A,E			4
8C		ADC A,H			4
8D		ADC A,L			4
8E		ADC A,(HL)		7
8F		ADC A,A			4
90		SUB B			4
91		SUB C			4
92		SUB D			4
93		SUB E			4
94		SUB H			4
95		SUB L			4
96		SUB (HL)		7
97		SUB A			4
98		SBC A,B			4
99		SBC A,C			4
9A		SBC A,D			4
9B		SBC A,E			4
9C		SBC A,H			4
9D		SBC A,L			4
9E		SBC A,(HL)		7
9F		SBC A,A			4
A0		AND B			4
A1		AND C			4
A2		AND D			4
A3		AND E			4
A4		AND H			4
A5		AND L			4
A6		AND (HL)		7
A7		AND A			4
A8		XOR B			4
A9		XOR C			4
AA		XOR D			4
AB		XOR E			4
AC		XOR H			4
AD		XOR L			4
AE		XOR (HL)		7
AF		XOR A			4
B0		OR B			4
B1		OR C			4
B2		OR D			4
B3		OR E			4
B4		OR H			4
B5		OR L			4
B6		OR (HL)			7
B7		OR A			4
B8		CP B			4
B9		CP C			4
BA		CP D			4
BB		CP E			4
BC		CP H			4
BD		CP L			4
BE		CP (HL)			7
BF		CP A			4
C0		RET NZ			11/5
C1		POP BC			10
C2 n n		JP NZ,(nn)		10
C3 n n		JP (nn)			10
C4 n n		CALL NZ,(nn)		17/10
C5		PUSH BC			11
C6 n		ADD A,n			7
C7		RST 0H			11
C8		RET Z			11/5
C9		RET			10
CA n n		JP Z,(nn)		10
CC n n		CALL Z,(nn)		17/10
CD n n		CALL (nn)		17
CE n		ADC A,n			7
CF		RST 8H			11
D0		RET NC			5
D1		POP DE			10
D2 n n		JP NC,(nn)		10
D3 n		OUT (n),A		11
D4 n n		CALL NC,(nn)		17/10
D5		PUSH DE			11
D6 n		SUB n			7
D7		RST 10H			11
D8		RET c			5
D9		EXX			4
DA n n		JP c,(nn)		10
DB n		IN A,(n)		11
DC n n		CALL c,(nn)		17/10
DE n		SBC A,n			15
DF		RST 18H			11
E0		RET PO			11/5
E1		POP HL			10
E2 n n		JP PO,(nn)		10
E3		EX (SP),HL		19
E4 n n		CALL PO,(nn)		17/10
E5		PUSH HL			11
E6 n		AND n			7
E7		RST 20H			11
E8		RET PE			11/5
E9		JP (HL)			4
EA n n		JP PE,(nn)		10
EB		EX DE,HL		4
EC n n		CALL PE,(nn)		17/10
EE n		XOR n			7
EF		RST 28H			11
F0		RET P			11/5
F1		POP AF			10
F2 n n		JP P,(nn)		10
F3		DI			4
F4 n n		CALL P,(nn)		17/10
F5		PUSH AF			11
F6 n		OR n			7
F7		RST 30H			11
F8		RET M			11/5
F9		LD SP,HL		6
FA n n		JP M,(nn)		10
FB		EI			4
FC n n		CALL M,(nn)		17/10
FE n		CP n			7
FF		RST 38H			11
