class AddBi:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == '__main__':
    c=AddBi()
    print(c.addBinary('10', '11'))