
global file1_contents,file2_contents
with open('sample1.txt') as f1, open('sample2.txt') as f2:
    file1_contents = f1.read()
    file2_contents = f2.read()

# write the files, swapping them.
open('sample1','w').write(file2_contents)
open('sampl2','w').write(file1_contents)

print('Successfully swapped the two files!')
print('sample 1: {}, sample 2: {}!'.format(file1_contents,file2_contents))
