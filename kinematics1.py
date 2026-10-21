def suvat(u,a,t):#u,a,t are parameters
    s = u*t + 0.5*a*t**2
    v = u + a*t
    return s, v
s,v = suvat(0, 9.81, 2)  # Example usage: initial velocity = 0 m/s, acceleration = 9.81 m/s², time = 2 s
print(s)
print(v)
print(f"s = {s:.2f}, v = {v:.2f}")
  # Example usage: initial velocity = 0 m/s, acceleration = 9.81 m/s², time = 2 s
s,v = suvat(5,2,10)
print(f"s = {s:.2f}, v = {v:.2f}")
