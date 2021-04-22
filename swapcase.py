# sWAP CaSe


# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints


# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# Test Cases 

"""
hACKERrANK.COM PRESENTS "pYTHONIST 2".

K96.5GI.sabDH3s.6iFzxMAh5IPtmWJ4w0uJ9MOWC45eoZkhaSs73gxKoQcd90Uge02cAxPnyMWtYW'TRVcO.0VnBq.sIQ5HFhkx

hG4 KIm2ONx3x5epersw Dz.ytOVfXSxrh'MephUyRYAkHsDZOZStP'2XRv6XqcT0RkI5INrfr38 4BPUuS85OGWXNgXZPaHF1oy

OzD0ro.7xwq A.MqhqT7'evgaVjpQ36OjSwfhuMaME'SDlyjPttjr6knZURciDARzAZ.3hQeIvX'IPe875zS3su6dajlMnbQOiH37U3YG0uzy6vW4v.onodBDDREYOf3CqeHfGcCeWV0dXrmTWAUsuw'jVwFO'5n.jvKLwXaDsam'y5sVQqB5O16bn1ug1XFeg3kmOGQFjxQ524k Z0yv76b4kkaC YuW9cw8Sfjf4 ynhe N88N3N2pfJF.I4ec5PgTp0Mp6VKawzg7GctsbPmU73aERqHxvWOMxDGZI9XWnJV6Aumecv0bHopAmfeD1K vTcxkzmdypHOGcdELdXjINde.ICPhEnpr9nJVL M7uY'L0BDX0i7CNCjIt9OiE2xjXt7JkK7vdUFlp6qn3Zua5vfP'nJcbviLrwj3.VlDDkd4VQ6zV1G2sGMmTVYkzaR9z5CDujAl'zYw8jw 9VOb5dP'zT'UTLMX2u8OG5YrGrvcENXF'QhBC8Ti'KRuhuO'SLlDKuRPHxFtnXW27YY1BMN9YkQww9kloEb43'loYiSFpIPiA0f1.3RYNUEN4QSbNQMpwQPZXsVKhc.uGvGJHiU80gcvOufOI2A0LdPcwGBWjTDl4TBZaycMfCmOceYqPj gqV7wTfSkY1F4INWqlKez.Vzbf84htDJg6D4MUt 2cGy8gMQolE 3gLR.rh3s5nbzN8hqKJr4c0L48zm2Hm7ObgsDu8dlrHnDaVKLQ65a7oTyz D6MLYD.q2AQXnQHKuTxKu5Fq7iNIRZKYyYeZo8n8JwHXtDbOaEnu'4'vmAsf2XR2q0ozLdw2FVsVpKEm4KzigoxY2GOpZq3OYW8cboQoD7STPJ8B'yEGZgk0vT mBABj0xeckqn6'Ouo99aTq'LKILUYjJ3DrduZj6Gq25kHUhfskez4LjZ21jduxXVXa8EmBNQeMf1A4R1v3fqGl W4Aw2UZ0t62TM fDGTqWgfvTb1RP7wyJ
"""


def swap_case(s):
    c = ''
    sc = '."\''
    for i in s:
        if i in sc:
            c = c + i 
        elif i.isspace():
            c = c + ' '
        elif i.isdigit() :
            c = c + i
        elif i.isalpha():
            if i.isupper():
                c = c +  i.lower()
            else:
                c = c + i.upper()
        
    return c

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result