import PIL
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Cria uma instância da janela Tkinter
root = Tk()
root.withdraw()  # Esconde a janela principal

# Permite que o usuário selecione um arquivo de imagem
filename = askopenfilename()

# Verifica se o usuário selecionou um arquivo
if filename:
    # Abre a imagem selecionada
    img = Image.open(filename)

    # Compacta e salva a imagem
    img.save("resultado.jpg", "JPEG", optimize=True, quality=10)
    print("Imagem compactada com sucesso!")
else:
    print("Nenhum arquivo selecionado.")
