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

$$\det(A) = (-1)^{1+1}a_{11}M_{11} + (-1)^{1+2}a_{12}M_{12} + (-1)^{1+3}a_{13}M_{13} + (-1)^{1+4}a_{14}M_{14}$$

Matriks asli:

$$
A = \begin{bmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{bmatrix}
$$

Baris ke-1: 1  -3  1  1

Langkah 2: Hitung satu per satu
Suku Pertama (Kolom 1):

Elemen: $ a*{11} = 1 $
Tanda: $ (-1)^{1+1} = +1 $
Minor $ M*{11} $ (hapus baris 1, kolom 1):

$$
\begin{bmatrix}
1 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
$$

$$M_{11} = 1\begin{vmatrix}-3&1\\1&-3\end{vmatrix} -1\begin{vmatrix}1&1\\1&-3\end{vmatrix} +1\begin{vmatrix}1&-3\\1&1\end{vmatrix} = -16$$
Suku 1 = $ (+1) \times 1 \times (-16) = -16 $
Suku Kedua (Kolom 2):

Elemen: $ a*{12} = -3 $
Tanda: $ (-1)^{1+2} = -1 $
Minor $ M*{12} $ (hapus baris 1, kolom 2):

$$
\begin{bmatrix}
-3 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
$$

$$M_{12} = -16$$
Suku 2 = $ (-1) \times (-3) \times (-16) = -48 $
Suku Ketiga (Kolom 3):

Elemen: $ a*{13} = 1 $
Tanda: $ (-1)^{1+3} = +1 $
Minor $ M*{13} $ (hapus baris 1, kolom 3):

$$
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
$$

$$M_{13} = 16$$
Suku 3 = $ (+1) \times 1 \times 16 = +16 $
Suku Keempat (Kolom 4):

Elemen: $ a*{14} = 1 $
Tanda: $ (-1)^{1+4} = -1 $
Minor $ M*{14} $ (hapus baris 1, kolom 4):

$$
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & -3 \\
1 & 1 & 1
\end{bmatrix}
$$

$$M_{14} = -16$$
Suku 4 = $ (-1) \times 1 \times (-16) = +16 $

Langkah 3: Jumlahkan semua suku
$$\det(A) = -16 + (-48) + 16 + 16 = -48 + 48 = \boxed{0}$$
Determinan matriks A adalah 0.

4. $$
   A = \begin{bmatrix}
   -7 & -5 \\
   1 & 4\\
   \end{bmatrix}
   $$

Langkah 1: Hitung Determinan
$$\det(A) = (-7 \times 4) - (-5 \times 1) = -28 + 5 = {-23}$$

Langkah 2: Buat Matriks Adjoin
Menurut rumus yang diberikan soal:

$ (adj A)_{ij} = (-1)^{i+j} M_{ji} $
Kita hitung setiap elemen adjoin satu per satu:

$ (adj A)_{11} = (-1)^{1+1} \times $ minor $ M_{11} $
Minor $ M*{11} $ = 4 → $ (adj A)*{11} = 4 $

$ (adj A)_{12} = (-1)^{1+2} \times $ minor $ M_{21} $
Minor $ M*{21} $ = -5 → $ (adj A)*{12} = -1 \times (-5) = 5 $

$ (adj A)_{21} = (-1)^{2+1} \times $ minor $ M_{12} $
Minor $ M*{12} $ = 1 → $ (adj A)*{21} = -1 \times 1 = -1 $

$ (adj A)_{22} = (-1)^{2+2} \times $ minor $ M_{22} $
Minor $ M*{22} $ = -7 → $ (adj A)*{22} = +(-7) = -7 $

Jadi matriks Adjoin:

$$
adj(A) = \begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}
$$

Langkah 3: Hitung Invers

$$
A^{-1} = \frac{1}{\det(A)} \times adj(A) = \frac{1}{-23} \begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}
$$

