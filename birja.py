#программа на основе известной цены высчитывает количество продажи/покупки акций со стартовым капиталом 1 рубль
#для получения наибольшей выгоды на выходе по известным ценам price
#выводит количество совершенных сделок купил/продал, а так же дни в которые были совершены сделки(в период с 1 дня и заканчивая steps+1)

#количество дней работы биржи акций (пример ввода: 6)
steps = int(input())

#последовательность целых чисел - цена за единицу акции (пример ввода: 1 3 4 2 6 7)
price = list(map(int,str(input()).split(' ')))

money = 1
stocks = 0
step = 0
buyAndSell = []

def getStocks(money, step):
    for p in price[step+1:]:
        if p>price[step]:
            buyAndSell.append(step+1)
            return 0, money/price[step], step+1
        else:
            return money, 0, step+1
    return money, 0, step+1

def getMoney(stocks, step):
    if step==len(price)-1:
            buyAndSell.append(step+1)
            return stocks*price[step], 0, step+1

    for p in price[step+1:]:
        if p<price[step] or max(price[step+1:])<=price[step]:
            buyAndSell.append(step+1)
            return stocks*price[step], 0, step+1
        elif p>price[step]:
            return 0, stocks, step+1
    return 0, stocks, step+1

while step<steps:
    if money:
        money, stocks, step = getStocks(money, step)
    else:
        money, stocks, step = getMoney(stocks, step)

print(len(buyAndSell)//2)
for i, buy in enumerate(buyAndSell):
    if i%2==0:
        print(buy, end=' ')
    else:
        print(buy, end='\n')