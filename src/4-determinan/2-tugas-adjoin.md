---
title: TUGAS Join (Adjoin)
date: 2026-4-12
---

## Adjoin Matriks, Determinan, dan Invers Matriks 5 × 5

Matriks A 5 x 5:

$$
A = \begin{bmatrix}
a & b & c & d & e \\
f & g & h & i & j \\
k & l & m & n & o \\
p & q & r & s & t \\
u & v & w & x & y
\end{bmatrix}
$$

## Determinan matriks 5x5 (det A)

Determinan 5×5 dihitung dengan ekspansi kofaktor (biasanya baris pertama):

$$
\det(A)=aC_{11}-bC_{12}+cC_{13}-dC_{14}+eC_{15}
$$

dimana:

## Kofaktor dan Minor

Kofaktor didefinisikan sebagai:

$$
C_{ij} = (-1)^{i+j} \cdot M_{ij}
$$

Keterangan:

- $C_{ij}$ = kofaktor elemen baris ke-$i$, kolom ke-$j$
- $M_{ij}$ = minor, yaitu determinan matriks yang diperoleh dengan menghapus baris ke-$i$ dan kolom ke-$j$

Sehingga:

$$
\text{Kofaktor} = \text{Minor} \times \text{Tanda}
$$

dengan tanda:

$$
(-1)^{i+j}
$$

## Kofaktor dan Cara Menghitung Determinan

Rumus kofaktor:

$$
C_{ij} = (-1)^{i+j} \cdot M_{ij}
$$

dengan:

$$
M_{ij}
$$

adalah determinan matriks $4 \times 4$ yang diperoleh dengan menghapus baris ke-$i$ dan kolom ke-$j$.

---

Jadi, langkah menghitung determinan matriks $5 \times 5$ adalah:

1. Hitung 5 determinan matriks $4 \times 4$
2. Setiap matriks $4 \times 4$ dipecah lagi menjadi determinan $3 \times 3$
3. Lanjutkan proses hingga menjadi determinan $2 \times 2$

## Adjoin Matriks (adj A)

Adjoin adalah transpose dari matriks kofaktor.

### Langkah-langkah:

1. Hitung semua kofaktor $C_{ij}$
2. Susun menjadi matriks kofaktor
3. Transpose matriks tersebut

---

Rumus:

$$
\mathrm{adj}(A) = (C_{ij})^T
$$

---

Artinya:

$$
\mathrm{adj}(A) =
\begin{bmatrix}
C_{11} & C_{21} & C_{31} & C_{41} & C_{51} \\
C_{12} & C_{22} & C_{32} & C_{42} & C_{52} \\
C_{13} & C_{23} & C_{33} & C_{43} & C_{53} \\
C_{14} & C_{24} & C_{34} & C_{44} & C_{54} \\
C_{15} & C_{25} & C_{35} & C_{45} & C_{55}
\end{bmatrix}
$$

## Invers Matriks A

Jika determinan tidak nol, maka invers matriks $A$ adalah:

$$
A^{-1} = \frac{1}{\det(A)} \cdot \mathrm{adj}(A)
$$

---

## Contoh Perhitungan Kofaktor

Misalkan kita ambil elemen pertama:

### Kofaktor $C_{11}$

$$
C_{11} = (+1) \times
\begin{vmatrix}
g & h & i & j \\
l & m & n & o \\
q & r & s & t \\
v & w & x & y
\end{vmatrix}
$$

---

### Kofaktor $C_{12}$

$$
C_{12} = (-1) \times
\begin{vmatrix}
f & h & i & j \\
k & m & n & o \\
p & r & s & t \\
u & w & x & y
\end{vmatrix}
$$

---

Dan seterusnya hingga:

$$
C_{55}
$$

dengan pola:

- Tanda mengikuti $(-1)^{i+j}$
- Minor adalah determinan matriks hasil menghapus baris ke-$i$ dan kolom ke-$j$

## Kesimpulan Singkat

- Determinan:

  $$
  \det(A)
  $$

  dihitung menggunakan ekspansi kofaktor (cukup panjang untuk matriks $5 \times 5$)

- Adjoin:

  $$
  \mathrm{adj}(A)
  $$

  adalah transpose dari matriks kofaktor

- Invers:

  $$
  A^{-1} = \frac{\mathrm{adj}(A)}{\det(A)}
  $$
