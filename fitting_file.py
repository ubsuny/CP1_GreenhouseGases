def fitting(data):
    n = len(data)
    if n <= 2: 
        print('Error! Not enough data!') 
    # Declare all variables (x and y components)
    s_x = 0
    s_y = 0
    s_xx = 0
    s_xy = 0
    for i in range(0,n):
        entry = data[i]
        s_x += entry[0]
        s_y += entry[1]
        s_xx += entry[0]**2
        s_xy += entry[1]**2
    den = n * s_xx - s_x**2    
    if abs(den) < 0.0000001:
        print('Error! Denominator is zero!')
    a = (s_xx * s_y - s_x * s_xy) / den
    b = (n*s_xy - s_x * s_y) / den
    sigma2 = 0
    for i  in range (0,n):
        entry = data[i]
        sigma2 += (entry[1] - (a*entry[0]))**2
    sigma2 = sigma2 / (n-2)
    final = [a,b,sigma2]
    return final