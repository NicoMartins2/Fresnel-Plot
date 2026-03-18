<h1>📊 Fresnel Integrals Visualization using Numerical Methods</h1>
<img width="1143" height="599" alt="Captura_de_tela_20260317_212925" src="https://github.com/user-attachments/assets/6ebe9d42-be61-4fe1-a7ba-7a16c28db991" />

This project implements the visualization of Fresnel Integrals using classical numerical methods:

-Rectangle Method

-Trapezoidal Rule

-Simpson’s Rule (1/3)

The goal is to graph the parametric curve:

C(t) = ∫₀ᵗ cos(πt²/2) dt
S(t) = ∫₀ᵗ sin(πt²/2) dt

This generates the Cornu Spiral, a mathematical structure that has no closed-form solution in elementary functions.

<h2>Implemented Methods</h2> 

<h3>🔹 Rectangle Method</h3>

Approximates the integral as a sum of rectangles:

∫ f(x) dx ≈ Σ f(x_i) * h

->Simple implementation

->Low accuracy

->Good for conceptual understanding

<h3>🔹 Trapezoidal Rule</h3>

Approximates using trapezoids:

∫ f(x) dx ≈ (h/2)[f(a) + 2Σf(x_i) + f(b)]

-> More accurate than rectangle

-> Assumes linear variation

<h3>🔹 Simpson’s Rule (1/3)</h3>

Uses parabolic approximation:

∫ f(x) dx ≈ (h/3)[f(a) + 4Σf(odd) + 2Σf(even) + f(b)]

-> High accuracy

-> Requires even subdivisions

-> Best trade-off for smooth functions

<h2>Code Structure</h2>

Function definitions def f_s(t): return np.sin(np.pi * t**2 / 2)
def f_c(t): return np.cos(np.pi * t**2 / 2)

These represent the Fresnel integrands.

Numerical methods
Each method receives:

f: function

a, b: interval

n: subdivisions

<h3>Curve construction</h3>
For each t:

C(t) = ∫₀ᵗ cos(...) S(t) = ∫₀ᵗ sin(...)

Stored in arrays:

C_vals.append(...) S_vals.append(...) 4. Plotting ax.plot(C_vals, S_vals)

-> Each numerical method can generate its own curve for comparison.

<h2>Result</h2>

The plot represents a spiral converging to:

(C(∞), S(∞)) = (0.5, 0.5)

Differences between methods appear in:

-> Accuracy

-> Smoothness

-> Stability for large t

<h2>Final Note</h2>

This project is a practical exploration of how numerical approximation transforms abstract integrals into visual structures, bridging mathematics and computation.
