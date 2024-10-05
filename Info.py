def hidden_info():
    part1 = chr(112) + chr(97) + chr(117) + chr(108)
    part2 = chr(119) + chr(105) + chr(108) + chr(100) + chr(101) + chr(110) + chr(98) + chr(101) + chr(114) + chr(103)
    part3 = chr(57) + chr(54)
    part4 = chr(64)
    part5 = chr(103) + chr(109) + chr(97) + chr(105) + chr(108)
    part6 = chr(46) + chr(99) + chr(111) + chr(109)

    return part1 + part2 + part3 + part4 + part5 + part6

def main():
    output = hidden_info()
    print(output)

if __name__ == "__main__":
    main()
