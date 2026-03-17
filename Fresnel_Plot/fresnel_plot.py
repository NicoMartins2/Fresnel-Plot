import matplotlib.pyplot as plt
import numpy as np

# Simpson
def simpson(f, a, b, n):
  h = (b-a)/n

  if n % 2 == 1:
    n += 1

  s = f(a) + f(b)

  for i in range(1, n):
    coef = 4 if i % 2 == 1 else 2

    s += coef*f(a+i*h)

  return s * h/3

# Trapezium

def trapezium(f, a, b, n):
  h = (b-a)/n

  if n % 2 == 1:
    n += 1

  s = f(a) + f(b)

  for i in range(1, n):
    s += 2*f(a+i*h)

  return s * h/2

# Rectangle
def rectangle(f, a, b, n):
  h = (b-a)/n
  s = 0
  for i in range(n):
    s += f(a + (i + 0.5) * h)
  return s * h


# Fresnel
def f_s(t):
    return np.sin(np.pi * t**2 / 2)

def f_c(t):
    return np.cos(np.pi * t**2 / 2)


# t values
t_vals = np.linspace(0, 5, 500)

# --- Simpson Plot ---
C_vals_simpson = []
S_vals_simpson = []

for t in t_vals:
  C_vals_simpson.append(simpson(f_c, 0, t, 500))
  S_vals_simpson.append(simpson(f_s, 0, t, 500))

fig, ax = plt.subplots(1,3, figsize=(10,6))
plt.suptitle('Fresnel Graphical Representation in Different Methods - Simpson x Trapezium x Rectangle')
plt.title("Simpson")
plt.subplot(1, 3, 1)
ax[0].plot(C_vals_simpson, S_vals_simpson, color='#8776DC')
plt.xlabel('C(t)')
plt.ylabel('S(t)')
plt.axis('equal')
plt.tight_layout()

# --- Trapezium Plot ---
C_vals_trapezium = []
S_vals_trapezium = []

for t in t_vals:
  C_vals_trapezium.append(trapezium(f_c, 0, t, 500))
  S_vals_trapezium.append(trapezium(f_s, 0, t, 500))

plt.title("Trapezium")
plt.subplot(1, 3, 2)
ax[1].plot(C_vals_trapezium, S_vals_trapezium, color='orange')
plt.xlabel('C(t)')
plt.ylabel('S(t)')
plt.axis('equal')
plt.tight_layout()


# --- Rectangle Plot ---
C_vals_rectangle = []
S_vals_rectangle = []

for t in t_vals:
  C_vals_rectangle.append(rectangle(f_c, 0, t, 500))
  S_vals_rectangle.append(rectangle(f_s, 0, t, 500))

plt.title("Rectangle")
plt.subplot(1, 3, 3)
ax[2].plot(C_vals_rectangle, S_vals_rectangle, color='green')
plt.xlabel('C(t)')
plt.ylabel('S(t)')
plt.axis('equal')

plt.show()