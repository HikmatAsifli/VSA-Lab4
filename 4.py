# Ədədi massiv yaratmaq
massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ədədi massivi fayla yazmaq
with open('massiv.txt', 'w') as f:
    for eded in massiv:
        f.write(str(eded) + '\n')

# 5-ə bölünməyən ədədləri tapmaq və yeni fayla yazmaq
cem = 0
with open('massiv_yeni.txt', 'w') as yeni_fayl:
    for eded in massiv:
        if eded % 5 != 0:
            yeni_fayl.write(str(eded) + '\n')
            cem += eded

# Cəmi print etmək
print("5-ə bölünməyən ədədlərin cəmi:", cem)
