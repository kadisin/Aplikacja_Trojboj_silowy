from StartWindow import StartWindow
import tkinter as tk

def main():
    root = tk.Tk()
    st = StartWindow(master=root)
    st.mainloop()


if __name__ == "__main__":
    main()