keypad=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def posscomb(comb,cur,output,n):
    if cur ==n:
        print(*output,sep=",")
        return
    for i in range(len(keypad[comb[cur]])):
        output.append(keypad[comb[cur]][i])
        posscomb(comb,cur+1,output,n)
        output.pop()
        if comb[cur]==0 or comb[cur]==1:
            return
comb=[4,3,4]
n=len(comb)
posscomb(comb,0,[],n)