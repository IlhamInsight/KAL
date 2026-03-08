---
title: Eliminasi Gauss
date: 2026-03-08
---

## Pengertian

Eliminasi Gauss ditemukan oleh **Carl Friedrich Gauss**, metode ini dapat digunakan untuk memecahkan sistem persamaan linier dengan mengubah persamaan tersebut menjadi bentuk matriks. Matriks tersebut lalu diubah ke dalam bentuk **Eselon Baris** melalui ** Operasi Baris Elementer**. Kemudian sistem diselesaikan dengan substitusi balik.

## Eselon Baris

Apa itu eselon baris?
Suatu matriks dapat dikatakan sebagai eselon baris jika memenuhi 3 syarat.

1. Jika dalam suatu baris, terdapat elemen-elemen yang **tidak semuanya nol**, maka bilangan **tak nol pertama** di dalam baris tersebut adalah 1. Contohnya adalah sebagai berikut:

```{math}
:label: eselon_baris_matrix_1

\begin{bmatrix}
    1 & 4 & 0 & 2 \\
    0 & 0 & -1 & 2 \\
    0 & 0 & 0 & 1
\end{bmatrix}
```
