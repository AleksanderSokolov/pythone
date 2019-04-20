#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

# Провести поиск подстроки в строке
import hashlib
dict = {}

def rabin_karp_count(s):
    for len_sub in range(len(s)):
        for i in range(len(s) - len_sub):
            subs = s[i:i+len_sub+1].encode('utf-8')
            if subs:
                h_subs = hashlib.sha1(subs).hexdigest()
                if h_subs:
                    if subs in dict:
                        dict.__setitem__(subs, dict[subs] + 1)
                    else:
                        dict.__setitem__(subs, int(1))
    return dict

print(rabin_karp_count("wewewe"))

#{b'w': 3, b'e': 3, b'we': 3, b'ew': 2, b'wew': 2, b'ewe': 2, b'wewe': 2, b'ewew': 1, b'wewew': 1, b'ewewe': 1, b'wewewe': 1}
# Как победить 2 wewe, не придумал еще.