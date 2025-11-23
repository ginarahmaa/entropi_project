from math import log2
import matplotlib.pyplot as plt


def entropy(p):
    """
    Menghitung entropi untuk distribusi biner [p, 1-p]
    p = probabilitas sisi 'angka', 1-p = sisi 'gambar'
    """
    if p == 0 or p == 1:
        return 0  
    return -(p * log2(p) + (1 - p) * log2(1 - p))

probs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

ents = [entropy(p) for p in probs]

plt.plot(probs, ents, marker='o')
plt.title("Entropi pada Probabilitas Lempar Koin")
plt.xlabel("Probabilitas Sisi 'Angka' (p)")
plt.ylabel("Nilai Entropi (bits)")
plt.grid(True)
plt.show()
