from tkinter import filedialog

#ファイルダイアログを表示して選択ファイルのパスを取得
def file_select():
    filename = filedialog.askopenfilename(
        title = "画像ファイルを開く",
        filetypes = [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], # ファイルフィルタ
        initialdir = "./"
    )
    print(filename)
    return filename


if __name__ == '__main__':
    file_select()

