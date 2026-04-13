---
title: Tugas 4
date: 2026-03-09
---

## Membuat operasi baris elementar 4 variabel dan 4 persamaan (eliminasi gauss)

$ x1 = 1, x2 = 2, x3 = 3, x4 = 4$

### Sistem Persamaan Linear

$$
x_1 + x_2 + x_3 + x_4 = 10 \\
2x_1 + 3x_2 + x_3 + x_4 = 15 \\
x_1 + 2x_2 + 3x_3 + x_4 = 18 \\
x_1 + x_2 + x_3 + 2x_4 = 14
$$

### Matrix Augmented:

$$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10 \\
2 & 3 & 1 & 1 & 15 \\
1 & 2 & 3 & 1 & 18 \\
1 & 1 & 1 & 2 & 14
\end{array}
\right]
$$

### Operasi Baris Elementer

1. Kolom 1(pivot R1) Pakai baris pertama sebagai jangkar untuk membuat kolom 1 dibawahnya menjadi 0. $
   R_2 \leftarrow R_2 - 2R_1 $

   > - $ 2 - 2(1) = 0 $
   > - $3 - 2(1) = 1$
   > - $1 - 2(1) = -1$
   > - $1 - 2(1) = -1$
   > - $15 - 2(10) = -5$

- $ R_3 \leftarrow R_3 - R_1 $

  > - $1 - 1 = 0,\; 2 - 1 = 1,\; 3 - 1 = 2,\; 1 - 1 = 0 \mid 18 - 10 = 8$

- $ R_4 \leftarrow R_4 - R_1 $

  > - $1 - 1 = 0,\; 1 - 1 = 0,\; 1 - 1 = 0,\; 2 - 1 = 1 \mid 14 - 10 = 4$

Matriks:

$$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10 \\
0 & 1 & -1 & -1 & -5 \\
0 & 1 & 2 & 0 & 8 \\
0 & 0 & 0 & 1 & 4
\end{array}
\right]
$$

2. Kolom 2(Pivot R2) Pakai baris kedua yang baru untuk membersihkan kolom 2. $ R_4 $ nya sudah memiliki angka 0 di kolom ini, jadi kita cukup menghitung $ R_3 $.

- $R_3 \leftarrow R_3 - R_2$
  > - $0 - 0 = 0$
  > - $1 - 1 = 0$
  > - $2 - (-1) = 2 + 1 = 3$
  > - $0 - (-1) = 0 + 1 = 1$
  > - $8 - (-5) = 8 + 5 = 13$

Matriks:

$$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10 \\
0 & 1 & -1 & -1 & -5 \\
0 & 0 & 3 & 1 & 13 \\
0 & 0 & 0 & 1 & 4
\end{array}
\right]
$$

3. Baris 4 ($R_4$) Baris 4 ($R_4$) sudah memiliki nol di kolom ketiga. Matriks ini sudah berbentuk Eselon Baris (segitiga atas). Jadi tidak perlu melakukan menolkan kolom 3 karena di bawah pivot $ x_3 $ sudah nol.

Dari matriks ini, kita baca persamaan-persamaannya sebagai berikut:

$$
\begin{cases}
0x_1 + 0x_2 + 0x_3 + 1x_4 = 4 & \text{(Baris 4)} \\
0x_1 + 0x_2 + 3x_3 + 1x_4 = 13 & \text{(Baris 3)} \\
0x_1 + 1x_2 - 1x_3 - 1x_4 = -5 & \text{(Baris 2)} \\
1x_1 + 1x_2 + 1x_3 + 1x_4 = 10 & \text{(Baris 1)}
\end{cases}
$$

### Subtitusi Balik

- Mencari $x_4$ (dari baris 4):
  $$ 1x_4 = 4 \;\Rightarrow\; \mathbf{x_4 = 4} $$
- Mencari $x_3$ (dari baris 3):
  $$
  3x_3 + x_4 = 13\\
  3x_3 + 4 = 13 \;\Rightarrow\; 3x_3 = 9 \;\Rightarrow\; \mathbf{x_3 = 3}
  $$
- Mencari $x_2$ (dari baris 2):
  $$
  x_2 - x_3 - x_4 = -5\\
  x_2 - 3 - 4 = -5\\
  x_2 - 7 = -5 \;\Rightarrow\; x_2 = -5 + 7 \;\Rightarrow\; \mathbf{x_2 = 2}
  $$
- Mencari $x_1$ (dari baris 1):
  $$
  x_1 + x_2 + x_3 + x_4 = 10\\
  x_1 + 2 + 3 + 4 = 10\\
  x_1 + 9 = 10 \;\Rightarrow\; \mathbf{x_1 = 1}
  $$

Hasil:

$$x_1 = 1,\; x_2 = 2,\; x_3 = 3,\; x_4 = 4$$
