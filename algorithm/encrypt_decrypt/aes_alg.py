from __future__ import print_function
import os
import random
import string
import base64
from Crypto.Cipher import AES


class AES_ECB(object):

    def __init__(self, secret="", block_size=16):
        # Block size (bytes):
        # 16(AES-128)
        # 24(AES-192)
        # 32(AES-256)
        self.BS = block_size

        if secret:
            self.secret = secret
        else:
            # self.secret = os.urandom(self.BS)
            self.secret = ''.join(random.sample(string.ascii_letters+string.digits, self.BS))
        print("secret:", self.secret)

        self.cipher = AES.new(self.secret, AES.MODE_ECB)
        self.padding_char = None

    # Pad text length to multiple of block size
    # Shortcut:
    # pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    def _pad(self, s):
        num_to_pad = self.BS - len(s) % self.BS

        # Note: padding char is the ascii char with the value of num_to_pad
        padding_char = chr(num_to_pad)
        padding = num_to_pad * padding_char

        return s + padding

    # Shortcut:
    # unpad = lambda s: s[0:-ord(s[-1])]
    def _unpad(self, s):
        return s[0:-ord[-1]]

    def encrypt(self, plaintext):
        encrypted_text = self.cipher.encrypt(self._pad(plaintext))
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = self.cipher.decrypt(ciphertext)
        decrypted_text = self._unpad(decrypted_text)
        return decrypted_text


if __name__ == '__main__':
    # aes_ecb = AES_ECB('1111111111111111')
    aes_ecb = AES_ECB()
    ciphertext = aes_ecb.encrypt("shit")
    print(ciphertext)
    print(base64.b64encode(ciphertext))


