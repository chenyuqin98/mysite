
urls=[]
for i in range(1,11):
    urls.append('https://libgen.lc/search.php?&res=100&req=Computer&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page='+str(i))

for i in range(0,10):
    print(urls[i])