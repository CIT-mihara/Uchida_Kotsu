def menu() -> int:

    flag = False
    selection = {1,2,99}
    
    print("1：乗車駅選択")
    print("2：チャージ機能")
    print("")
    print("使用する機能を選択してください(終了する場合は99を入力)")
    
    while(not flag):
        try:
            select = int(input())
            if select not in selection:
                raise ValueError()
        except ValueError:
            print("正しい数値を入力してください．")
            continue
        else:
            flag = True
    return select


def select_station() -> int:

    flag = False
    select = 0
    selection = {1,2,3,99}
    station = [
                ["秋葉原",113],
                ["山梨",4128],
                ["長野",7990]
              ]

    for i in range(len(station)):
        print(f"{i+1}:{station[i][0]}\t{station[i][1]}円")
    print("")
    print("乗車する駅を選択してください(キャンセルする場合は99を入力)")
    
    while(not flag):
        try:
            select = int(input())
            if select not in selection:
                raise ValueError()
        except ValueError:
            print("正しい数値を入力してください．")
            continue
        else:
            flag = True
    
    if select != 99:
        name = station[select-1][0]
        fare = station[select-1][1]
        print(f"乗車駅は{name}で料金は{fare}円です．")
    else:
        fare = 0

    print("\n")
    return fare

def pay(balance:int, fare:int) -> int:

    flag = False
    
    if balance >= fare:
        balance -= fare
        print(f"チャージ残高は{balance}です．")
        if balance < 500:
            print("残高が500円未満のため3000円自動チャージします．")
            balance += 3000
            print(f"チャージ残高は{balance}です．")
    else:
        print(f"チャージ残高は{balance}です．")
        print("残高不足です．")
        while(not flag):
            if balance < fare:
                print("3000円自動チャージします．")
                balance += 3000
            else:
                balance -= fare
                print(f"精算後のチャージ残高は{balance}です．")
                flag = True

    print("\n")
    return balance

def charge(balance:int) -> int:

    flag = False
    selection = {1,2,3,4,5,6,7,8,9,10,99}
    amount = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

    print(f"チャージ残高は{balance}です．")
    print("\n")

    for i in range(len(amount)):
        print(f"{i+1}:{amount[i]}円")

    print("")
    print("チャージする金額を選択してください(キャンセルする場合は99を入力)")

    while(not flag):
        try:
            select = int(input())
            if select not in selection:
                raise ValueError()
        except ValueError:
            print("正しい数値を入力してください．")
            continue
        else:
            flag = True

    if select != 99:
        chargeAmount = amount[select-1]
        print(f"{chargeAmount}円チャージします．")
        balance += chargeAmount
        print(f"チャージ残高は{balance}です．")
    else:
        print("キャンセルしました．")
    print("\n")
    return balance

def main():
    balance = 500
    while(1):
        print("【ウチダ交通　交通ICカード検証システム】\n")
        mode = menu()
        if   mode ==  1:
            print("【乗車駅選択】\n")
            fare = select_station()
            if fare == 0:
                print("キャンセルしました．\n")
                continue
            else:
                balance = pay(balance, fare)
        elif mode ==  2:
            print("【チャージ機能】\n")
            balance = charge(balance)  
        elif mode == 99:
            print("システムを終了します\n")
            break

if __name__ == "__main__":
    main()