from heapq import heappush, heappop, heapify
import collections
from collections import defaultdict
from tkinter import *
import math


def setupWindow():
    # Deleting previous values
    l.grid(row=3, column=0, sticky='w')
    resultEntry.grid(row=4, column=0)



    resultEntry.config(state=NORMAL)
    resultEntry.tag_delete("myTags")
    resultEntry.delete(1.0, END)


    l2.grid(row=3, column=2, sticky='w')
    resultEntry2.grid(row=4, column=2)
    l11.grid(row=5, column=0, sticky='w')
    l22.grid(row=5, column=1, sticky='w')
    l33.grid(row=6, column=0, sticky='w')


    resultEntry2.config(state=NORMAL)
    resultEntry2.delete(1.0, END)




def formatString(event):
    setupWindow()
    str1 = str(inputString.get())
    symb2freq = collections.Counter(str1)

    prevtotal = getFrequencies(symb2freq)

    huff = encode(symb2freq)

    print("Carácter\tFrecuencia\tCódigo")
    # Insert in window
    resultEntry.insert(INSERT, "Carácter\tFrecuencia\tCódigo\n")
    total = 0
    for p in huff:
        resultEntry.insert(INSERT, "  %s\t  %s\t  %s\n" % (p[0], symb2freq[p[0]], p[1]))
        total += len(p[1]) * symb2freq[p[0]]
        print("%s\t\t%s\t\t%s" % (p[0], symb2freq[p[0]], p[1]))
    tvar.set('Total bits = %s' % total)

    efficiency = total/prevtotal

    resultVar.set('Efficiency = %s' % efficiency)


def getFrequencies(inputCnt):
    codeLength = math.ceil(math.log(len(inputCnt), 2))
    c = 0
    total = 0
    resultEntry2.insert(INSERT, "Carácter\tFrecuencia\tCódigo\n")
    for key, val in inputCnt.most_common():
        st = ('{0:b}'.format(c)).zfill(codeLength)
        resultEntry2.insert(INSERT,"  %s\t  %s\t  %s\n" % (key, val, st))
        c += 1
        total += val * len(st)
    tvar2.set('Total bits = %s' % total)
    return total

def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def buildWindow():
    root = Tk()


    l1 = Label(root, text="Enter the message to encode:")
    l1.grid(row=1, column=0)
    global inputString
    inputString = Entry(root, width=50)
    inputString.grid(row=2, column=0)


    submitButton = Button(root, text="Submit")
    submitButton.bind("<Button-1>", formatString)
    submitButton.grid(row=2, column=1, sticky='e')

    global l
    l = Label(root, text="Encoded Message:")
    global resultEntry
    resultEntry = Text(root, height=12, width=33)

    global l2
    l2 = Label(root, text="Non huffman encoding:")
    global resultEntry2
    resultEntry2 = Text(root, height=12, width=33)

    global tvar, tvar2, resultVar
    tvar = StringVar()
    tvar2 = StringVar()
    resultVar = StringVar()

    global l11
    l11 = Label(root, textvariable=tvar)

    global l22
    l22 = Label(root, textvariable=tvar2)

    global l33
    l33 = Label(root, textvariable=resultVar)


    root.mainloop()

# aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff
# AAAAAAAAAAEEEEEEEEEEEEEEEIIIIIIIIIIIISSSTTTTPPPPPPPPPPPPP\n
buildWindow()