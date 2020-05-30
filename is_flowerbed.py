class Sol:
    def is_flowerbed(self,arr,n):
        j=0
        count=0
        for i in range(len(arr)):
            if arr[i]==1:
                c=int((i-j-1)/2)
                print('c=',c)
                if c>0:
                    count+=c
                j=i
            elif i==len(arr)-1:
                c = int((i-j) / 2)
                if c > 0:
                    count += c
        return count>=n
if __name__ == '__main__':
    p1=Sol()
    print(p1.is_flowerbed([1,0,0,0,0], 2))
