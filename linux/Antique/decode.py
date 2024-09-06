# Mengambil nilai BITS dari string
bits_string = "50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32 " \
              "33 1 3 9 17 18 19 22 23 25 26 27 30 31 33 34 35 " \
              "37 38 39 42 43 49 50 51 54 57 58 61 65 74 75 79 " \
              "82 83 86 90 91 94 95 98 103 106 111 114 115 119 " \
              "122 123 126 130 131 134 135"

# Pisahkan nilai heksadesimal menjadi list
hex_values = bits_string.split()

# Konversi nilai heksadesimal ke karakter ASCII
result_string = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])

print(result_string)
