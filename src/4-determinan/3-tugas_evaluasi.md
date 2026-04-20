---
title: TUGAS Evaluasi determinan dan invers
date: 2026-4-20
---

## soal

A. Hitunglah determinan matrik berikut dengan menggunakan rumus expansi baris

$$
\sum_{k=1}^n (-1)^{i+k} a_{ik} M_{ik}
$$

dengan $M_{ij}$ adalah minior dari matrik A dan

$$
M_{ij} = \det A_{ij}.
$$

$A_{ij}$ adalah submatrik dengan menghapus baris i dan kolom kolom j dari matrix $A_{mxn}$ dengan $1 \le i, j \le n$

1. $$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$
2. $$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$
3. $$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}.$$

B. Gunakan rumus matriks adjoin untuk menghitung invers dari matriks berikut dengan rumus

$$(\operatorname{adj} A)_{ij} = (-1)^{i+j} M_{ji}$$

dan

$$A^{-1} = \frac{1}{\det A} \operatorname{adj} A.$$

4. $$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$
5. $$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$
6. $$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}.$$

## Jawaban

1. $$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$

Rumus determinan matrixs 2 x 2

$$
\det(A) = ad - bc\\
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

- Hitung:
  $$\det(A) = (-7) \times (4) - (-5) \times (1)$$

  $$= -28 - (-5) = -28 + 5 = -23$$

2. $$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$

### Langkah 1: Rumus expansi baris ke - 3

$$
\det(A) = (-1)^{3+1} a_{31} M_{31} + (-1)^{3+2} a_{32} M_{32} + (-1)^{3+3} a_{33} M_{33}
$$

### Langkah 2: Lihat elemen pada baris ke - 3

Matriks asli:
$$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$
Baris ke - 3 adalah: 0 0 1

Hitung satu per satu suku.

Suku pertama (kolom 1):

> - Elemen $a_{31}: 0$
>   (ini adalah baris ke -3 kolom ke 1)
> - Tanda: $(-1)^{3 + 1} = 1$
> - Karena elemen $a_{31} = 0$ maka suku ini menjadi
>   $$(+1) \times 0 \times M_{31} = 0$$

Suku Kedua (Kolom 2):

> - : $ a\_{32} = 0 $
>   (Angka di baris ke-3, kolom ke-2)
> - Tanda: $ (-1)^{3+2} = (-1) $
> - Karena elemennya juga 0, maka suku kedua ini juga = 0

Suku Ketiga (Kolom 3):

> - Elemen: $ a\_{33} = 1 $
>   (Angka di baris ke-3, kolom ke-3 — pojok kanan bawah)
> - Tanda: $ (-1)^{3+3} = (+1) $

Hitung minor $M\_{33}
menghapus baris 3 dan kolom 3 dari matriksA.

matriks setelah dihapus $M\_{33}$:

$$
\begin{bmatrix}
0 & 2 \\
1 & -2
\end{bmatrix}
$$

Hitung determinan dari matriks 2×2 ini:
$$M_{33} = (0 \times -2) - (2 \times 1) = 0 - 2 = -2$$

suku ketiga adalah:
$$(+1) \times (1) \times (-2) = -2$$

Jumlahkan semua suku
$$\det(A) = 0 + 0 + (-2) = -2$$

determinan A adalah: - 2

3. $$
   A = \begin{bmatrix}
   1 & -3 & 1 & 1 \\
   -3 & 1 & 1 & 1 \\
   1 & 1 & -3 & 1 \\
   1 & 1 & 1 & -3
   \end{bmatrix}
   $$

### Langkah 1: Rumus ekspansi baris ke-1 ($ i = 1 $):

$$\det(A) = (-1)^{1+1} a_{11} M_{11} + (-1)^{1+2} a_{12} M_{12} + (-1)^{1+3} a_{13} M_{13} + (-1)^{1+4} a_{14} M_{14}$$

Matriks asli:

$$
A = \begin{bmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{bmatrix}
$$

Baru nomor 2
