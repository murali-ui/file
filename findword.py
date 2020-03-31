
fn = input("Enter file name:")
sw = input("Enter word to be searched:")
a = 0

with open(fn, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==sw):
                a=a+1

print("search word is:",sw,"\t occurrence is",":", a)
