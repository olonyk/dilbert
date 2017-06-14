# https://www.facebook.com/ThinkingHumanity/videos/1032600683467487/

from max_len_read_sub import MLRS

dictionary= ["what","at","a","how","help","i", "am", "ace", \
             "mobile","samsung","sam","sung","man","mango", \
             "icecream","and","go","i","like","ice","cream"]
dictionary= ["i","on"]
looked_up_words = []


M = [[-1 for x in range(4)] for y in range(4)]


def read2(w):
    w_sub = ""
    for w_i in reversed(w):
        w_sub = w_i + w_sub
        ret = read(w_sub)
        if ret:
            return True
    return False

def nr_subs(string, start, end):
    if end > len(string):
        return 0
    subs = 0
    for i in range(end, start, -1):
        if read(string[i-1:end]):
            subs = 1
            start = end
            break
    end = end + 1
    return subs + nr_subs(string, start, end)

def nr_subs_dyn(string):
    M = [[-1 for x in range(len(string))] for y in range(len(string))]
    subs = 0
    j_max = len(string)
    for i in range(len(string), -1, -1):
        for j in range(j_max, i, -1):
            print(str(i) + " " + str(j) + " -> " + string[i:j])
            if read(string[i:j]):
                M[i][j-1] = 1
                M[i][i] = 1
                subs = subs + 1
                j_max = i
                break
            else:
                M[i][j-1] = 0
    print(" ".join(string))
    for i, row in enumerate(M):
        #print(str(i) + ":", end='')
        for cell in row:
            if cell == -1:
                print("  ", end='')
            else:
                print(str(cell) + " ", end='')
        print()
    return subs

def nr_subs_dyn_vec(string):
    M = [-1 for x in range(len(string)+1)]
    subs = 0
    j_max = len(string)
    for i in range(len(string), -1, -1):
        for j in range(j_max, i, -1):
            print(str(i) + " " + str(j) + " -> " + string[i:j])
            if read(string[i:j]):
                M[i] = 1
                subs = subs + 1
                j_max = i
                break
            else:
                M[i] = 0
    print(" ".join(string))
    for cell in M:
        if cell == -1:
            print("  ", end='')
        else:
            print(str(cell) + " ", end='')
    print()
    return subs

def nr_subs_dyn_vec_min(string):
    n = len(string)
    M = [0 for x in range(n)]
    subs = 0
    for i in range(1, n):
        for j in range(n):
            if j+i > n:
                break
            elif not any(M[k] == 1 for k in range(j, j+i)):
                print(str(j) + " " + str(j+i) + " -> " + string[j:j+i])
                if read(string[j:j+i]):
                    for k in range(j, j+i):
                        M[k] = 1
                    subs = subs + 1
                    print("Found '" + string[j:j+i] + "', M = " + ' '.join(str(M)))
    print(" ".join(string))
    for cell in M:
        if cell == -1:
            print("  ", end='')
        else:
            print(str(cell) + " ", end='')
    print()
    return subs

def MRS(s, k, j):
    n = len(s)
    # Base case 1, already tested
    #if M[k] != -1:
    #    return M[k]
    # Base case 2, one char string
    if n == 1:
        if read(s):
            M[k][j-1] = 1
            return 1
        else:
            M[k][j-1] = 0
            return 0
    # Recursive case, find which cut that maximizes the s1.
    i_sum = 0
    i_max = 0
    for i in range(1, n):
        s1 = s[0:i]
        s2 = s[i:n]
        print(str(k) + "-s : " + s)
        print(str(k) + "-s1: " + s1)
        print(str(k) + "-s2: " + s2)
        mrs_s1 = MRS(s1, k, i)
        mrs_s2 = MRS(s2, k+1, j)
        i_sum = mrs_s1 + mrs_s2
        if i_sum > i_max:
            i_max = i_sum
    i_max = (1 if read(s) else 0) if i_max == 0 else i_max
    M[k][j-1] = i_max
    return i_max

def word_break(string):
    size = len(string)
    # Trivial case
    if size == 0: return False

    # Create the dybamic programing table M to store results of the subproblems. The value
    # M[k] will be true if string[0:k] can be segmented into dictinary words and false otherwise.
    M = [False]*(size+1)
    for k in range(1, size +1):
        # If M[k] is false we check if the current prefix can make it true.
        # The current prefix is string[0:k]
        if not M[k] and read2(string[0:k]):
            M[k] = True
        # If M[k] is true then search for all substrngs from (k+1)th character and store
        # their results.
        if M[k]:
            # The last prefix is reached.
            if k == size:
                return True
            for j in range(k+1, size +1):
                if not M[j] and read2(string[k:j]):
                    M[j] = True
                # If we reached the last character
                if j == size and M[j]:
                    print(M)
                    return True
    print(M)
    return False

#a = word_break("whatzzhowqruhelpw")
#print(a)
#print(str(nr_lookups))
string = "IZON"
#string = "izona"

mlrs = MLRS(string)
mlrs.new_MRS()

#sub_sets = nr_subs_dyn_vec(string)
#print("I've found " + str(sub_sets) + " disjointed words, and I did " + str(nr_lookups) + " number of look ups")
#sub_sets = nr_subs_dyn("iamace",0,1)
#print("I've found " + str(sub_sets) + " disjointed words, and I did " + str(nr_lookups) + " number of look ups")




















