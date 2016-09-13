import os
from tkinter import *
from tkinter.ttk import *
from An import *

path = os.path.dirname(__file__) + '/'


def decrypt(m, n):
    s = ''

    for c in m:
        i = ord(c)

        if i in range(97, 123):
            i -= 97
            i = (i - n) % 26
            i += 97
            s += chr(i)

        elif i in range(65, 91):
            i -= 65
            i = (i - n) % 26
            i += 65
            s += chr(i)

        else:
            s += c

    return s


def cryptanalysis():
    na = 0
    ni = 0
    e = 4
    i = 8
    o = 14
    t = 19
    g = False

    pt1Str.set('')
    n1Str.set('')

    pt2Str.set('')
    n2Str.set('')

    pt3Str.set('')
    n3Str.set('')

    pt4Str.set('')
    n4Str.set('')

    pt5Str.set('')
    n5Str.set('')

    pt6Str.set('')
    n6Str.set('')

    pt7Str.set('')
    n7Str.set('')

    pt8Str.set('')
    n8Str.set('')

    pt9Str.set('')
    n9Str.set('')

    pt0Str.set('')
    n0Str.set('')

    m = mText.get(1.0, 'end')
    m = trim(m)

    l = m.split()

    for c in l:
        if len(c) == 1:
            b = ord(c)

            if b in range(65, 91):
                b -= 65
                na = b
                ni = b - i
                g = True
                break

            elif b in range(97, 123):
                b -= 97
                na = b
                ni = b - i
                g = True
                break

    if g and m != '':
        s = decrypt(m, na)
        pt1Str.set(s)
        n1Str.set(na)

        s = decrypt(m, ni)
        pt2Str.set(s)
        n2Str.set(ni)

    elif not g and m != '':
        d = [0] * 26
        l = m.lower()

        for c in l:
            b = ord(c)
            if b in range(97, 123):
                d[b - 97] += 1

        b = max(d)
        x = d.index(b)
        d.remove(b)

        b = max(d)
        y = d.index(b)
        l = []

        na0 = x
        ne0 = x - e
        ni0 = x - i
        no0 = x - o
        nt0 = x - t

        na1 = y
        ne1 = y - e
        ni1 = y - i
        no1 = y - o
        nt1 = y - t

        s = decrypt(m, na0)
        pt1Str.set(s)
        n1Str.set(na0)
        l.append(na0)

        if ne0 not in l:
            s = decrypt(m, ne0)
            pt2Str.set(s)
            n2Str.set(ne0)
            l.append(ne0)

        if ni0 not in l:
            s = decrypt(m, ni0)
            pt3Str.set(s)
            n3Str.set(ni0)
            l.append(ni0)

        if no0 not in l:
            s = decrypt(m, no0)
            pt4Str.set(s)
            n4Str.set(no0)
            l.append(no0)

        if nt0 not in l:
            s = decrypt(m, nt0)
            pt5Str.set(s)
            n5Str.set(nt0)
            l.append(nt0)

        if na1 not in l:
            s = decrypt(m, na1)
            pt6Str.set(s)
            n6Str.set(na1)
            l.append(na1)

        if ne1 not in l:
            s = decrypt(m, ne1)
            pt7Str.set(s)
            n7Str.set(ne1)
            l.append(ne1)

        if ni1 not in l:
            s = decrypt(m, ni1)
            pt8Str.set(s)
            n8Str.set(ni1)
            l.append(ni1)

        if no1 not in l:
            s = decrypt(m, no1)
            pt9Str.set(s)
            n9Str.set(no1)
            l.append(no1)

        if nt1 not in l:
            s = decrypt(m, nt1)
            pt0Str.set(s)
            n0Str.set(nt1)
            l.append(nt1)


