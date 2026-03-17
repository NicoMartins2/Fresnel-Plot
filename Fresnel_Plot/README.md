📊 Fresnel Integrals Visualization using Numerical Methods
📊 Visualização das Integrais de Fresnel com Métodos Numéricos
🇧🇷 Português (PT-BR)
📌 Descrição

Este projeto implementa a visualização das Integrais de Fresnel utilizando métodos numéricos clássicos:

Método do Retângulo

Método do Trapézio

Método de Simpson (1/3)

O objetivo é representar graficamente a curva paramétrica:

C(t) = ∫₀ᵗ cos(πt²/2) dt  
S(t) = ∫₀ᵗ sin(πt²/2) dt

Essa curva gera a Espiral de Cornu, uma estrutura matemática interessante por não possuir solução analítica em termos de funções elementares.

⚙️ Métodos Numéricos Implementados
🔹 Método do Retângulo

A integral é aproximada pela soma de áreas de retângulos:

∫ f(x) dx ≈ Σ f(x_i) * h

Simples de implementar

Menor precisão

Útil para entendimento inicial

🔹 Método do Trapézio

A integral é aproximada por trapézios:

∫ f(x) dx ≈ (h/2)[f(a) + 2Σf(x_i) + f(b)]

Mais preciso que o retângulo

Considera variação linear da função

🔹 Método de Simpson (1/3)

Utiliza aproximação por parábolas:

∫ f(x) dx ≈ (h/3)[f(a) + 4Σf(x_ímpar) + 2Σf(x_par) + f(b)]

Alta precisão

Requer número par de subdivisões

Melhor custo-benefício para funções suaves

🧠 Estrutura do Código
1. Definição das funções
def f_s(t):
    return np.sin(np.pi * t**2 / 2)

def f_c(t):
    return np.cos(np.pi * t**2 / 2)

Essas funções representam os integrandos das integrais de Fresnel.

2. Métodos numéricos

Cada método é implementado como uma função que recebe:

f: função a ser integrada

a, b: intervalo

n: número de subdivisões

Exemplo (Simpson):

def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        s += coef * f(a + i*h)
        
    return s * h / 3
3. Construção da curva

Para cada valor de t, calculamos:

C(t) = ∫₀ᵗ cos(...)
S(t) = ∫₀ᵗ sin(...)

Armazenando os valores em listas:

C_vals.append(...)
S_vals.append(...)
4. Plotagem

A curva é gerada com:

ax.plot(C_vals, S_vals)

Cada método numérico pode gerar sua própria curva para comparação visual.

📈 Resultado

O gráfico gerado representa uma espiral que converge para:

(C(∞), S(∞)) = (0.5, 0.5)

Diferenças entre os métodos aparecem principalmente em:

Precisão da curva

Suavidade

Estabilidade para valores grandes de t

🇺🇸 English (US-EN)
📌 Description

This project implements the visualization of Fresnel Integrals using classical numerical methods:

Rectangle Method

Trapezoidal Rule

Simpson’s Rule (1/3)

The goal is to graph the parametric curve:

C(t) = ∫₀ᵗ cos(πt²/2) dt  
S(t) = ∫₀ᵗ sin(πt²/2) dt

This generates the Cornu Spiral, a mathematical structure that has no closed-form solution in elementary functions.


⚙️ Implemented Methods
🔹 Rectangle Method

Approximates the integral as a sum of rectangles:

∫ f(x) dx ≈ Σ f(x_i) * h

Simple implementation

Low accuracy

Good for conceptual understanding

🔹 Trapezoidal Rule

Approximates using trapezoids:

∫ f(x) dx ≈ (h/2)[f(a) + 2Σf(x_i) + f(b)]

More accurate than rectangle

Assumes linear variation

🔹 Simpson’s Rule (1/3)

Uses parabolic approximation:

∫ f(x) dx ≈ (h/3)[f(a) + 4Σf(odd) + 2Σf(even) + f(b)]

High accuracy

Requires even subdivisions

Best trade-off for smooth functions

🧠 Code Structure
1. Function definitions
def f_s(t):
    return np.sin(np.pi * t**2 / 2)

def f_c(t):
    return np.cos(np.pi * t**2 / 2)

These represent the Fresnel integrands.

2. Numerical methods

Each method receives:

f: function

a, b: interval

n: subdivisions

Example (Simpson):

def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        s += coef * f(a + i*h)
        
    return s * h / 3
3. Curve construction

For each t:

C(t) = ∫₀ᵗ cos(...)
S(t) = ∫₀ᵗ sin(...)

Stored in arrays:

C_vals.append(...)
S_vals.append(...)
4. Plotting
ax.plot(C_vals, S_vals)

Each numerical method can generate its own curve for comparison.

📈 Result

The plot represents a spiral converging to:

(C(∞), S(∞)) = (0.5, 0.5)

Differences between methods appear in:

Accuracy

Smoothness

Stability for large t


🧩 Final Note

This project is a practical exploration of how numerical approximation transforms abstract integrals into visual structures, bridging mathematics and computation.