def hidden_info():
    part1 = chr(84) + chr(101) + chr(115) + chr(116) + chr(105) + chr(110) + chr(103)
    part2 = chr(32)
    part3 = chr(116) + chr(101) + chr(115) + chr(116) + chr(105) + chr(110) + chr(103)
    part4 = chr(32)
    part5 = chr(49) + chr(50) + chr(51) 
    part6 = chr(46) + chr(46) + chr(46)

    return part1 + part2 + part3 + part4 + part5 + part6

def main():
    output = hidden_info()
    print(output)

if __name__ == "__main__":
    main()
