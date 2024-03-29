def heapify(num_list, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    if (left <= heap_size - 1) and (num_list[left] > num_list[i]):
        cur_max = left
    else:
        cur_max = i

    if (right <= heap_size - 1) and (num_list[right] > num_list[cur_max]):
        cur_max = right

    if cur_max != i:
        num_list[i], num_list[cur_max] = num_list[cur_max], num_list[i]
        num_list = heapify(num_list, cur_max, heap_size)

    return num_list


def build_heap(num_list):
    heap_size = len(num_list)
    num_of_parent = heap_size // 2

    for i in range(num_of_parent - 1, -1, -1):
        num_list = heapify(num_list, i, heap_size)

    return num_list


def heap_sort(num_list):
    heap_size = len(num_list)
    num_list = build_heap(num_list)
    length = heap_size

    for i in range(length - 1, 0, -1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        heap_size -= 1
        num_list = heapify(num_list, 0, heap_size)

    return num_list
