def BinarySearch(List, number):
    low = 0
    high = len(List) - 1

    if List[high] < number:
        return -1
    else:
        while low <= high:
            mid = int((low + high) / 2)
            if List[mid] < number:
                low = mid + 1
            elif List[mid] > number:
                high = mid - 1
            else:
                return mid

List = []
while True:
    print("Add number into List or type s to stop: ")
    number = input()
    if number == "s":
        break
    else:
        List.append(number)

new_list = sorted(List)
print(new_list)
search_value = input("Enter search value: ")
result = BinarySearch(new_list, search_value)
if result == -1:
    print("Number not in List")
else:
    print("Number found in Index: ", result)
