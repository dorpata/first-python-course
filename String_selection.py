import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--task')
parser.add_argument('--arg')
args = parser.parse_args()

#first task


def vowels(string):
    Vowels = ['a', 'A', 'i', 'I', 'e', 'E', 'u', 'U', 'y', 'Y', 'o', 'O']
    Bank = []
    for i in args.arg:
        if i in Vowels:
            Bank.append(i)
    return len(Bank)


# second task
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selectiom_sort(lst):      # sort a list in a upper order
    '''sort list in place'''
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return lst


def perfect(string):
    bank = [1]
    for i in range(2, int(args.arg) + 1):
        for k in range(2, int(args.arg) + 1):
            if i ** k not in bank and i ** k <= int(args.arg) ** 2:
                bank.append(i ** k)
    selectiom_sort(bank)
    return bank[int(args.arg) - 1]


def lazy(string):
     n = int(string)
     k = ((n ** 2) - n + 2) // 2
     return  k


if args.task == 'vowels':
    print(vowels(args.arg))
elif args.task == 'perfect':
    print(perfect(args.arg))
elif args.task == 'lazy':
    print(lazy(args.arg))
else:
    print('wrong input')


