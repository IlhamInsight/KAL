---
title: Tugas 5
date: 2026-03-09
---

## Membuat operasi baris elementar 5 variabel dan 5 persamaan (eliminasi gauss)

$x1 = 1, x2 = 2, x3 = 3, x4 = 4, x5 = 5$

### Sistem persamaan Linear

$x_1 + x_2 + x_3 + x_4 + x_5 = 15$

$2x_1 + 3x_2 + 2x_3 + 2x_4 + 2x_5 = 32$

$x_1 + 2x_2 + 3x_3 + 2x_4 + 2x_5 = 32$

$x_1 + x_2 + 2x_3 + 3x_4 + 2x_5 = 31$

$x_1 + x_2 + x_3 + 2x_4 + 3x_5 = 29$

### Matriks Augmanted:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
2 & 3 & 2 & 2 & 2 & 32 \\
1 & 2 & 3 & 2 & 2 & 32 \\
1 & 1 & 2 & 3 & 2 & 31 \\
1 & 1 & 1 & 2 & 3 & 29
\end{array}
\right]
$$

### Operasi Baris Elementer

1. Kolom 1 (Baris 1($R_1$))

Pakai baris 1 untuk menolkan elemen dibawah angka 1 pada kolom pertama.

- $R_2 \leftarrow R_2 - 2R_1$

  > - $2 - 2(1) = 0$
  > - $3 - 2(1) = 1$
  > - $2 - 2(1) = 0$
  > - $2 - 2(1) = 0$
  > - $2 - 2(1) = 0$
  > - $32 - 2(15) = 2$

- $R_3 \leftarrow R_3 - R_1$

  > - $1 - 1 = 0,\; 2 - 1 = 1,\; 3 - 1 = 2,\; 2 - 1 = 1,\; 2 - 1 = 1 \;|\; 32 - 15 = 17$

- $R_4 \leftarrow R_4 - R_1$

  > - $1 - 1 = 0,\; 1 - 1 = 0,\; 2 - 1 = 1,\; 3 - 1 = 2,\; 2 - 1 = 1 \;|\; 31 - 15 = 16$

- $R_5 \leftarrow R_5 - R_1$
  > - $1 - 1 = 0,\; 1 - 1 = 0,\; 1 - 1 = 0,\; 2 - 1 = 1,\; 3 - 1 = 2 \;|\; 29 - 15 = 14$

Matriks:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 1 & 2 & 1 & 1 & 17 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

2. Kolom 2 (baris 2($R_2$))

Pakai baris 2 untuk menolkan elemen di bawah angka 1 pada kolom kedua. Kebetulan hanya $R_3$ yang perlu diproses.

- $R_3 \leftarrow R_3 - R_2$

  > - $0 - 0 = 0$
  > - $1 - 1 = 0$
  > - $2 - 0 = 2$
  > - $1 - 0 = 1$
  > - $1 - 0 = 1$
  > - $17 - 2 = 15$

- (Baris 4 dan 5 sudah bernilai 0 di kolom kedua, jadi lewati saja).

Matriks:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 2 & 1 & 1 & 15 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

3. Kolom 3 (Tukar($R_3$<->$R_4$) & Pivot)

Supaya tidak bertemu pecahan ($15 ÷ 16$), kita tukar $R_4$ dengan $R_4$ karena $R_4$ memiliki angka 1 di kolom ketiga.

- Tukar $R_3 \leftrightarrow R_4$

- $R_4 \leftarrow R_4 - 2R_3$
  > - $0 - 2(0) = 0$
  > - $0 - 2(0) = 0$
  > - $2 - 2(1) = 0$
  > - $1 - 2(2) = -3$
  > - $1 - 2(1) = -1$
  > - $15 - 2(16) = -17$

Matriks:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & -3 & -1 & -17 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

4. Kolom 4(Tukar($R_4$<->$R_5$))

- Tukar $R_4 \leftrightarrow R_5$
- $R_5 \leftarrow R_5 + 3R_4$
  > - $0 + 3(0) = 0, \ 0 + 3(0) = 0, \ 0 + 3(0) = 0$
  > - $-3 + 3(1) = 0$
  > - $-1 + 3(2) = 5$
  > - $-17 + 3(14) = -17 + 42 = 25$

Matriks :

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & 1 & 2 & 14 \\
0 & 0 & 0 & 0 & 5 & 25
\end{array}
\right]
$$

### Subtitusi Balik

- Mencari $x_5$:
  > - $5x_5 = 25 \implies \mathbf{x_5 = 5}$
- Mencari $x_4$:
  > - $x_4 + 2x_5 = 14$
  > - $x_4 + 2(5) = 14 \implies x_4 + 10 = 14 \implies \mathbf{x_4 = 4}$
- Mencari $x_3$:
  > - $x_3 + 2x_4 + x_5 = 16$
  > - $x_3 + 2(4) + 5 = 16 \implies x_3 + 8 + 5 = 16 \implies \mathbf{x_3 = 3}$
- Mencari $x_2$:
  > - Dari baris 2: $1x_2 = 2 \implies \mathbf{x_2 = 2}$
- Mencari $x_1$:
  > - $x_1 + x_2 + x_3 + x_4 + x_5 = 15$
  > - $x_1 + 2 + 3 + 4 + 5 = 15$
  > - $x_1 + 14 = 15 \implies \mathbf{x_1 = 1}$

Hasil :

$$x_1 = 1, x_2 = 2, x_3 = 3, x_4 = 4, x_5 = 5$$
