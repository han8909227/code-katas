"""Kata: Moving Zeros to the End - move all zeros in the list to the very end

#1 Best Practices Solution by riyakayal

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
"""


def move_zeros(array):
    """."""
    original_array = array[:]
    num_zeros = 0

    for i, obj in enumerate(original_array):
        try:
            if int(obj) == 0 and not (obj is False):
                value = int(array.pop(i - num_zeros))
                array.append(value)
                num_zeros += 1
        except Exception:
            continue

    return array
