def invest(amount:float,rate:float,years:int):
    
    for i in range(1,years+1):
        amount=amount*(1+rate)
        print(f" year {i}: ${amount:.2f}") # calculates the amount of the investment increased in a given rate after given years
amount=float(input('Enter your initial amount: '))
rate=float(input('Enter investment rate: '))
years=int(input('Enter investment period: '))
print(invest(amount,rate,years))