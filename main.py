import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        # Generate hash values based on item
        return [mmh3.hash(item, seed) % self.size for seed in range(self.num_hashes)]

    def add(self, item):
        # Set bits at hashed positions
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        # Check if all bits at hashed positions are set
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))

# Example Usage
size = 1000  # Size of the bit array
num_hashes = 7  # Number of hash functions

bloom = BloomFilter(size, num_hashes)
bloom.add("hello")
bloom.add("world")

print(bloom.check("hello"))  # Should return True
print(bloom.check("world"))
