class SelectError(Exception): #自作例外 選択肢外エラー
    pass

def menu() -> int: #menu関数

    flag = False #入力完了フラグ
    select = 0 #入力
    selection = {1,2,99} #選択肢
    
    print("1：乗車駅選択")
    print("2：チャージ機能")
    print("")
    print("使用する機能を選択してください(終了する場合には99を入力)")
    
    while(not flag): #入力ループ
        try:
            select = int(input())
            if select not in selection:
                raise SelectError()
        except ValueError: #文字列エラー
            print("数字を入力してください．")
            continue
        except SelectError: #選択肢外エラー
            print("正しい数値を入力してください．")
            continue
        else:
            flag = True
    return select

def select_station() -> int:

    flag = False #入力完了フラグ
    select = 0 #入力
    selection = {1,2,3,99} #選択肢
    station = [ #駅名 運賃
                ["秋葉原",133],
                ["山梨",4128],
                ["長野",7990]
              ]

    for i in range(len(station)):
        print(f"{i+1}:{station[i][0]}駅から\t{station[i][1]}円")
    print("")
    print("乗車する駅を選択してください(キャンセルする場合には99を入力)")
    
    while(not flag): #入力ループ
        try:
            select = int(input())
            if select not in selection:
                raise SelectError()
        except ValueError: #文字列エラー
            print("数字を入力してください．")
            continue
        except SelectError: #選択肢外エラー
            print("正しい数値を入力してください．")
            continue
        else:
            flag = True
    
    if select != 99: #運賃
        name = station[select-1][0]
        fare = station[select-1][1]
        print(f"乗車駅は{name}で料金は{fare}円です．")
    else: #終了
        fare = 0

    return fare

def pay(balance:int, fare:int) -> int:

    flag = False #チャージ完了フラグ
    
    if balance >= fare: #残高 >= 運賃
        balance -= fare
        print(f"チャージ残高は{balance}円です．")
        if balance < 500: #チャージ処理
            print("残高が500円未満のため3000円自動チャージします．")
            balance += 3000
            print(f"チャージ残高は{balance}円です．")
    else: #残高 < 運賃
        print(f"チャージ残高は{balance}円です．")
        print("残高不足です．")
        while(not flag): #チャージ処理
            if balance < fare:
                print("3000円自動チャージします．")
                balance += 3000
            else:
                balance -= fare
                print(f"精算後のチャージ残高は{balance}円です．")
                flag = True

    print("")
    return balance

def charge(balance:int) -> int:

    flag = False #入力完了フラグ
    selection = {1,2,3,4,5,6,7,8,9,10,99} #選択肢
    amount = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #チャージ金額

    print(f"チャージ残高は{balance}円です．")
    print("")

    for i in range(len(amount)):
        print(f"{i+1}:{amount[i]}円")

    print("")
    print("チャージする金額を選択してください(キャンセルする場合には99を入力)")

    while(not flag): #入力ループ
        try:
            select = int(input())
            if select not in selection:
                raise SelectError()
        except ValueError: #文字列エラー
            print("数字を入力してください．")
            continue
        except SelectError: #選択肢外エラー
            print("正しい数値を入力してください．")
            continue
        else:
            flag = True

    if select != 99: #チャージ処理
        chargeAmount = amount[select-1]
        print(f"{chargeAmount}円チャージします．")
        balance += chargeAmount
        print(f"チャージ残高は{balance}円です．")
    else: #終了処理
        print("チャージをキャンセルしました．")
    print("")
    return balance

def main():
    balance = 500
    while(1):
        print("【ウチダ交通　交通ICカード検証システム】\n")
        mode = menu()
        if   mode ==  1: #乗車駅選択
            print("【乗車駅選択】\n")
            fare = select_station()
            if fare == 0: #選択終了
                print("駅の選択をキャンセルしました．\n")
                continue
            else: #運賃支払い
                balance = pay(balance, fare)
        elif mode ==  2: #チャージ機能
            print("【チャージ機能】\n")
            balance = charge(balance)  
        elif mode == 99: #システム終了
            print("システムを終了します\n")
            break

if __name__ == "__main__":
    main()