from tkinter import Tk, Label, Entry, Button, Text, END
from scraper import run_scraper

def start_scraper():
    minero = entry_minero.get()
    links_text = text_links.get("1.0", END)
    links = [link.strip() for link in links_text.split('\n') if link.strip()]
    if minero and links:
        run_scraper(minero, links)
    else:
        print("Por favor, ingrese el nombre del minero y al menos una URL.")

# Interfaz gráfica
root = Tk()
root.title("Scraper de Comentarios")

Label(root, text="Nombre del Minero:").grid(row=0, column=0, padx=10, pady=10)
entry_minero = Entry(root)
entry_minero.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="URLs (una por línea):").grid(row=1, column=0, padx=10, pady=10)
text_links = Text(root, height=10, width=50)
text_links.grid(row=1, column=1, padx=10, pady=10)

Button(root, text="Iniciar Scraping", command=start_scraper).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
