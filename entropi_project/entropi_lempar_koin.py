import math

def entropy(probabilities):
    H = 0
    for p in probabilities:
        if p > 0:
            H -= p * math.log2(p)
    return H

# ======================
# 1. Koin Adil (0.5 , 0.5)
# ======================
p_fair = [0.5, 0.5]
H_fair = entropy(p_fair)

# =========================
# 2. Koin Tidak Adil (0.8 , 0.2)
# =========================
p_unfair = [0.8, 0.2]
H_unfair = entropy(p_unfair)

print("Kasus Entropi: Lempar Koin")
print(f"Entropy Koin Adil (0.5, 0.5): {H_fair:.3f} bits")
print(f"Entropy Koin Tidak Adil (0.8, 0.2): {H_unfair:.3f} bits")
