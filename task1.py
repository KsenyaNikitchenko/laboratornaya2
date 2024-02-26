n=10
print("Задание 1. Вариант ",(n-1)%10+1)

def progress(istrikestr,maxday):
    dates=set()
    istrikes=istrikestr.split()
    an=int(istrikes[0])
    step=int(istrikes[1])+1
    while(an<maxday):
        dates.add(an)
        an+=step
    return dates
begininf=list(input("Введите количество дней в году и число партий: ").split())
strikes=[]
N=int(begininf[0])
K=int(begininf[1])
print("Введите информацию о забастовках:")
for i in range(K):
    strikes.append(input())
datesofstrikes=set()
for i in range(len(strikes)):
    datesofstrikes.update(progress(strikes[i],N))
print("Количество забастовок, произошедших в течение года, равно ",len(datesofstrikes))