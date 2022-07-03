from asyncio.windows_events import NULL
import json
import math
import struct
inputFilePath = "input.thing_text"
outputFilePath = "output.thing_bin"
inputFileContent = ""

with open(inputFilePath) as fid:
    lines = fid.readlines()
    inputFileContent = "".join(lines)

data = json.loads(inputFileContent)

obstacles = data["Obstacles"]

FORMATTER_32_BIT = '{:032b}'
FORMATTER_8_BIT = '{:08b}'

f = open(outputFilePath, "wb")

def writeInt32(number):
    #turn number into binary
    bR = number.to_bytes(4, byteorder='big')
    bR = [bR[3], bR[2], bR[1], bR[0]]
    f.write(bytes(bR))


def writeBoolean(value):
    binaryByte = [int(value == True)]
    #turn bool into binary
    f.write(bytes(binaryByte))

def writeSingle(inp):
    if inp != 0:
        # #see https://en.wikipedia.org/wiki/Single-precision_floating-point_format
        # #get rid of sign so that math isnt affected, its added back alter
        # value = abs(inp)
        # decimalBinary = ""
        # decimal = value - math.floor(value)
        # currentDecimal = decimal
        # #convert fraction into binary fraction, limiting at precision limit (23 repetitions)
        # for i in range(0, 23):
        #     currentDecimal = currentDecimal * 2
        #     decimalBinary += str(int(currentDecimal >= 1))
        #     if currentDecimal >= 1:
        #         currentDecimal -= 1
        #     if currentDecimal == 0:
        #         break
            
        # #get whole value
        # wholeBinary = str(bin(math.floor(value - decimal)))[2:]
        # #get normalized exponent (offset from 127)
        # normalExponent = 127 + (len(wholeBinary) - 1)
        # #convert exponent into binary
        # exponentBinary = str(bin(normalExponent))[2:]
        # #shift so that only 1 digit remains before decimal point
        # fractionBinary = wholeBinary[1:] + decimalBinary

        # #concat all parts together into an unrounded (and thus unlimited in size) set of bits
        # unroundedBinary = str(int(inp < 0)) + exponentBinary + fractionBinary
        
        # binaryRep = ""
        # #if less then len 32 append 0s to end to get to 32 bits
        # if len(unroundedBinary) < 32:
        #     binaryRep = unroundedBinary + "0" * (32 - len(binaryRep))
        # #if greater then 32 round to 32 bits 1s round up the next digit, very simply so if we get any 1 then the rest chain causing the final bit to be 1
        # #it should not round like this, this is not how it works but its a quick implementation
        # elif len(unroundedBinary) > 32:
        #     for i in range(len(unroundedBinary) - 1, 32, -1):
        #         if unroundedBinary[i] == "1":
        #             binaryRep = unroundedBinary[0:31] + "1"
        #             break
        #     else:
        #         binaryRep = unroundedBinary
        binaryRep =''.join('{:0>8b}'.format(c) for c in struct.pack('!f', inp))
        #store binary as 2 chunks of 16
        sections = ["",""]
        for i in range(8, 33, 8):
            byte = binaryRep[i-8:i]
            sections[(i - 1) // 16] += byte

        #f.write(chr(int(bytes[1][0:8], 2))) #1,2
        #write in order of D C B A
        for section in reversed(sections):
            sectionBytes = [int(section[8:16], 2), int(section[0:8], 2)]
            f.write(bytes(sectionBytes))

    else:
        #Empty float print all null bytes
        emptyBytes = [0, 0, 0, 0]
        f.write(bytes(emptyBytes))

#collect R,G,B, and A and write them into the binary
def writeColor(colorTable):
    r = colorTable["R"]
    g = colorTable["G"]
    b = colorTable["B"]
    a = colorTable["A"]
    colorBytes = [r, g, b, a]
    f.write(bytes(colorBytes))
    
def writeString(string):
    #add length of string to array
    stringBytes = [len(string)]
    #add each character to array to be converted
    for c in string:
        stringBytes.append(ord(c))
    #write converting each into bytes representation
    f.write(bytes(stringBytes))

def writeStringAllowNull(string):
    #if string is null print null (shows engine no string values to read)
    if string == NULL or string == "":
        writeBoolean(False)
    #if string is not null print true to show to read string and then read string like normal
    else:
        writeBoolean(True)
        writeString(string)



FILE_VERSION = 4
print("version")
writeInt32(FILE_VERSION)
ITEM_COUNT = len(obstacles)
print("Item Count")
print(ITEM_COUNT)
writeInt32(ITEM_COUNT)

for item in obstacles:
# for i in range(0,17):
#     item = obstacles[i]
    print(item["Name"] + (item["Comments"] if "Comments" in item else ""))
    writeBoolean(True)

    writeBoolean(item["ActivateAtRange"])
    writeSingle(item["ActivationRange"])
    writeBoolean(item["Active"])
    writeSingle(item["Angle"])

    writeInt32(len(item["AttachedIDs"]))
    for attachedID in item["AttachedIDs"]:
        writeInt32(attachedID) 

    writeInt32(item["AttachToID"])
    writeBoolean(item["Collision"])
    writeColor(item["Color"])
    writeStringAllowNull(item["Comments"] if "Comments" in item else "")
    writeString(item["DataType"])
    writeBoolean(item["FlipHorizontal"])
    writeBoolean(item["FlipVertical"])
    writeBoolean(item["Friendly"])

    writeInt32(len(item["GroupNames"]))
    for groupName in item["GroupNames"]:
         writeStringAllowNull(groupName)

    writeSingle(item["HealthFraction"])
    writeStringAllowNull(item["HelpTextId"] if "HelpTextId" in item else "")
    writeInt32(item["Id"])
    writeBoolean(item["IgnoreGridManager"])
    writeBoolean(item["Invert"])
    writeBoolean(item["Invulnerable"])
    writeColor(item["LightColor"])
    writeSingle(item["LightIntensity"])
    writeSingle(item["LightRadius"])
    writeSingle(item["LightZ"])

    writeSingle(item["Location"]["X"])
    writeSingle(item["Location"]["Y"])
    if "Material" in item and item["Material"] != None:
        writeBoolean(True)
        writeSingle(item["Material"]["Ambient"])
        writeSingle(item["Material"]["Diffuse"])
        writeSingle(item["Material"]["Directionality"])
    else:
        writeBoolean(False)

    writeStringAllowNull(item["Name"] if "Name" in item else "")
    
    writeSingle(item["OffsetZ"])
    writeSingle(item["ParallaxAmount"])

    if "Points" in item:
        writeInt32(len(item["Points"]))
        for point in item["Points"]:
            writeSingle(point["X"])
            writeSingle(point["Y"])
    else:
        writeInt32(0)
    
    writeSingle(item["Scale"])
    writeSingle(item["SkewAngle"])
    writeSingle(item["SkewScale"])

    writeInt32(item["SortIndex"])

    writeBoolean(item["UseAttackAI"])
    writeBoolean(item["UseMoveAI"])
    writeBoolean(item["UseTargetAI"])


f.close()