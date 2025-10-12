# Лабораторная работа №2

## Задание №1-array.py
```

empty_list = []
def find_min_max(values):
    if values == empty_list: 
        return "ValueError"
    return min(values), max(values)  
def get_unique_sorted(values):
    if values == empty_list: 
        return "ValueError"  
    return list(set(sorted(values)))  

def flatten_list(nested):

    if nested == empty_list: 
        return "ValueError"  
    flat_list = []
    for sublist in nested: 
        for item in sublist:
            if not isinstance(item, int):  
                return "TypeError" 
            flat_list.append(item)
    return flat_list

print("find_min_max")
print(find_min_max([3, -1, 5, 5, 0]))  
print(find_min_max([42]))  
print(find_min_max([-5, -2, -9]))  
print(find_min_max([]))  
print(" ")

print("get_unique_sorted")
print(get_unique_sorted([3, 1, 2, 1, 3]))  
print(get_unique_sorted([]))  
print(get_unique_sorted([-1, -1, 0, 2, 2]))  
print(get_unique_sorted([1.0, 1, 2.5, 2.5, 0])) 

print(" ")

print("flatten_list")
print(flatten_list([[1, 2], [3, 4]]))  
print(flatten_list([[1, 2], (3, 4, 5)]))  
print(flatten_list([[1], [], [2, 3]]))  
print(flatten_list([[[1, 2], "ab"]]))  
```
<img width="1157" height="580" alt="Снимок экрана 2025-10-06 194847" src="https://github.com/user-attachments/assets/68b16fdc-c179-47e6-91b0-a5ec6f1d9eb7" />

## Задание №2-matrix.py
```
def transpose(mat):
    if not mat:
        return []
    n = len(mat[0]) 
    for row in mat:
        if len(row) != n:
            return "ValueError"  
    res = [] 
    for j in range(n): 
        new_row = []  
        for i in range(len(mat)): 
            new_row.append(mat[i][j])  
        res.append(new_row)  
    return res  
def row_sums(mat):
    if not mat:
        return [] 
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            return "ValueError" 
    res = []  
    for row in mat:  
        s = 0  
        for x in row:  
            s += x 
        res.append(s)  
    return res  
def col_sums(mat):
    if not mat:
        return [] 
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            return "ValueError"  
    res = []  
    for j in range(n):  
        s = 0  
        for i in range(len(mat)):  
            s += mat[i][j] 
        res.append(s)  
    return res 
print("transpose")
print(transpose([[1, 2, 3]]))  
print(transpose([[1], [2], [3]]))  
print(transpose([[1, 2], [3, 4]]))  
print(transpose([])) 
print(transpose([[1, 2], [3]])) 
print("................................................... ")
print("row_sums")
print(row_sums([[1, 2, 3], [4, 5, 6]]))  
print(row_sums([[-1, 1], [10, -10]])) 
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print("................................................... ")
print("col_sums")
print(col_sums([[1, 2, 3], [4, 5, 6]])) 
print(col_sums([[-1, 1], [10, -10]]))  
print(col_sums([[0, 0], [0, 0]]))  
print(col_sums([[1, 2], [3]]))  
```
<img width="1176" height="614" alt="Снимок экрана 2025-10-06 201825" src="https://github.com/user-attachments/assets/a5237a30-7bcd-4a67-aa8a-05b268066088" />

## Задание №3-tuple.py
```
def format_record(s):
    for i in s:
        if not i:
            return "ValueError"  
    fio = s[0].strip().split()  
    if len(fio) < 2:
        return "ValueError"
    if not isinstance(s[2], float):
        return "TypeError" 
    if not (1 < s[2] <= 5):  
        return "ValueError"  
    try:
        fio_ready = f'"{fio[0].capitalize()} {fio[1][0].upper()}.{fio[2][0].upper()}."'
    except IndexError:
        fio_ready = f'"{fio[0].capitalize()} {fio[1][0].upper()}."'
    group = f"гр. {s[1]}"
    gpa = f"{s[2]:.2f}"
    gpa_ready = f"{gpa}"
    end = f"{fio_ready}, {group}, {gpa_ready}"
    return end  
print(format_record(("Иванов Иван Иванович", "BIVT-25",4.6 )))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("","BIVT-25",3.999)))
```

<img width="537" height="181" alt="Снимок экрана 2025-10-06 212539" src="https://github.com/user-attachments/assets/0b99743d-c348-4daf-9741-9572acd58f27" />

