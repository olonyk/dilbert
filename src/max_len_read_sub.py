
class MLRS:
    def __init__(self, string):
        self.string = string
        self.n = len(string)
        self.M = [[-1 for x in range(self.n)] for y in range(self.n)]
        self.nr_lookups = 0
        self.looked_up_words = []
        self.dictionary = ["I", "ON"]
        self.tree = []

    def read(self, w):
        #print(w + "\t" + str(w in self.dictionary))
        if w in self.looked_up_words:
            print("WARNING this word has been looked up before")
        self.looked_up_words.append(w)
        self.nr_lookups = self.nr_lookups + 1
        return w in self.dictionary

    def new_MRS(self):
        self.MRS(self.string, 0, self.n-1)
        print(" ".join(self.string))
        for row in self.M:
            for cell in row:
                if cell == -1:
                    print("  ", end='')
                    #print(str(cell) + " ", end='')
                else:
                    print(str(cell) + " ", end='')
            print()
        print("I've found " + str(self.M[0][self.n-1]) + " disjointed words, and I did " + str(self.nr_lookups) + " look ups")

    def print_m(self):
        print(" ".join(self.string))
        for row in self.M:
            for cell in row:
                if cell == -1:
                    print("  ", end='')
                    #print(str(cell) + " ", end='')
                else:
                    print(str(cell) + " ", end='')
            print()

    def MRS(self, s, k, j):
        self.tree.append(s)
        print("\t"*k + s + "(" + str(k) + "," + str(j) + ")")
        n = len(s)
        # Base case 1, already tested
        if self.M[k][j] != -1:
            return self.M[k][j]
        # Base case 2, one char string
        if n == 1:
            if self.read(s):
                self.M[k][j] = 1
                return 1
            else:
                self.M[k][j] = 0
                return 0
        # Recursive case, find which cut that maximizes the s1.
        i_sum = 0
        i_max = 0
        for i in range(1, n):
            s1 = s[0:i]
            s2 = s[i:n]
            mrs_s1 = self.MRS(s1, k, k+i-1)
            mrs_s2 = self.MRS(s2, k+i, j)
            print("\t"*k + "|-> s1: " + s1 + "(" + str(k) + "," + str(k+i-1) + ")")
            print("\t"*k + "\-> s2: " + s2 + "(" + str(k+i) + "," + str(j) + ")")
            self.print_m()
            i_sum = mrs_s1 + mrs_s2
            if i_sum > i_max:
                i_max = i_sum
        i_max = (1 if self.read(s) else 0) if i_max == 0 else i_max
        self.M[k][j] = i_max
        return i_max
