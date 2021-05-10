'''
https://www.codeproject.com/Tips/1275693/Recursive-Permutations-in-Python
'''

class Solution:
    def largestTimeFromDigits(self, arr: list) -> str:
        '''
        Make all permutations of 4 digits find max of hours and minutes
        i =0,1,2,3, i=1,2,3,0, i=2,3,0,1, i=3,0,1,2
        keep all as is
        hours as is, switch C,D
        switch A,B,
        '''
        curr = ''
        i, j, k, m = 0, 1, 2, 3
        count = 0

        while True:
            first = (i + count) % 4
            second_idx = (j + count) % 4
            third_idx = (k + count) % 4
            fourth_idx = (m + count) % 4

        pass

    def permute(self,s):
        out = []
        if len(s) == 1:
            return s
        else:
            for i, let in enumerate(s):
                for perm in self.permute(s[:i] + s[i + 1:]):
                    temp = [let + perm]
                    out += temp
                    #out += [let + perm]
        return out

    def combinations(self, a):
        '''
        DP: [1,1,1,4]: empty set is base case then with 1: {}, {1},
        :param a:
        :return:
        '''


if __name__=="__main__":
    sol = Solution()
    # Driver program to test above function
    data = list('1234')
    for p in sol.permute(data):
        print(p)

    ans = sol.permute(data)
    print(f'ans: {ans}')
    all_arrs = []
    for answer in ans:
        all_arrs.append(list(answer))
    print(all_arrs)
    print('combos')
    print(sol.combinations(data))

    arr = [1, 2, 3, 4]
    #23:41

    arr = [5, 5, 5, 5]
    #'' no solution

    arr = [0,0,1,0]
    #10:00

    arr = [0,0,0,0]
    #00:00