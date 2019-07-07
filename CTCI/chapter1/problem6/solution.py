"""
String Compression
implement a method to perform basic string compression using counts of repeated characters. so aabcccccaaa would become a2b1c5a3. if the compressed
string would not become smaller than the original string, your method should return the original string
"""

def compress_string(s):
    compressed = [s[0]]
    curr_count = 1
    curr_letter = s[0]
    for i in range(1, len(s)):
        if curr_letter != s[i]:
            compressed.append(str(curr_count))
            curr_letter = s[i]
            curr_count = 1
            compressed.append(s[i])
        else:
            curr_count += 1
    compressed.append(str(curr_count))
    compressed = ''.join(compressed)
    if len(compressed) >= len(s):
        return s
    else:
        return compressed


def main():
     print(compress_string('aabcccccaaa'))
main()    