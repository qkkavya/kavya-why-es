

from ciphers.base import CipherAdapter
from ciphers.registry import register_cipher

_SBOX = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]

_PBOX_64 = [
     0, 17, 34, 51, 48,  1, 18, 35, 32, 49,  2, 19, 16, 33, 50,  3,
     4, 21, 38, 55, 52,  5, 22, 39, 36, 53,  6, 23, 20, 37, 54,  7,
     8, 25, 42, 59, 56,  9, 26, 43, 40, 57, 10, 27, 24, 41, 58, 11,
    12, 29, 46, 63, 60, 13, 30, 47, 44, 61, 14, 31, 28, 45, 62, 15,
]

_PBOX_128 = [
      0, 33, 66, 99,  96,  1, 34, 67,  64, 97,  2, 35,  32, 65, 98,  3,
      4, 37, 70, 103, 100,  5, 38, 71,  68, 101,  6, 39,  36, 69, 102,  7,
      8, 41, 74, 107, 104,  9, 42, 75,  72, 105, 10, 43,  40, 73, 106, 11,
     12, 45, 78, 111, 108, 13, 46, 79,  76, 109, 14, 47,  44, 77, 110, 15,
     16, 49, 82, 115, 112, 17, 50, 83,  80, 113, 18, 51,  48, 81, 114, 19,
     20, 53, 86, 119, 116, 21, 54, 87,  84, 117, 22, 55,  52, 85, 118, 23,
     24, 57, 90, 123, 120, 25, 58, 91,  88, 121, 26, 59,  56, 89, 122, 27,
     28, 61, 94, 127, 124, 29, 62, 95,  92, 125, 30, 63,  60, 93, 126, 31,
]

_RC = [
    0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D, 0x3B, 0x37, 0x2F,
    0x1E, 0x3C, 0x39, 0x33, 0x27, 0x0E, 0x1D, 0x3A, 0x35, 0x2B,
    0x16, 0x2C, 0x18, 0x30, 0x21, 0x02, 0x05, 0x0B, 0x17, 0x2E,
    0x1C, 0x38, 0x31, 0x23, 0x06, 0x0D, 0x1B, 0x36, 0x2D, 0x1A,
    0x34, 0x29, 0x12, 0x24, 0x08, 0x11, 0x22, 0x04, 0x09, 0x13,
    0x26, 0x0C, 0x19, 0x32, 0x25, 0x0A, 0x15, 0x2A, 0x14, 0x28,
    0x10, 0x20,
]

class _GiftBase(CipherAdapter):

    KEY_BITS    = 128
    IS_STREAM   = False
    _PBOX = []
    _KEY_OFFSET = 16
    _BIT_OFFSET = 0

    def encrypt(self, plaintext_bits, key_bits, rounds):
        n_nibbles = self.BLOCK_BITS // 4
        n_bits    = self.BLOCK_BITS
        pt_int    = self.bits_to_int(plaintext_bits)
        key_int   = self.bits_to_int(key_bits)

        state    = [(pt_int  >> (4 * i)) & 0xF for i in range(n_nibbles)]
        key      = [(key_int >> (4 * i)) & 0xF for i in range(32)]

        bits      = [0] * n_bits
        perm_bits = [0] * n_bits
        key_bits  = [0] * 128
        temp_key  = [0] * 32

        pbox       = self._PBOX
        key_off    = self._KEY_OFFSET
        bit_offset = self._BIT_OFFSET

        for r in range(rounds):

            for i in range(n_nibbles):
                state[i] = _SBOX[state[i]]

            for i in range(n_nibbles):
                for j in range(4):
                    bits[4*i+j] = (state[i] >> j) & 0x1
            for i in range(n_bits):
                perm_bits[pbox[i]] = bits[i]
            for i in range(n_nibbles):
                state[i] = 0
                for j in range(4):
                    state[i] ^= perm_bits[4*i+j] << j

            for i in range(n_nibbles):
                for j in range(4):
                    bits[4*i+j] = (state[i] >> j) & 0x1
            for i in range(32):
                for j in range(4):
                    key_bits[4*i+j] = (key[i] >> j) & 0x1

            kbc = 0
            for i in range(n_nibbles):
                bits[4*i + bit_offset]     ^= key_bits[kbc]
                bits[4*i + bit_offset + 1] ^= key_bits[kbc + key_off]
                kbc += 1

            bits[3]        ^= _RC[r] & 0x1
            bits[7]        ^= (_RC[r] >> 1) & 0x1
            bits[11]       ^= (_RC[r] >> 2) & 0x1
            bits[15]       ^= (_RC[r] >> 3) & 0x1
            bits[19]       ^= (_RC[r] >> 4) & 0x1
            bits[23]       ^= (_RC[r] >> 5) & 0x1
            bits[n_bits-1] ^= 1

            for i in range(n_nibbles):
                state[i] = 0
                for j in range(4):
                    state[i] ^= bits[4*i+j] << j

            for i in range(32):
                temp_key[i] = key[(i+8) % 32]
            for i in range(24):
                key[i] = temp_key[i]
            key[24] = temp_key[27]
            key[25] = temp_key[24]
            key[26] = temp_key[25]
            key[27] = temp_key[26]
            key[28] = ((temp_key[28] & 0xC) >> 2) | ((temp_key[29] & 0x3) << 2)
            key[29] = ((temp_key[29] & 0xC) >> 2) | ((temp_key[30] & 0x3) << 2)
            key[30] = ((temp_key[30] & 0xC) >> 2) | ((temp_key[31] & 0x3) << 2)
            key[31] = ((temp_key[31] & 0xC) >> 2) | ((temp_key[28] & 0x3) << 2)

        ct_int = sum(state[i] << (4*i) for i in range(n_nibbles))
        return self.int_to_bits(ct_int, n_bits)

@register_cipher
class Gift64_128Adapter(_GiftBase):

    CIPHER_NAME    = "gift_B64_K128"
    BLOCK_BITS     = 64
    MAX_ROUNDS     = 28
    DEFAULT_ROUNDS = 28
    _PBOX          = _PBOX_64
    _KEY_OFFSET    = 16
    _BIT_OFFSET    = 0

    def test_vectors(self):
        return [
            {"key":       0x00000000000000000000000000000000,
             "plaintext":  0x0000000000000000,
             "rounds":     28,
             "ciphertext": 0xf62bc3ef34f775ac},
            {"key":       0xfedcba9876543210fedcba9876543210,
             "plaintext":  0xfedcba9876543210,
             "rounds":     28,
             "ciphertext": 0xc1b71f66160ff587},
        ]
