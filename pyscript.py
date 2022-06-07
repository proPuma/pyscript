import os, sys
import math
def delete():
	os.system("clear")
	
a = """\033[1;33m _______         __    __    
|   |   |.---.-.|  |_ |  |--.
|       ||  _  ||   _||     |
|__|_|__||___._||____||__|__|"""
d = """
""" """\033[1;33m---------------------------------""" """\033[1;34m
[*] Arifmetik amallarni bajarish
[*] uchun @darknet_off1cial 
[*] tomonidan dasturlangan
[*] dastur.
""" """\033[1;33m---------------------------------"""


r = """

"""
print(a,d)

n = input("""
[*] Davom ettirmoqchimisiz h/y: """)
delete()
if n == 'h':

	o = input("""\033[1;35m
 _______         __    __    
|   |   |.---.-.|  |_ |  |--.
|       ||  _  ||   _||     |
|__|_|__||___._||____||__|__|
"""
"""\033[1;31m
[*] Menular qatoridan kerakligini tanlang [*]
---------------------------------------------
[01] pilus, minus, kopaytruv, bo'lish
[02] logarifmni hisoblash
[03] ildizni hisoblash
[04] kasrni hisoblash
[05] factoriyal ni hisoblash
[06] x ning sinusini topish
[07] x ning cosinusini topish
[08] x ning tanginusini topish
[09] x ning gamma sini qaytaradi
[10] mantissa
[11] kubni hisoblash
---------------------------------------------
[00] Telegram kanallarimiz
---------------------------------------------
>>>""")

if o == '1':
	while True:
		print(eval(input("Son kiriting: ")))
elif o == '2':
	