"""
Task 1 - Coding Challenge for LFX Mentorship - RISCV
Saaswath L N
ln.saaswath.eee19@itbhu.ac.in
"""
import sys

isa = input().strip().upper()
coverpoints_list = list()

if "32" in isa:
   xlen = 32
   ext = isa[4:]
elif "64" in isa:
   xlen = 64
   ext = isa[4:]
elif "128" in isa:
   xlen = 128
   ext = value[5:]
else:
   print("Invalid base integer")
   sys.exit()   

if ('G' in isa):
    if 'I' not in isa:
        isa = isa + 'I'
    if 'M' not in isa:
        isa = isa + 'M'
    if 'A' not in isa:
        isa = isa + 'A'
    if 'D' not in isa:
        isa = isa + 'D'
   
if 'I' not in isa and 'E' not in isa:
    print("Invalid base integer")

if 'D' in isa and 'F' not in isa:
    isa = isa + 'F'
    sys.exit() 

for x in "ABCDEFHIJKLMNPQSTUVX":                             
    if x in ext:                      
        pos = 25 - int(ord(x) - ord('A'))     
        ext_coverpoint = hex(2**pos)       
        coverpoints_list.append(f"misa && {ext_coverpoint} == {ext_coverpoint}")
        print(f"misa && {ext_coverpoint} == {ext_coverpoint}")
