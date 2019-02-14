import random

with open('./data/siamese_data/sun2') as f:
    lines1 = f.readlines()
with open('./data/siamese_data/yuan2') as f:
    lines2 = f.readlines()
with open('./data/siamese_data/yu2') as f:
    lines3 = f.readlines()


def create_siamese0():
    with open('./data/siamese_data/siamese0.txt', 'a') as w:
        for line1 in lines1:
            for line2 in lines2:
                w.write(line1.strip() + ' ' + line2.strip() + '\n')
            for line3 in lines3:
                w.write(line1.strip() + ' ' + line3.strip() + '\n')
        for line2 in lines2:
            for line3 in lines3:
                w.write(line2.strip() + ' ' + line3.strip() + '\n')


def create_siamese1():
    with open('./data/siamese_data/siamese1.txt', 'a') as w:
        for l11 in lines1:
            for l12 in lines1:
                w.write(l11.strip() + ' ' + l12.strip() + '\n')
        for l21 in lines2:
            for l22 in lines2:
                w.write(l21.strip() + ' ' + l22.strip() + '\n')
        for l31 in lines3:
            for l32 in lines3:
                w.write(l31.strip() + ' ' + l32.strip() + '\n')


with open('./data/siamese_data/siamese0_shuffle.txt', 'r') as f:
    with open('./data/siamese_data/siamese1_shuffle.txt', 'r') as w:
        with open('./data/siamese_data/siamese_shuffle.txt', 'w') as ww:
            lines0 = f.readlines()
            lines1 = w.readlines()
            lines = lines0 + lines1
            random.shuffle(lines)
            for line in lines:
                ww.write(line)
