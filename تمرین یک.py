def squared_log_n(n):
    if n <= 1:
        return 0

    counter = 0
    for i in range(n):
        for j in range(n):
            k = n
            if k == 0:
                k = 1
            temp_k = k
            while temp_k > 0:
                counter += 1
                temp_k //= 2
                if temp_k == 0 and k > 0:
                    pass
                elif temp_k == 0:
                    break
    return counter
