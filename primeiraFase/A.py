N, A, B = input().split()

avgSticker = float((int(A) + int(B))/2)
avgPacket = float(int(N)/avgSticker)
print("%.5f" % avgPacket)
