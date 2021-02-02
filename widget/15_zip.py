kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "bananan", "orange"]

print(list(zip(kor, eng))) # 압축

mixed = [('사과', 'apple'), ('바나나', 'bananan'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # 해제

kor2, eng2 = list(zip(*mixed))

print(kor2)
print(eng2)