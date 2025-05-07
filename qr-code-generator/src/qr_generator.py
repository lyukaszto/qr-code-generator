class QRCodeGenerator:
    def __init__(self):
        import qrcode
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def generate_qr_code(self, data):
        self.qr.add_data(data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        return img

    def save_qr_code(self, file_path):
        img = self.qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)