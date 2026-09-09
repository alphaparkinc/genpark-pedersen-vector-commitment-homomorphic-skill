import hashlib

PRIME = 21888242871839275222246405745257275088548364400416034343698204186575808495617

class PedersenVectorCommitment:
    """Pedersen Vector Commitment with Additive Homomorphism."""
    def __init__(self, vector_len=4):
        self.p = PRIME
        self.g = [self._hash_to_field(f"G_{i}") for i in range(vector_len)]
        self.h = self._hash_to_field("H_blinding")

    def _hash_to_field(self, name):
        h = int(hashlib.sha256(name.encode()).hexdigest(), 16)
        return (h % (self.p - 2)) + 1

    def commit(self, vector, blinding):
        val = (blinding * self.h) % self.p
        for gi, vi in zip(self.g, vector):
            val = (val + (gi * vi)) % self.p
        return val

    def add_commitments(self, comm1, comm2):
        return (comm1 + comm2) % self.p
