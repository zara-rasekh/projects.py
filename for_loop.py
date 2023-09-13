names_a=["ava","bita","ana","arshina","hana","peyman","niloofar","afshin"]
names_b=["zahra","melika","ana","niloofar","rayan","sara","peyman","hana"]
same=[]

for n in names_a :
    for i in names_b:
         if n==i:
            same.append(n)

print(same)
print(len(same))      