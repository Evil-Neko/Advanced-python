def arr_sum(arr):
    res = 0
    for i in range(len(arr)):
        res += arr[i]
    return res

def arr_mean(arr):
    res = arr_sum(arr)
    return round(res/len(arr), 2)

arr1 = list(map(int, input('Enter the first array of numbers(no more than 15): ').split()))
arr2 = list(map(int, input('Enter the second array of numbers(no more than 15): ').split()))
arr3 = list(map(int, input('Enter the third array of numbers(no more than 15): ').split()))
print(f'First array: \n Sum = {arr_sum(arr1)}; Arithmetic mean = {arr_mean(arr1)}')
print(f'Second array: \n Sum = {arr_sum(arr2)}; Arithmetic mean = {arr_mean(arr2)}')
print(f'Third array: \n Sum = {arr_sum(arr3)}; Arithmetic mean = {arr_mean(arr3)}')