from client import PedersenVectorCommitment

def main():
    print("=== Testing Pedersen Vector Commitment ===")
    pvc = PedersenVectorCommitment(vector_len=3)
    v1 = [10, 20, 30]
    r1 = 5
    c1 = pvc.commit(v1, r1)

    v2 = [1, 2, 3]
    r2 = 4
    c2 = pvc.commit(v2, r2)

    # Homomorphic addition: c1 + c2 == commit(v1 + v2, r1 + r2)
    c_sum = pvc.add_commitments(c1, c2)
    c_expected = pvc.commit([11, 22, 33], 9)
    print("Homomorphic sum matches:", c_sum == c_expected)
    assert c_sum == c_expected

    print("Pedersen Vector Commitment verified successfully!")

if __name__ == '__main__':
    main()
