import sys

# ======== Input ============
_structure = []
_out = []
while(1):
    input_layer = input("Input을 입력해주세요 EX) -1 28 28 1\n:" )
    l = input_layer.split(" ")
    if len(l) == 4:
        b_size =int(l[0])
        I_w = int(l[1])
        I_h = int(l[2])
        I_c = int(l[3])
        l = [b_size, I_w, I_h, I_c]

        _out.append(l)
        break
    elif input_layer =='q':
        sys.exit()
while(1):
    layer_name = input("Conv or Maxpool or undo EX)conv, maxpool\n:")
    if layer_name[:4] =='conv':
        s = layer_name.split(" ")
        if len(s) ==0:
            Channel = input("Channel : ")
            if Channel.isdigit() == False:
                print("Wrong Value of Channel!")
                continue
            else:
                if int(Channel)<=0:
                    print("Wrong Value of Channel!")
                    continue
                else:
                    Channel = int(Channel)
            Kernel = input("Kernel : ")
            if Kernel.isdigit() == False:
                print("Wrong Value of Kernel!")
                continue
            else:
                if int(Kernel) <= 0 or int(Kernel)%2 ==0:
                    print("Wrong Value of Kernel!")
                    continue
                else:
                    Kernel = int(Kernel)
            Stride = input("Stride : ")
            if Stride.isdigit() == False:
                print("Wrong Value of Stride!")
                continue
            else:
                if int(Stride) <= 0:
                    print("Wrong Value of Stride!")
                    continue
                else:
                    Stride = int(Stride)
            Padding = input("Padding : ")
            if Padding.isdigit() == False:
                print("Wrong Value of Padding!")
                continue
            else:
                if int(Padding) < 0:
                    print("Wrong Value of Padding!")
                    continue
                else:
                    Padding = int(Padding)
        elif len(s) == 5:
            Channel = s[1]
            if Channel.isdigit() == False:
                print("Wrong Value of Channel!")
                continue
            else:
                if int(Channel) <= 0:
                    print("Wrong Value of Channel!")
                    continue
                else:
                    Channel = int(Channel)
            Kernel = s[2]
            if Kernel.isdigit() == False:
                print("Wrong Value of Kernel!")
                continue
            else:
                if int(Kernel) <= 0 or int(Kernel) % 2 == 0:
                    print("Wrong Value of Kernel!")
                    continue
                else:
                    Kernel = int(Kernel)
            Stride = s[3]
            if Stride.isdigit() == False:
                print("Wrong Value of Stride!")
                continue
            else:
                if int(Stride) <= 0:
                    print("Wrong Value of Stride!")
                    continue
                else:
                    Stride = int(Stride)
            Padding = s[4]
            if Padding.isdigit() == False:
                print("Wrong Value of Padding!")
                continue
            else:
                if int(Padding) < 0:
                    print("Wrong Value of Padding!")
                    continue
                else:
                    Padding = int(Padding)

        _structure.append([layer_name.split(" ")[0], "Channel: {}".format(Channel), "Kernel: {}x{}".format(Kernel, Kernel), "Stride: {}".format(Stride), "Padding: {}".format(Padding)])
        result =[b_size, (l[1]-Kernel+2*Padding)/Stride+1, (l[2]-Kernel+2*Padding)/Stride+1,Channel]
        temp = l
        l = result
        _out.append(result)
    elif layer_name[:7] =='maxpool':
        s = layer_name.split(" ")
        if len(s) == 0:
            Kernel = input("Kernel : ")
            if Kernel.isdigit() == False:
                print("Wrong Value of Kernel!")
                continue
            else:
                if int(Kernel) <= 0 :
                    print("Wrong Value of Kernel!")
                    continue
                else:
                    Kernel = int(Kernel)
            Stride = input("Stride : ")
            if Stride.isdigit() == False:
                print("Wrong Value of Stride!")
                continue
            else:
                if int(Stride) <= 0:
                    print("Wrong Value of Stride!")
                    continue
                else:
                    Stride = int(Stride)
        elif len(s) == 3:
            Kernel = s[1]
            if Kernel.isdigit() == False:
                print("Wrong Value of Kernel!")
                continue
            else:
                if int(Kernel) <= 0 :
                    print("Wrong Value of Kernel!")
                    continue
                else:
                    Kernel = int(Kernel)
            Stride = s[2]
            if Stride.isdigit() == False:
                print("Wrong Value of Stride!")
                continue
            else:
                if int(Stride) <= 0:
                    print("Wrong Value of Stride!")
                    continue
                else:
                    Stride = int(Stride)
        _structure.append([layer_name.split(" ")[0], "Kernel: {}x{}".format(Kernel,Kernel), "Stride: {}".format(Stride)])
        result = [b_size, (l[1] - Kernel) / Stride + 1, (l[2] - Kernel) / Stride + 1,
                  l[3]]
        temp = l
        l = result
        _out.append(result)
    elif layer_name == "undo":
        _structure.pop(-1)
        _out.pop(-1)
        l = temp
    elif layer_name =='q':
        break
    # elif layer_name =='maxpool':
#
# print(_structure)
# print(_out)
print("구조 살펴보기===============")
for i in range(len(_out)):

    if i >0:
        print(_structure[i-1])
    print(_out[i])