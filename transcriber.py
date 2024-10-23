from os import popen
import tkinter

#Hello!!!
#csjbfish


codes = {"UUU":"Phe","UUC":"Phe", "UUA":"Lew", "UUG":"Leu", "UCU": "Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser", "UAU":"Tyr", "UAC":"Tyr","UGU":"Cys", "UGC":"Cys", "UGG":"Trp","CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu", "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro", "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln", "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg", "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met", "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr", "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys", "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg", "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val", "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala", "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu", "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}
template = input("Enter Template Code: ")

codon = ""
polypeptideCode = ""
final = ""

for c in template:
    if c == "A":
        codon+="U"
    elif c == "T":
        codon+="A"
    elif c == "C":
        codon+="G"
    elif c == "G":
        codon+="C"

start = codon.index("AUG")

if "UAA" in codon:
    stop = codon.index("UAA")
elif "UAG" in codon:
    stop = codon.index("UAG")
elif "UGA" in codon:
    stop = codon.index("UGA")

polypeptideCode = codon[start:stop]
pCodeLen = int(len(polypeptideCode)/3)

for i in range(pCodeLen):
    temp = polypeptideCode[0:3]
    polypeptideCode = polypeptideCode[3:len(polypeptideCode)]
    final = final + codes[temp] + '-'
    i+=1


print("The polypeptide name is "+final[0:len(final)-1]+"\n")
