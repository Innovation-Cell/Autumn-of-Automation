# Lets go for palindromes

palid = int(input("Enter the palindrome: "))

def palid_check(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if str_num[i] == str_num[len(str_num) - (i+1)]:
            result = True
        else:
            return False

    return result

def find_next(palind):
    i = 1
    while True:
        if palid_check(palind + i):
            #print(palid_check(palind + i))
            return palind + i
        else:
            i += 1
            # print(i)
            continue


print(find_next(palid))
