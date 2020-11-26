from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# creating model for this application

class QrDetails(models.Model):
    text = models.CharField(max_length=255)
    qr_image = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.text)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(self.text)
        qr.make(fit=True)
        qr_image = qr.make_image(fill="black", back_color="white")
        canvas = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        file_name = f'qr_code-{self.text}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_image.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(args, kwargs)
