import numpy as np

def svd_print(U, S, Vt):
    S_idx = np.argmax(S) #Returns index of highest S value

    print(f"——\tU\t——\n{U}")
    print(f"——\tS\t——\n{S} —— Largest is S[{S_idx}]")
    for i in range(len(S)):
        if i == S_idx:
            print(f"——\t*Vᵀ[{i}]\t——\n{Vt[i]}")
        else:    
            print(f"——\tVᵀ[{i}]\t——\n{Vt[i]}")