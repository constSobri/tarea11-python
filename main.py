import tkinter
import tkinter as tk
from tkinter import ttk


def main():
    def reinicio():
        print('Se ha reiniciado')
        salsaFavorita.set('')

    def finalizado():
        print(f'Su salsa favorita es {salsaFavorita.get()}')
        window.quit()

    window = tkinter.Tk()
    window.columnconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    label = tkinter.Label(window, text="Elige tu salsa favorita:")
    label.grid(row=1, pady=5, padx=5)

    salsaFavorita = tk.StringVar()
    r1 = ttk.Radiobutton(window, text='Ketchup', value='Ketchup', variable=salsaFavorita)
    r2 = ttk.Radiobutton(window, text='Mayonesa', value='Mayonesa', variable=salsaFavorita)
    r3 = ttk.Radiobutton(window, text='Mostaza', value='Mostaza', variable=salsaFavorita)

    r1.grid(column=0, row=2, pady=10, padx=10)
    r2.grid(column=0, row=3, pady=10, padx=10)
    r3.grid(column=0, row=4, pady=10, padx=10)

    botonFinalizado = ttk.Button(window, text="Listo", command=finalizado)
    botonFinalizado.grid(column=0, row=6, padx=10, pady=10)

    botonReset = ttk.Button(window, text="Reiniciar", command=reinicio)
    botonReset.grid(column=0, row=5, padx=10, pady=10)

    window.mainloop()


if __name__ == '__main__':
    main()
