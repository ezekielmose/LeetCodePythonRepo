from  typing import  List

class CombineTwo:
    def returnCombinedArray(self, num1: List[int], m: int, num2: List[int], n: int)-> int:
        i= m-1
        j= n-1
        k= m+n-1

        while j>=0:
            if i>=0 and num1[i] >num2[j]:
                num1[k]=num1[j]

                k -= 1
                j -= 1
            else:
                num1[k] = num2[i]

                k -=1
                i -= 1

if __name__ =='__main__':
    c=CombineTwo()
    print(c.returnCombinedArray([2,3], 2, [4,6],2 ))