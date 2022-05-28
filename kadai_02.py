def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    # 探索範囲の左端と右端を定義
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        # 中間の値を切り捨て除算で定義
        mid = (left + right) // 2
        if sorted_array[mid] == target_number:
            # 中間の値と探索対象が一致した場合、中間の値を返す
            return mid
        elif sorted_array[mid] < target_number:
            # 中間の値が探索対象より小さい場合、左端を変更
            left = mid + 1
        else:
            # 中間の値が探索対象より大きい場合、右端を変更
            right = mid - 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
