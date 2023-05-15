#  open file MIXIN:
from io import BytesIO

class FileMixin:
    # def get_content(self):
    #     with open(self.data, 'rb') as f:
    #         return f.read()

    def get_content(self):
        # Return the bytes of the PDF file
        with open(self.data, 'rb') as f:
            return BytesIO(f.read()).getvalue()