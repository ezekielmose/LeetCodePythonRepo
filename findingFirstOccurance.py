class FirstOccurance:
    def strMatchMismatch(self, heystack: str, needle: str)-> str:
        m= len(heystack)
        n= len(needle)

        for i in range (m-n+1):
            if heystack[i:i+n]==needle:
                return 0
        return -1

if __name__=='__main__':
    r=FirstOccurance()
    print(r.strMatchMismatch('school', 'schol'))