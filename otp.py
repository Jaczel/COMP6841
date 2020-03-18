"""
This code supplements my blog post discussing One Time Pads:
https://www.openlearning.com/u/josephaczel-q5v7qm/blog/
Code to help understand how decoding an OTP can be used to decrypt other
messages that use the same OTP.
Example usage:
String 1: LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl
String 3: UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg

The first three characters of String 1 could possibly be the word 'The'.
The first three characters of String 3 could be another word determined
by subtracting the OTP found from the first three letters of string 1.

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
    crypt = input("Enter part of the encrypted text you think " +
                  "you can decode (e.g. Lpa): ")
    plain = input("Enter what you think the text maps to (e.g. The): ")
    print("Plain text expected is", plain)
    print("Encrypted text is", crypt)
    otp = decrypt(plain.lower(), crypt.lower())
    print("Great! Your OTP is", otp)
    other_string = input("Enter text from another encrypted " +
                         "string with the letters in the same " + 
                         "place as the first(e.g. string 3, 'Uij': ")

    print("Subtracting", otp, "from", other_string)

    decrypted = decrypt(otp.lower(), other_string.lower())

    print("Encrypted is", other_string)
    print(other_string, "-", otp, "=", decrypted)
