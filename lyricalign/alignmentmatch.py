file1 = open("D:\\Main Project\\Pitch-Perfect\\lyricalign\\output.txt",'r')
file2 = open("D:\\Main Project\\Pitch-Perfect\\lyricalign\\output.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()
count = 0

for i in range(len(file2_lines)):
    L1 = file1_lines[i].split('\t')
    L2 = file2_lines[i].split('\t')
    if(L1[0] == L2[0]):
        count = count + 1
print("Match percentage: {:.2f}".format((count/(i+1))*100))

file1.close()
file2.close()
