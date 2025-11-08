def approximate_pi(n_terms):
    leibniz_series = []
    pai = 0  

    for i in range(n_terms):
        sign = (-1) ** i
        denominator = 2 * i + 1
        term = sign * (1 / denominator)  
        leibniz_series.append(term)
        pai = pai + term  #sum

    pai = 4 * pai  
    return pai
