def list_comprehension(num_ls):
    return [num_ls[i] + num_ls[i - 1] for i, num in enumerate(num_ls) if i > 0]