if __name__ == '__main__':
    root = Tk()
    root.title("An's shift cipher cryptanalysis v1.0")
    img = PhotoImage(file=path + 'icon.gif')
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.resizable(False, False)

    style = Style()
    themes = style.theme_names()

    if 'xpnative' in themes:
        style.theme_use('xpnative')
    elif 'aqua' in themes:
        style.theme_use('aqua')
    elif 'alt' in themes:
        style.theme_use('alt')
    else:
        style.theme_use('default')

    mf = Frame(root, padding=10)
    mf.grid(column=0, row=0, sticky='wnes')

    inLf = Labelframe(mf, text='Nhập bản mã Shift')
    inLf.grid(column=0, row=0, ipady=10, padx=5)

    inLbl = Label(inLf, text='Bản mã:')
    inLbl.grid(column=0, row=0)

    mText = Text(inLf, width=40, height=9)
    mText.grid(column=0, row=1, padx=10, pady=10)

    cryptBtn = Button(inLf, text='Thám mã', command=cryptanalysis)
    cryptBtn.grid(column=0, row=2)

    outLf = Labelframe(mf, text='10 kết quả khả nghi')
    outLf.grid(column=1, row=0, ipady=10, ipadx=10, padx=5, sticky='n')

    ptLbl = Label(outLf, text='Bản rõ:')
    ptLbl.grid(column=0, row=0)

    nLbl = Label(outLf, text='n')
    nLbl.grid(column=1, row=0)

    pt1Str = StringVar()
    pt1Lbl = Label(outLf, textvariable=pt1Str)
    pt1Lbl.grid(row=1, column=0)

    n1Str = StringVar()
    n1Lbl = Label(outLf, textvariable=n1Str)
    n1Lbl.grid(row=1, column=1)

    pt2Str = StringVar()
    pt2Lbl = Label(outLf, textvariable=pt2Str)
    pt2Lbl.grid(row=2, column=0)

    n2Str = StringVar()
    n2Lbl = Label(outLf, textvariable=n2Str)
    n2Lbl.grid(row=2, column=1)

    pt3Str = StringVar()
    pt3Lbl = Label(outLf, textvariable=pt3Str)
    pt3Lbl.grid(row=3, column=0)

    n3Str = StringVar()
    n3Lbl = Label(outLf, textvariable=n3Str)
    n3Lbl.grid(row=3, column=1)

    pt4Str = StringVar()
    pt4Lbl = Label(outLf, textvariable=pt4Str)
    pt4Lbl.grid(row=4, column=0)

    n4Str = StringVar()
    n4Lbl = Label(outLf, textvariable=n4Str)
    n4Lbl.grid(row=4, column=1)

    pt5Str = StringVar()
    pt5Lbl = Label(outLf, textvariable=pt5Str)
    pt5Lbl.grid(row=5, column=0)

    n5Str = StringVar()
    n5Lbl = Label(outLf, textvariable=n5Str)
    n5Lbl.grid(row=5, column=1)

    pt6Str = StringVar()
    pt6Lbl = Label(outLf, textvariable=pt6Str)
    pt6Lbl.grid(row=6, column=0)

    n6Str = StringVar()
    n6Lbl = Label(outLf, textvariable=n6Str)
    n6Lbl.grid(row=6, column=1)

    pt7Str = StringVar()
    pt7Lbl = Label(outLf, textvariable=pt7Str)
    pt7Lbl.grid(row=7, column=0)

    n7Str = StringVar()
    n7Lbl = Label(outLf, textvariable=n7Str)
    n7Lbl.grid(row=7, column=1)

    pt8Str = StringVar()
    pt8Lbl = Label(outLf, textvariable=pt8Str)
    pt8Lbl.grid(row=8, column=0)

    n8Str = StringVar()
    n8Lbl = Label(outLf, textvariable=n8Str)
    n8Lbl.grid(row=8, column=1)

    pt9Str = StringVar()
    pt9Lbl = Label(outLf, textvariable=pt9Str)
    pt9Lbl.grid(row=9, column=0)

    n9Str = StringVar()
    n9Lbl = Label(outLf, textvariable=n9Str)
    n9Lbl.grid(row=9, column=1)

    pt0Str = StringVar()
    pt0Lbl = Label(outLf, textvariable=pt0Str)
    pt0Lbl.grid(row=10, column=0)

    n0Str = StringVar()
    n0Lbl = Label(outLf, textvariable=n0Str)
    n0Lbl.grid(row=10, column=1)

    mText.focus()
    root.mainloop()
