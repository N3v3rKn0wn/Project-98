
global data_a,data_b
def swapFileData():    
    with open('sample1.txt') as f1, open('sample2.txt') as f2:
        data_a = f1.read()
        data_b = f2.read()

open('file_1.txt','w').write(data_b)
open('file_2.txt','w').write(data_a)

print('Successfully swapped the two files!')
print('data_a: {}, data_b: {}!'.format(file1_contents,file2_contents))
swapFileData()