def simple_interest(s, t, r):
    print('The principal is', s)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (s * t * r) / 100

    print('The Simple Interest is', si)
    return si


simple_interest(8, 6, 8)
