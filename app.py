x=int(input("donner n"))
while(x>30 or x<5):
    x=int(input("doner n"))
tbl=[]
for i in range(x):
    print("valeur numero",i+1,":")
    y=int(input())
    while(x<=0):
        print("valeur numero",i+1,":")
        y=int(input())

    tbl.append(y)

for i in range(x):
    if (tbl[i]%2==0):
        print(tbl[i])