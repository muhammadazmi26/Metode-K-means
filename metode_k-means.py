#
# Python Version : 3.7.4 
#
# Rabu, 31 Maret 2021
#

import numpy as np
import os

def get_dataset() :
    filename = os.path.dirname(__file__) + "\dataset.csv"  # data balita berisi berat badan dan tinggi badan yang telah di normalisasi
    dataset = np.genfromtxt(filename, delimiter=",")   # dataset bertipe numpy array
    print("DATA POINT :", dataset)
    return dataset

def get_centroids() :  # kembalian bertipe numpy array
    centroids = []
    centroids.append([0.92, 1.00]) # Gizi Buruk(C1)
    centroids.append([1.00, 0.46]) # Gizi Kurang(C2)
    centroids.append([0.35, 0.63]) # Gizi Baik(C3)
    centroids.append([0.58, 0.13]) # Gizi Lebih(C4)
    centroids.append([0, 0.08])    # Obesitas(C5)
    return np.array(centroids)
    
def hitung_euclidean_distance(dataset, centroid):
    return np.sqrt(np.sum((dataset - centroid)**2))

def iterasi_k_means(dataset, centroid, panjang_dataset, panjang_centroid) :

    dataset_label = []
    label_cluster = []
    for i in range(panjang_dataset): # 50 X
        hasil_euclid = []
        for j in range(panjang_centroid): # 5 X
            hasil_euclid.append(hitung_euclidean_distance(dataset[i], centroid[j])) 

        nilai_terkecil = min(hasil_euclid)
        index_nilai_terkecil = hasil_euclid.index(min(hasil_euclid))
        label_cluster.append(index_nilai_terkecil)
        dataset_label.append([[i],[index_nilai_terkecil]])  # array dua dimensi diappend lagi sehingga jadi array 3 dimensi

    # print("DATASET LABEL :", dataset_label) # urutan hasil pengelompokan/cluster tiap dataset (data 1 -> data 50)

    # mendapatkan indeks label centroid
    indeks_label = []
    for i in range(panjang_centroid):
        for j in range(panjang_dataset):
            if i in dataset_label[j][1] : 
                indeks_label.append([i, j])
    # print("INDEKS LABELL :", indeks_label)

    # mencari centroid baru
    new_centroid = []
    for y in range(panjang_centroid):
        centroidbaru = 0
        for x in range(panjang_dataset):
            if indeks_label[x][0] == y :
                centroidbaru = centroidbaru + dataset[indeks_label[x][1]]  # dataset[indeks_label[x][1] adalah array dua dimensi, sehingga otomatis variabel centroid baru berubah jadi array dua dimensi juga

        temp = centroidbaru/(label_cluster.count(y))  # count() untuk mendapatkan jumlah masing2 label/cluster
        new_centroid.append(temp)

    print("CENTROID BARU :", new_centroid)
    return new_centroid, label_cluster
    
# START PROGRAM
dataset = get_dataset()
centroid = get_centroids() # centroid awal, variabel akan berubah seiring perulangan k-means
panjang_dataset  = len(dataset)
panjang_centroid = len(centroid)

print("CENTROID AWAL :", centroid)

temp_centroid = np.array("")
ulang = True
while ulang :
    [centroid, label_cluster] = iterasi_k_means(dataset, centroid, panjang_dataset, panjang_centroid)
    if np.array_equal(centroid, temp_centroid) == True : # jika centroid lama SAMA DENGAN centroid baru, maka variabel ulang akan False ataupun perulangan while berhenti.
        ulang = False
    temp_centroid = centroid

print("----------------------------------------------------")
print("------------------ HASIL CLUTERING -----------------")
print("----------------------------------------------------")

for i in range(panjang_dataset):
    # Tampilakn Hasil Cluster Akhir
    print("DATASET Ke", i , ":",dataset[i], "| Cluster :", label_cluster[i])










