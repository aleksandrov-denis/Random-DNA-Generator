import doctest
from random import randint


NUC = 'ATGC'

def run(length, num, rep_at_index, filename):
    '''(int, int, int, str) -> NoneType
    This function takes three integers representing the length of each strand, number of strands, and
    a number that determines the constancy of a nucleotide at a specific index relative to previously
    generated strands. The function also takes a string representing the name of the output file.
    This function writes a series of random nucleotides to a file with any extension. All strands end with
    either C or G with a length 5-15.
    '''
    fobj = open(filename, 'w')

    list_out = create_list(length, num, rep_at_index)
    for l in list_out:
        fobj.write(l + '\n')
    fobj.close()
    
def create_list(length, num, rep_at_index):
    '''(int, int) -> list
    Function takes two integers, one representing the length of each dna strand and the
    other representing the length of the returned list of strands.
    '''
    list_out = []
    for line in range(num):
        remaining_len = length
        byt_list = []
        while remaining_len > 0:
            if remaining_len <= rep_at_index:
                nums = remaining_len
            else:
                nums = rep_at_index
            byt = make_strand(nums)
            while byt in byt_list:
                byt = make_strand(nums)
            byt_list.append(byt)
            remaining_len -= nums
        byt_list[-1] = byt_list[-1][:-2] + NUC[randint(2,3)]
        list_out.append(''.join(byt_list))
    return list_out

def make_strand(length):
    strand = ''
    for n in range(length):
        strand += NUC[randint(0,3)]
    return strand

length = int(input('Enter the length for each strand: '))
num = int(input('Enter the number of strands: '))
rep_at_index = int(input('Enter the number of consecutive nucleotides that have to be unique in each strand: '))
filename = input('Enter the name of the file to write to (with appropriate extension): ')
run(length, num, rep_at_index, filename)