$$
A^{-1} = {
\begin{bmatrix}
-\dfrac{4}{23} & -\dfrac{5}{23} \\
\dfrac{1}{23} & \dfrac{7}{23}
\end{bmatrix}
}
$$

Matriks 2×2
Untuk matriks $ \begin{bmatrix} a & b \\ c & d \end{bmatrix} $, inversnya langsung:
$$A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
Pakai angka soal:

$$
A^{-1} = \frac{1}{-23} \begin{bmatrix} 4 & -(-5) \\ -1 & -7 \end{bmatrix}
= \frac{1}{-23} \begin{bmatrix} 4 & 5 \\ -1 & -7 \end{bmatrix}
$$

5. $$
   A = \begin{bmatrix}
   0 & 2 & -3 \\
   1 & -2 & -1 \\
   0 & 0 & 1\\
   \end{bmatrix}
   $$

Langkah 1: Hitung Determinan

Gunakan ekspansi baris ke-3 (karena banyak nol):

$$\det(A) = (-1)^{3+3} \times 1 \times M_{33}$$
Minor $ M\_{33} $ (hapus baris 3, kolom 3):

$$
\begin{bmatrix}
0 & 2 \\
1 & -2
\end{bmatrix}
\qquad
M_{33} = (0 \times -2) - (2 \times 1) = -2
$$

$$\det(A) = (+1) \times 1 \times (-2) = \boxed{-2}$$

Langkah 2: Buat Matriks Adjoin

Hitung setiap elemen $ (adj A)_{ij} = (-1)^{i+j} M_{ji} $ Ini memerlukan 9 minor, tapi karena matriks kecil dan banyak nol, cukup ringkas.

Hasil Matriks Adjoin (setelah dihitung lengkap):

$$
adj(A) = \begin{bmatrix}
-2 & -2 & -8 \\
-1 & 0 & -3 \\
0 & 0 & 2
\end{bmatrix}
$$

Langkah 3: Hitung Invers

$$
A^{-1} = \frac{1}{\det(A)} \times adj(A) = \frac{1}{-2} \begin{bmatrix}
-2 & -2 & -8 \\
-1 & 0 & -3 \\
0 & 0 & 2
\end{bmatrix}
$$

Hasil Akhir

$$
A^{-1} = {
\begin{bmatrix}
1 & 1 & 4 \\
\frac{1}{2} & 0 & \frac{3}{2} \\
0 & 0 & -1
\end{bmatrix}
}
$$

6. $$
   A = \begin{bmatrix}
   1 & -3 & 1 & 1 \\
   -3 & 1 & 1 & 1 \\
   1 & 1 & -3 & 1 \\
   1 & 1 & 1 & -3\\
   \end{bmatrix}
   $$

Langkah 1: Hitung Determinan det(A)

Menggunakan ekspansi cofactor sepanjang baris pertama sesuai rumus:

$$\det(A) = \sum_{j=1}^{4} (-1)^{1+j} a_{1j} M_{1j}$$

Perhitungan minor-minor:

- $ M\_{11} = -16 $
- $ M\_{12} = -16 $
- $ M\_{13} = 16 $
- $ M\_{14} = -16 $

$$\det(A) = (1)(-16) + (-3)(-1)(-16) + (1)(16) + (1)(-1)(-16) = -16 -48 + 16 + 16 = \boxed{0}$$
Langkah 2: Matriks Adjoin
Sesuai rumus yang diminta soal:
$$(adj\, A)_{ij} = (-1)^{i+j} M_{ji}$$
Matriks adjoin dapat dihitung, tetapi tidak perlu dilanjutkan karena determinan nol.
Langkah 3: Hitung Invers
Sesuai rumus yang diminta:
$$A^{-1} = \frac{1}{\det A} \ adj(A)$$
Karena $ \det(A) = 0 $, pembagian dengan nol tidak terdefinisi.

Hasil Akhir:

$A^{-1} \quad \text{tidak ada (tidak terdefinisi)}$

Matriks $ A $ tidak memiliki invers (singular / tidak invertible).
