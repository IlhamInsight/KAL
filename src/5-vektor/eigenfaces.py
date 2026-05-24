import os
import cv2
import numpy as np

class EigenfaceRecognizer:
    def __init__(self, target_size=(64, 64), k_komponen=50):
        self.target_size = target_size
        self.k_komponen = k_komponen
        self.wajah_rata_rata = None
        self.eigenfaces = None
        self.bobot_training = None
        self.label_wajah = []

    def siapkan_dataset_otomatis(self, folder_path):
        print(f"[!] Folder dataset '{folder_path}' tidak ditemukan atau kosong.")
        os.makedirs(folder_path, exist_ok=True)
        
        # Coba unduh Olivetti faces dari scikit-learn
        try:
            print("[*] Mencoba mengunduh dataset asli Olivetti Faces dari scikit-learn...")
            from sklearn.datasets import fetch_olivetti_faces
            dataset = fetch_olivetti_faces(shuffle=True, random_state=42)
            for i, img in enumerate(dataset.images):
                # Skala gambar dari [0, 1] float ke [0, 255] uint8
                img_uint8 = (img * 255).astype(np.uint8)
                filename = f"face_{i:03d}.png"
                cv2.imwrite(os.path.join(folder_path, filename), img_uint8)
            print(f"[+] Berhasil mengunduh dan menyimpan {len(dataset.images)} foto wajah asli!")
            return
        except Exception as e:
            print(f"[-] Gagal mengunduh dataset asli ({e}).")
            print("[*] Membuat dataset wajah sintetis sebagai cadangan offline...")
            
        # Jika gagal / offline, buat dataset sintetis agar script tetap bekerja
        count = 410
        for i in range(count):
            img = np.zeros((64, 64), dtype=np.uint8) + 128  # Abu-abu netral
            
            # Gambar elemen wajah sederhana (oval wajah)
            cv2.ellipse(img, (32, 32), (20, 25), 0, 0, 360, 50, -1)
            
            # Gambar mata kiri dan kanan (sedikit variasi koordinat)
            eye_y = 25 + np.random.randint(-1, 2)
            cv2.circle(img, (22, eye_y), 4, 220, -1)
            cv2.circle(img, (42, eye_y), 4, 220, -1)
            cv2.circle(img, (22, eye_y), 1, 0, -1)
            cv2.circle(img, (42, eye_y), 1, 0, -1)
            
            # Gambar hidung
            cv2.line(img, (32, 28), (32, 38), 100, 2)
            
            # Gambar mulut (senyum/sedih acak)
            mouth_w = 8 + np.random.randint(-2, 3)
            mouth_h = 4 + np.random.randint(-1, 3)
            cv2.ellipse(img, (32, 44), (mouth_w, mouth_h), 0, 0, 180, 200, 2)
            
            # Tambahkan noise agar data kaya variasi geometri
            noise = np.random.randint(-12, 13, size=(64, 64))
            img = np.clip(img.astype(np.int32) + noise, 0, 255).astype(np.uint8)
            
            filename = f"face_synthetic_{i:03d}.png"
            cv2.imwrite(os.path.join(folder_path, filename), img)
            
        print(f"[+] Berhasil membuat {count} foto wajah sintetis!")

    def latih_model(self, folder_path):
        print("=== Memulai Tahap Training ===")
        
        # Cek apakah folder dataset ada dan berisi gambar
        jika_kosong = True
        if os.path.exists(folder_path):
            daftar_file = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
            if len(daftar_file) > 0:
                jika_kosong = False
                
        if jika_kosong:
            self.siapkan_dataset_otomatis(folder_path)
            
        # Membaca seluruh foto dari folder
        daftar_file = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        matriks_wajah = []
        
        for filename in daftar_file:
            path = os.path.join(folder_path, filename)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img_resized = cv2.resize(img, self.target_size)
            
            # Ubah jadi vektor 1D dan masukkan ke list
            matriks_wajah.append(img_resized.flatten())
            self.label_wajah.append(filename) # Menyimpan nama file sebagai identitas
            
        # Bentuk Matriks Data A (Ukuran: Piksel x Jumlah_Foto)
        A = np.array(matriks_wajah).T
        print(f"Matriks Data Wajah (A) berhasil dibentuk dengan ukuran: {A.shape}")
        
        # 2. Sentralisasi Data (Mean Subtraction)
        self.wajah_rata_rata = np.mean(A, axis=1, keepdims=True)
        A_terpusat = A - self.wajah_rata_rata
        
        # 3. Hitung SVD sesuai teori matematika
        print("Menghitung Singular Value Decomposition (SVD)...")
        U, S, Vt = np.linalg.svd(A_terpusat, full_matrices=False)
        self.S = S
        
        # 4. Ambil k-Eigenfaces terbesar untuk reduksi dimensi
        self.eigenfaces = U[:, :self.k_komponen]
        print(f"Eigenspace (Eigenfaces) berhasil dibentuk dengan ukuran: {self.eigenfaces.shape}")
        
        # 5. Proyeksikan data training ke Eigenspace untuk mendapat vektor bobot
        self.bobot_training = self.eigenfaces.T @ A_terpusat
        print("Model berhasil dilatih dan vektor bobot disimpan.\n")

    def kenali_wajah_baru(self, path_wajah_baru):
        if self.eigenfaces is None:
            raise ValueError("Model belum dilatih! Jalankan 'latih_model()' terlebih dahulu.")
            
        # 1. Baca dan preprocess wajah baru
        img = cv2.imread(path_wajah_baru, cv2.IMREAD_GRAYSCALE)
        img_resized = cv2.resize(img, self.target_size)
        vektor_baru = img_resized.flatten().reshape(-1, 1) # Jadikan vektor kolom
        
        # 2. Sentralisasi wajah baru terhadap wajah rata-rata training
        vektor_terpusat = vektor_baru - self.wajah_rata_rata
        
        # 3. Proyeksikan ke Eigenspace untuk mendapatkan vektor bobot baru
        bobot_baru = self.eigenfaces.T @ vektor_terpusat
        
        # 4. Hitung Euclidean Distance dengan seluruh data training
        jarak_list = []
        for i in range(self.bobot_training.shape[1]):
            jarak = np.linalg.norm(bobot_baru - self.bobot_training[:, i:i+1])
            jarak_list.append(jarak)
            
        # 5. Cari indeks dengan jarak terpendek (paling mirip)
        indeks_terdekat = np.argmin(jarak_list)
        jarak_terdekat = jarak_list[indeks_terdekat]
        nama_orang_mirip = self.label_wajah[indeks_terdekat]
        
        return nama_orang_mirip, jarak_terdekat
    
    def visualisasikan_eigenfaces(self, jumlah_tampil=10):
        import matplotlib.pyplot as plt
        if self.eigenfaces is None:
            print("[-] Model belum dilatih!")
            return
        
        print(f"[*] Menampilkan {jumlah_tampil} Eigenfaces pertama...")
        plt.figure(figsize=(15, 6))
        for i in range(jumlah_tampil):
            plt.subplot(2, 5, i + 1)
            # Reshape kembali dari vektor 1D (4096) ke matriks 2D (64x64)
            komponen_wajah = self.eigenfaces[:, i].reshape(self.target_size)
            
            plt.imshow(komponen_wajah, cmap='gray')
            plt.title(f"Eigenface {i+1}")
            plt.axis('off')
            
        plt.suptitle("Visualisasi Basis Subspace (Eigenfaces)", fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        # Simpan gambar plot secara otomatis ke folder img
        try:
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "hasil10eigenfaces.png")
            plt.savefig(output_path, dpi=150)
            print(f"[+] Visualisasi Eigenfaces berhasil disimpan ke: {output_path}")
        except Exception as e:
            print(f"[-] Gagal menyimpan visualisasi eigenfaces: {e}")
            
        plt.show()
        
    def plot_retensi_energi(self):
        import matplotlib.pyplot as plt
        if self.S is None:
            print("[-] Data Nilai Singular tidak ditemukan!")
            return
        
        # Hitung varians / energi kumulatif berdasarkan nilai kuadrat singular values
        energi_total = np.sum(self.S**2)
        energi_kumulatif = np.cumsum(self.S**2) / energi_total * 100
        
        plt.figure(figsize=(9, 5))
        # Plot garis energi kumulatif
        plt.plot(range(1, len(energi_kumulatif) + 1), energi_kumulatif, color='blue', linewidth=2)
        
        # Beri tanda titik merah pada batas k komponen yang kita pilih (k=50)
        persen_terpilih = energi_kumulatif[self.k_komponen - 1]
        plt.scatter(self.k_komponen, persen_terpilih, color='red', s=100, zorder=5)
        plt.axhline(y=persen_terpilih, color='red', linestyle='--')
        plt.axvline(x=self.k_komponen, color='red', linestyle='--')
        
        plt.title("Scree Plot: Retensi Energi Kumulatif Nilai Singular", fontsize=12, fontweight='bold')
        plt.xlabel("Jumlah Komponen Utama (k)")
        plt.ylabel("Persentase Informasi / Energi Kumulatif (%)")
        plt.text(self.k_komponen + 10, persen_terpilih - 5, f"k={self.k_komponen}\nInfo = {persen_terpilih:.2f}%", color='red', fontweight='bold')
        plt.grid(True, linestyle=':', alpha=0.6)
        
        # Simpan gambar plot secara otomatis ke folder img
        try:
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "hasil_scatterplot.png")
            plt.savefig(output_path, dpi=150)
            print(f"[+] Scree Plot berhasil disimpan ke: {output_path}")
        except Exception as e:
            print(f"[-] Gagal menyimpan Scree Plot: {e}")
            
        plt.show()

