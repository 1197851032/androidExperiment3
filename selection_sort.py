def selection_sort(arr):
    """实现选择排序算法"""
    n = len(arr)
    for i in range(n):
        # 找到剩余未排序元素中的最小值
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换找到的最小值和当前位置的元素
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def test():
    """测试选择排序功能"""
    try:
        # 获取用户输入并转换为整数列表
        input_data = input("请输入待排序的整数（用空格分隔）：")
        numbers = list(map(int, input_data.split()))
        
        # 调用选择排序函数
        sorted_numbers = selection_sort(numbers.copy())
        
        # 输出排序结果
        print("排序前的列表：", numbers)
        print("排序后的列表：", sorted_numbers)
        
    except ValueError:
        print("输入无效，请输入用空格分隔的整数！")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    test()