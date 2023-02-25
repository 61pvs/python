def sort_array(source_array):
    # Return a sorted array.
    m=[]
    for i in source_array:
        if i%2!=0:
            m.append(i)
    m.sort()
    for i in range(len(source_array)):
        if source_array[i]%2!=0:
            source_array[i] = m[0]
            del m[0]
    return source_array

print(sort_array([5, 8, 6, 3, 4]))