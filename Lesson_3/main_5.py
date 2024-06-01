# Алгоритмы
# Алгоритмом называется набор инструкций для выполнения некоторой задачи. В
# принципе, любой фрагмент программного кода можно назвать алгоритмом, но мы с
# Вами рассмотрим 2 самых интересных алгоритмы сортировок:
# ● Быстрая сортировка
# ● Сортировка слиянием

#####################################

# ● Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [1, 2, 5, 8, 9, 7, 10, 45, 1, 7]
merge_sort(list1)
print(list1)
