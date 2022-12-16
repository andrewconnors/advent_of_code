BUFFER_SIZE = 14
if __name__ == "__main__":
    with open('signal_locking.txt', 'r') as input:
        for line in input:
            print(line)
            ptr_a, ptr_b = 0, 0

            while (ptr_b - ptr_a) < BUFFER_SIZE:
                ptr_b += 1
            while ptr_b < len(line):
                if len(set(line[ptr_a:ptr_b])) == BUFFER_SIZE:
                    print(f"first unique 4 char section happens after receiving char: {ptr_b}")
                    break; 
                ptr_a += 1
                ptr_b += 1
        



