def avg_multiple(*args):
    return sum(args)/len(args)
print(avg_multiple(1, 2, 4, 6))
print(avg_multiple(2, 2))

def sort_str():
    s = input("Eneter your text ")
    print(' '.join(sorted(s.split(' '))))
    
sort_str()

def sort_nums():
    num_seq_str = input("Please, enter your sequence ").split()
    try:
        num_seq = [int(x) for x in num_seq_str] 
        print(sorted(num_seq, reverse=False))
    except ValueError:
        print('You have entered not numbers into the sequence')
sort_nums()