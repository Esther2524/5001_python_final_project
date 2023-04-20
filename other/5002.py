

def get_sequence(n):

    binary_of_n = ""

    while n >= 1:
        if n % 2 == 0:
            binary_of_n = "0" + binary_of_n
        else:
            binary_of_n = "1" + binary_of_n
        n = n // 2
    
    sequence = []

    for i in binary_of_n[1:]:
        if i == "0":
            sequence.append("Left")
        else:
            sequence.append("Right")


    print(binary_of_n)
    print(sequence)


        




def main():

    get_sequence(34)

    


main()