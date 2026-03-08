---
title: SageMath
date: 2026-03-08
---

## Pengertian

SageMath adalah _software open-source_ matematika berbasis Python. _Software_ ini sering digunakan untuk membantu perhitungan matematika, mulai dari aljabar, geometri, dan sebagainya. Untuk menggunakan SageMath, anda dapat menggunakan sintaks-sintaks dari Python.

Sebagai contoh, disini saya menyelesaikan SPLDV menggunakan SageMath.

```python
var('x y')
solve([x + 2*y == 20, 2*x + 3*y == 33], x, y)
```

Jika kita menuliskan kode diatas, berarti kita menyuruh SageMath untuk mencari solusi dari persamaan berikut.

```{math}
:label: sagemath_ex_eq

\begin{aligned}
x + 2y &= 20 \\
2x + 3y &= 33
\end{aligned}
```

SageMath akan langsung mencarikan solusi dari persamaan diatas tanpa anda melakukan eliminasi manual.
