for num in range(1, 101):
    string = ''

    # ここから記述
    
    if num % 3 == 0 and num % 5 != 0:
        # 3の倍数かつ5の倍数でない時、Fizzを代入
        string = 'Fizz'
        
    elif num % 3 != 0 and num % 5 == 0:
        #3の倍数でなく5の倍数である時、Buzzを代入
        string = 'Buzz'
        
    elif num % 3 == 0 and num % 5 == 0:
        # 3の倍数かつ5の倍数である時、FizzBuzzを代入
        string = 'FizzBuzz'

    else:
        string = num

    # ここまで記述

    print(string)