# CARA PENGGUNAAN SKRIP

if __name__ == "__main__":
    pengenal = EigenfaceRecognizer(target_size=(64, 64), k_komponen=50)
    folder_dataset = "eigenfaces" 
    
    try:
        # 1. Jalankan training data (akan otomatis mengunduh/membuat dataset jika tidak ada)
        pengenal.latih_model(folder_dataset)
        
        # === PLAY VISUALISASI GRAFIS ===
        pengenal.visualisasikan_eigenfaces(jumlah_tampil=10)
        pengenal.plot_retensi_energi()
        # ===============================
        
        # 2. Jalankan pengujian wajah baru
        foto_test = "img/test_wajah.jpg"
        
        # Buat dummy foto_test jika tidak ada agar uji deteksi berjalan lancar
        if not os.path.exists(foto_test):
            img_dir = os.path.dirname(foto_test)
            if img_dir:
                os.makedirs(img_dir, exist_ok=True)
            # Ambil salah satu gambar dari dataset untuk dijadikan test_wajah.jpg
            daftar_file = [f for f in os.listdir(folder_dataset) if f.endswith(('.jpg', '.jpeg', '.png'))]
            if daftar_file:
                contoh_path = os.path.join(folder_dataset, daftar_file[0])
                img_contoh = cv2.imread(contoh_path)
                cv2.imwrite(foto_test, img_contoh)
                print(f"[+] File uji otomatis disiapkan di '{foto_test}' (menyalin dari {daftar_file[0]})")
        
        if os.path.exists(foto_test):
            nama_hasil, nilai_jarak = pengenal.kenali_wajah_baru(foto_test)
            print("=== HASIL IDENTIFIKASI WAJAH ===")
            print(f"Input Foto       : {foto_test}")
            print(f"Paling Mirip Dengan: {nama_hasil}")
            print(f"Jarak Euclidean  : {nilai_jarak:.4f}")
        else:
            print(f"Sistem siap! Masukkan file foto baru dengan nama '{foto_test}' untuk mencoba deteksi.")
            
    except Exception as e:
        print(f"Terjadi Kesalahan: {e}")