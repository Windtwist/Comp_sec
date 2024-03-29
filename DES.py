#IP
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
    ]
# PC1
pc1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
    ]
#LSH for each round
shift_schedule = [1, 1, 2, 2,
                  2, 2, 2, 2,
                  1, 2, 2, 2,
                  2, 2, 2, 1
                  ]
#PC2
pc2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
    ]

#32 -  > 48
expand = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

#S as in presentation
s_func = [
    #S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    #S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    #S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    #S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    #S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    #S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    #S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    #S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
#P
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
    ]
#IP^-1
ip_inv = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def binary_to_ascii(bin):
    ascii = ""
    for i in range(0, len(bin), 8):  #8 bits
        byte = bin[i:i + 8]  #Extract byte
        ascii_char = chr(int(byte, 2)) #bin to int -> char
        ascii += ascii_char
    return ascii

def permute_ip(bin):
    ip_res = ''.join(bin[IP[i] - 1] for i in range(64)) #index of the bit to be taken from the original binary string
    return ip_res

def LSH(bin, shift):
    #perform LSH on bin input
    return bin[shift:] + bin[:shift]
def gen_keys():

    key = "0100110001001111010101100100010101000011010100110100111001000100"
    pc1_key = ""
    for bit in pc1:
        pc1_key += key[bit - 1] #iterate over each position -> get correspoding bit

    #56-bit -> two 28-bit
    c0 = pc1_key[:28]
    d0 = pc1_key[28:]

    keys = []
    for num in range(16):
        #LSH on c0 and d0
        c0 = LSH(c0, shift_schedule[num])
        d0 = LSH(d0, shift_schedule[num])

        #combine c0 and d0
        cd = c0 + d0

        round_key = ""  #pc2
        for bit in pc2:
            round_key += cd[bit - 1]

        #store keys in list
        keys.append(round_key)
        print(num+1, round_key,"\n")
    return keys

def decryption(sol):
    #lists to store round keys
    round_keys = gen_keys()

    # Apply Initial Permutation
    IP_int = permute_ip(sol)

    lpt = IP_int[:32]
    rpt = IP_int[32:]

    for num in range(16):
        #32 -> 48
        expanded = [rpt[i - 1] for i in expand]

        # Convert the result back to a string for better visualization
        expanded_conn = ''.join(expanded) #concat string

        key = round_keys[15 - num]

        #XOR key and result
        xor = ''
        for i in range(48):
            xor += str(int(expanded_conn[i]) ^ int(key[i]))

        #48 bit -> 8 x6 bits
        groups = [xor[i:i + 6] for i in range(0, 48, 6)]

        string_groups = ''.join(groups) #concat string
        print(num+1, "function f: ", string_groups)

        #s_func bits string
        s_sub = ''

        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            #row and column
            row = int(groups[i][0] + groups[i][-1], 2)
            col = int(groups[i][1:-1], 2)

            #  value
            s = s_func[i][row][col]

            #4-bit binary string
            s_sub += format(s, '04b')

        #P permutation
        p_perm = []

        #go over each index in P table
        for i in P:
            p_perm.append(s_sub[i - 1])

        #list of bits for XOR
        lpt_l = list(lpt)

        #XOR operation
        rpt_2 = [str(int(lpt_l[i]) ^ int(p_perm[i])) for i in range(32)]

        rpt_conn = ''.join(rpt_2)

        lpt = rpt
        rpt = rpt_conn

    print('\n')
    finl_sol = rpt + lpt

    cipher = []
    for i in range(64): #ip_inv
        cipher.append(finl_sol[ip_inv[i] - 1])

    final_str = ''.join(cipher)

    print("final cipher after inv: ", final_str)

    #bin -> ascii
    decrypted = binary_to_ascii(final_str)
    print("Decryption of Cipher :", decrypted)

    return decrypted

dec = decryption("1100101011101101101000100110010101011111101101110011100001110011")


