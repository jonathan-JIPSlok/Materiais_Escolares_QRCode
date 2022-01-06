import qrcode

def QR(Data):
    """Cria a imagen com os dados"""
    img = qrcode.make(Data)
    return img
    
def Salvar(img, Local):
    """salva a imagem"""
    img = img.save(Local)
    return type(img)