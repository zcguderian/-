"""利用二分法查找有序列表"""

def two_find(list, index):
    list.sort()
    min = 0  # 设置最小下限
    maxl = len(list)  # 设置最大上限
    if index in list:
        while True:
            midl = (min + maxl) // 2  # 分段
            if list[midl] > index:  # index在list左侧
                maxl = midl
            elif list[midl] < index:  # index在list右侧
                min = midl
            elif list[midl] == index:
                print("{} 在 {} 中的下标是 {}".format(index, list, midl))
                break
    else:
        print("没有该数字")


if __name__ == "__main__":
    arr = [1, 6, 7, 9, 12, 43, 13, 54, 65, 43, 23, 22, 15, 0, 100]
    while True:
        num = input("请输入一个整数: ")
        if num == 'exit' or num == '':
            print('退出...')
            break
        try:
            k = int(num)
            two_find(arr, k)
        except Exception as e:
            print(e)

