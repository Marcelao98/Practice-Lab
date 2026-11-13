#Okay now for exercise 4 hexadecimal huh, now that is a fun one 
hexmap = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
}

def hex_convert():
     hex_number = input("Type a number in hex")
     dec_number = 0
     for index, digit in enumerate(hex_number[::-1]):
          print(f"Index {index}, digit is {digit}")
          dec_number += hexmap[digit]*10**(index)
     print(dec_number)      


    
hex_convert()
