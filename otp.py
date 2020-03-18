"""
Code to export
- Joe Aczel
18/3/2020
"""
import string

def merge(list1, list2):
    """
    Merge two lists into a list of tuples
    """
    return [(list1[i], list2[i]) for i in range(0, len(list1))]

def decrypt(plain, crypt):
    """
    encrypted - expected_text = otp
    OR
    encrypted - otp = plain text
    """
    otp = list()
    for i, c in enumerate(plain):
        num = ((otp_chars[crypt[i]] - otp_chars[plain[i]]) % 26)
        otp.append(otp_nums[num])
    return ''.join(otp)

# Global Variables
letters = string.ascii_lowercase[:26]
numbers = list(range(1, 27))
otp_chars = dict(merge(letters, numbers))
otp_nums = dict(merge(numbers, letters))


if __name__ == "__main__":
    crypt = input("Enter part of the encrypted text you think you can decode: ")
    plain = input("Enter what you think the text maps to: ")
    print("Plain text expected is", plain)
    print("Encrypted text is", crypt)
    otp = decrypt(plain.lower(), crypt.lower())
    print("Great! Your OTP is", otp)
    other_string = input("Enter some other encrypted text: ")

    print("Subtracting", otp, "from", other_string)

    decrypted = decrypt(otp.lower(), other_string.lower())

    print("Encrypted is", other_string)
    print(other_string, "-", otp, "=", decrypted)
