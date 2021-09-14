import monkdata as m
from dtree import entropy, averageGain

print("entropy")

mk1_entropy = entropy(m.monk1)
print(mk1_entropy) # 1

mk2_entropy = entropy(m.monk2)
print(mk2_entropy) # 0.957117428264771

mk3_entropy = entropy(m.monk3)
print(mk3_entropy) # 0.9998061328047111

#mk1
print("MK1")
mk1a1 = averageGain(m.monk1, m.attributes[0])
print(mk1a1) # 0.07527255560831925

mk1a2 = averageGain(m.monk1, m.attributes[1])
print(mk1a2) # 0.005838429962909286

mk1a3 = averageGain(m.monk1, m.attributes[2])
print(mk1a3) # 0.00470756661729721

mk1a4 = averageGain(m.monk1, m.attributes[3])
print(mk1a4) # 0.02631169650768228

mk1a5 = averageGain(m.monk1, m.attributes[4]) # > infogain!!
print(mk1a5) # 0.28703074971578435

mk1a6 = averageGain(m.monk1, m.attributes[5])
print(mk1a6) # 0.0007578557158638421

print("MK2")
mk2a1 = averageGain(m.monk2, m.attributes[0])
print(mk2a1) # 0.0037561773775118823

mk2a2 = averageGain(m.monk2, m.attributes[1])
print(mk2a2) # 0.0024584986660830532

mk2a3 = averageGain(m.monk2, m.attributes[2])
print(mk2a3) # 0.0010561477158920196

mk2a4 = averageGain(m.monk2, m.attributes[3])
print(mk2a4) # 0.015664247292643818

mk2a5 = averageGain(m.monk2, m.attributes[4]) # > infogain!!
print(mk2a5) # 0.01727717693791797

mk2a6 = averageGain(m.monk2, m.attributes[5])
print(mk2a6) # 0.006247622236881467

print("MK3")

mk3a1 = averageGain(m.monk3, m.attributes[0])
print(mk3a1) # 0.007120868396071844

mk3a2 = averageGain(m.monk3, m.attributes[1])
print(mk3a2) # 0.29373617350838865

mk3a3 = averageGain(m.monk3, m.attributes[2])
print(mk3a3) # 0.0008311140445336207

mk3a4 = averageGain(m.monk3, m.attributes[3])
print(mk3a4) # 0.002891817288654397

mk3a5 = averageGain(m.monk3, m.attributes[4]) # > infogain!!
print(mk3a5) # 0.25591172461972755

mk3a6 = averageGain(m.monk3, m.attributes[5])
print(mk3a6) # 0.007077026074097326
