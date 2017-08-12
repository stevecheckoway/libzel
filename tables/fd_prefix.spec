FD00		NOP			8
FD01 n n	LD BC,nn		14
FD02		LD (BC),A		11
FD03		INC BC			10
FD04		INC B			8
FD05		DEC B			8
FD06 n		LD B,n			11
FD07		RLCA			8
FD08		EX AF,AF'		8
FD09		ADD IY,BC		15
FD0A		LD A,(BC)		11
FD0B		DEC BC			10
FD0C		INC C			8
FD0D		DEC C			8
FD0E n		LD C,n			11
FD0F		RRCA			8
FD10 e		DJNZ (PC+e)		12/17
FD11 n n	LD DE,nn		14
FD12		LD (DE),A		11
FD13		INC DE			10
FD14		INC D			8
FD15		DEC D			8
FD16 n		LD D,n			11
FD17		RLA			8
FD18 e		JR (PC+e)		16
FD19		ADD IY,DE		15
FD1A		LD A,(DE)		11
FD1B		DEC DE			10
FD1C		INC E			8
FD1D		DEC E			8
FD1E n		LD E,n			11
FD1F		RRA			8
FD20 e		JR NZ,(PC+e)		16/11
FD21 n n	LD IY,nn		14
FD22 n n	LD (nn),IY		16
FD23		INC IY			10
FD24		INC IYH			10	guess
FD25		DEC IYH			10	guess
FD26 n 		LD IYH,n		11	guess
FD27		DAA			8
FD28 e		JR Z,(PC+e)		16/11
FD29		ADD IY,IY		15
FD2A n n	LD IY,(nn)		14
FD2B		DEC IY			10
FD2C		INC IYL			10	guess
FD2D		DEC IYL			10	guess
FD2E n		LD IYL,n		11	guess
FD2F		CPL			8
FD30 e		JR NC,(PC+e)		16/11
FD31 n n	LD SP,nn		14
FD32 n n	LD (nn),A		17
FD33		INC SP			10
FD34 d		INC (IY+d)		23
FD35 d		DEC (IY+d)		23
FD36 d n	LD (IY+d),n		19
FD37		SCF			8
FD38 e		JR c,(PC+e)		16/11
FD39		ADD IY,SP		15
FD3A n n	LD A,(nn)		17
FD3B		DEC SP			10
FD3C		INC A			8
FD3D		DEC A			8
FD3E n		LD A,n			11
FD3F		CCF			8
FD40		LD B,B			8
FD41		LD B,C			8
FD42		LD B,D			8
FD43		LD B,E			8
FD44		LD B,IYH		8	guess
FD45		LD B,IYL		8	guess
FD46 d		LD B,(IY+d)		19
FD47		LD B,A			8
FD48		LD C,B			8
FD49		LD C,C			8
FD4A		LD C,D			8
FD4B		LD C,E			8
FD4C		LD C,IYH		8	guess
FD4D		LD C,IYL		8	guess
FD4E d		LD C,(IY+d)		19
FD4F		LD C,A			8
FD50		LD D,B			8
FD51		LD D,C			8
FD52		LD D,D			8
FD53		LD D,E			8
FD54		LD D,IYH		8	guess
FD55		LD D,IYL		8	guess
FD56 d		LD D,(IY+d)		19
FD57		LD D,A			8
FD58		LD E,B			8
FD59		LD E,C			8
FD5A		LD E,D			8
FD5B		LD E,E			8
FD5C		LD E,IYH		8	guess
FD5D		LD E,IYL		8	guess
FD5E d		LD E,(IY+d)		19
FD5F		LD E,A			8
FD60		LD IYH,B		8	guess
FD61		LD IYH,C		8	guess
FD62		LD IYH,D		8	guess
FD63		LD IYH,E		8	guess
FD64		LD IYH,IYH		8	guess
FD65		LD IYH,IYL		8	guess
FD66 d		LD H,(IY+d)		19
FD67		LD IYH,A		8	guess
FD68		LD IYL,B		8	guess
FD69		LD IYL,C		8	guess
FD6A		LD IYL,D		8	guess
FD6B		LD IYL,E		8	guess
FD6C		LD IYL,IYH		8	guess
FD6D		LD IYL,IYL		8	guess
FD6E d		LD L,(IY+d)		19
FD6F		LD IYL,A		8	guess
FD70 d		LD (IY+d),B		19
FD71 d		LD (IY+d),C		19
FD72 d		LD (IY+d),D		19
FD73 d		LD (IY+d),E		19
FD74 d		LD (IY+d),H		19
FD75 d		LD (IY+d),L		19
FD76		HALT			8
FD77 d		LD (IY+d),A		19
FD78		LD A,B			8
FD79		LD A,C			8
FD7A		LD A,D			8
FD7B		LD A,E			8
FD7C		LD A,IYH		8	guess
FD7D		LD A,IYL		8	guess
FD7E d		LD A,(IY+d)		19
FD7F		LD A,A			8
FD80		ADD A,B			8
FD81		ADD A,C			8
FD82		ADD A,D			8
FD83		ADD A,E			8
FD84		ADD A,IYH		8	guess
FD85		ADD A,IYL		8	guess	
FD86 d		ADD A,(IY+d)		19
FD87		ADD A,A			8
FD88		ADC A,B			8
FD89		ADC A,C			8
FD8A		ADC A,D			8
FD8B		ADC A,E			8
FD8C		ADC A,IYH		8	guess
FD8D		ADC A,IYL		8	guess
FD8E d		ADC A,(IY+d)		19
FD8F		ADC A,A			8
FD90		SUB B			8
FD91		SUB C			8
FD92		SUB D			8
FD93		SUB E			8
FD94		SUB IYH			8	guess
FD95		SUB IYL			8	guess
FD96 d		SUB (IY+d)		19
FD97		SUB A			8
FD98		SBC A,B			8
FD99		SBC A,C			8
FD9A		SBC A,D			8
FD9B		SBC A,E			8
FD9C		SBC A,IYH		8	guess
FD9D		SBC A,IYL		8	guess
FD9E d		SBC A,(IY+d)		19
FD9F		SBC A,A			8
FDA0		AND B			8
FDA1		AND C			8
FDA2		AND D			8
FDA3		AND E			8
FDA4		AND IYH			8	guess
FDA5		AND IYL			8	guess
FDA6 d		AND (IY+d)		19
FDA7		AND A			8
FDA8		XOR B			8
FDA9		XOR C			8
FDAA		XOR D			8
FDAB		XOR E			8
FDAC		XOR IYH			8	guess
FDAD		XOR IYL			8	guess
FDAE d		XOR (IY+d)		19
FDAF		XOR A			8
FDB0		OR B			8
FDB1		OR C			8
FDB2		OR D			8
FDB3		OR E			8
FDB4		OR IYH			8	guess
FDB5		OR IYL			8	guess
FDB6 d		OR (IY+d)		19
FDB7		OR A			8
FDB8		CP B			8
FDB9		CP C			8
FDBA		CP D			8
FDBB		CP E			8
FDBC		CP IYH			8	guess
FDBD		CP IYL			8	guess
FDBE d		CP (IY+d)		19
FDBF		CP A			8
FDC0		RET NZ			15/9
FDC1		POP BC			14
FDC2 n n	JP NZ,(nn)		14
FDC3 n n	JP (nn)			14
FDC4 n n	CALL NZ,(nn)		21/14
FDC5		PUSH BC			15
FDC6 n		ADD A,n			11
FDC7		RST 0H			15
FDC8		RET Z			15/9
FDC9		RET			14
FDCA n n	JP Z,(nn)		14
FDCC n n	CALL Z,(nn)		21/14
FDCD n n	CALL (nn)		21
FDCE n		ADC A,n			11
FDCF		RST 8H			15
FDD0		RET NC			9
FDD1		POP DE			14
FDD2 n n	JP NC,(nn)		14
FDD3 n		OUT (n),A		15
FDD4 n n	CALL NC,(nn)		21/14
FDD5		PUSH DE			15
FDD6 n		SUB n			11
FDD7		RST 10H			15
FDD8		RET c			9
FDD9		EXX			8
FDDA n n	JP c,(nn)		14
FDDB n		IN A,(n)		15
FDDC n n	CALL c,(nn)		21/14
FDDE n		SBC A,n			19
FDDF		RST 18H			15
FDE0		RET PO			15/9
FDE1		POP IY			14
FDE2 n n	JP PO,(nn)		14
FDE3		EX (SP),IY		23
FDE4 n n	CALL PO,(nn)		21/14
FDE5		PUSH IY			15
FDE6 n		AND n			11
FDE7		RST 20H			15
FDE8		RET PE			15/9
FDE9		JP (IY)			8
FDEA n n	JP PE,(nn)		14
FDEB		EX DE,HL		8
FDEC n n	CALL PE,(nn)		21/14
FDEE n		XOR n			11
FDEF		RST 28H			15
FDF0		RET P			15/9
FDF1		POP AF			14
FDF2 n n	JP P,(nn)		14
FDF3		DI			8
FDF4 n n	CALL P,(nn)		21/14
FDF5		PUSH AF			15
FDF6 n		OR n			11
FDF7		RST 30H			15
FDF8		RET M			15/9
FDF9		LD SP,IY		10
FDFA n n	JP M,(nn)		14
FDFB		EI			8
FDFC n n	CALL M,(nn)		21/14
FDFE n		CP n			11
FDFF		RST 38H			15
