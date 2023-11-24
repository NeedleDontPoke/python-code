import tkinter.ttk
import _thread
import time
import PIL
import PIL.Image
import PIL.ImageGrab
import PIL.ImageTk

img = None
TkImg = None
st = time.perf_counter()
main = tkinter.Tk()
main.title('Your Screen')
F = tkinter.ttk.Frame(main, width=1920, height=1080)
L = tkinter.ttk.Label(F)
L.place(x=0, y=0)
F.place(x=0, y=0)


def refresh_img():
    global img, TkImg, main, L, st
    img = PIL.ImageGrab.grab()
    TkImg = PIL.ImageTk.PhotoImage(img)
    L.config(image=TkImg)
    main.title('Your Screen - Refresh Rate : ' + str((1 / (time.perf_counter() - st)).__round__(1)) + 'fps')
    st = time.perf_counter()
    main.after(1, lambda: _thread.start_new_thread(refresh_img, ()))


main.after(1, lambda: _thread.start_new_thread(refresh_img, ()))
main.mainloop()
