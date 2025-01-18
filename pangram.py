sentence=input("Enter a sentence")
"""
acount=0
ecount=0
icount=0
ocount=0
ucount=0
for x in range(len(sentence)):
    if sentence[x]=="a":
        acount=acount+1
for x in range(len(sentence)):
    if sentence[x]=="e":
        ecount=ecount+1
for x in range(len(sentence)):
    if sentence[x]=="i":
        icount=icount+1
for x in range(len(sentence)):
    if sentence[x]=="o":
        ocount=ocount+1
for x in range(len(sentence)):
        if sentence[x]=="u":
            ucount=ucount+1
print(acount)
print(ecount)
print(icount)
print(ocount)
print(ucount)
"""
vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for letter in sentence:
    if letter in vowels:
        vowels[letter]+=1
print(vowels)

number=input("Enter a number and I will check if it is a pangram")

#pangram number
pangram={
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}
ispangram=True
for digit in number:
    if digit in pangram:
        pangram[digit]+=1
for value in pangram.values():
    if value==0:
        ispangram=False
if ispangram:
    print("That is a pangram")
else:
    print("That is not a pangram")
