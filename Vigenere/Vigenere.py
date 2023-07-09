class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()  # 비밀키를 대문자로 변환하여 저장

    def encrypt(self, message):
        encrypted_message = ''
        key_length = len(self.key)
        key_index = 0

        for char in message:
            if char.isalpha():
                key_char = self.key[key_index]
                key_offset = ord(key_char) - ord('A')
                ascii_offset = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - ascii_offset + key_offset) % 26 + ascii_offset)

                encrypted_message += encrypted_char

                key_index = (key_index + 1) % key_length  # 다음 키 문자로 이동
            else:
                encrypted_message += char

        return encrypted_message

    def decrypt(self, ciphertext):
        decrypted_message = ''
        key_length = len(self.key)
        key_index = 0

        for char in ciphertext:
            if char.isalpha():
                key_char = self.key[key_index]
                key_offset = ord(key_char) - ord('A')
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - ascii_offset - key_offset) % 26 + ascii_offset)

                decrypted_message += decrypted_char

                key_index = (key_index + 1) % key_length  # 다음 키 문자로 이동
            else:
                decrypted_message += char

        return decrypted_message
key = 'SKY'  # 비밀키 설정
message = "johnwick"  # 암호화할 메시지

cipher = VigenereCipher(key)  # VigenereCipher 클래스 인스턴스 생성
ciphertext = cipher.encrypt(message)  # 메시지 암호화
print("암호문:", ciphertext)

decrypted_message = cipher.decrypt(ciphertext)  # 암호문 복호화
print("복호화된 메시지:", decrypted_message)
