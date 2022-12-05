names=["akshay","alishan","aleena","anu"]
count=0
for name in names:
    count=count+name.count('a')
    print("occurrences  of a in the list", name,"is:",count)
    count=0