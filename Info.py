def hidden_info():
    part1 = chr(87) + chr(101) + chr(108) + chr(99) + chr(111) + chr(109) + chr(101)
    part2 = chr(32) + chr(116) + chr(111) + chr(32)
    part3 = chr(116) + chr(104) + chr(101) + chr(32)
    part4 = chr(72) + chr(105) + chr(100) + chr(100) + chr(101) + chr(110) + chr(32)
    part5 = chr(80) + chr(114) + chr(111) + chr(106) + chr(101) + chr(99) + chr(116) + chr(33)
    part6 = chr(32) + chr(72) + chr(97) + chr(118) + chr(101) + chr(32) + chr(102) + chr(117) + chr(110) + chr(126)

    return part1 + part2 + part3 + part4 + part5 + part6

def main():
    output = hidden_info()
    print(output)

if __name__ == "__main__":
    main()
