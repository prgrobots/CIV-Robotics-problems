# test_extensions.py
import unittest
from extensions import determine_media_type

class TestExtensionsProgram(unittest.TestCase):

    def test_gif_extension(self):
        result = determine_media_type("example.gif")
        self.assertEqual(result, "image/gif")

    def test_jpg_extension(self):
        result = determine_media_type("picture.jpg")
        self.assertEqual(result, "image/jpeg")

    def test_jpeg_extension(self):
        result = determine_media_type("photo.jpeg")
        self.assertEqual(result, "image/jpeg")

    def test_png_extension(self):
        result = determine_media_type("image.png")
        self.assertEqual(result, "image/png")

    def test_pdf_extension(self):
        result = determine_media_type("document.pdf")
        self.assertEqual(result, "application/pdf")

    def test_txt_extension(self):
        result = determine_media_type("text_file.txt")
        self.assertEqual(result, "text/plain")

    def test_zip_extension(self):
        result = determine_media_type("archive.zip")
        self.assertEqual(result, "application/zip")

    def test_unknown_extension(self):
        result = determine_media_type("unknown.file")
        self.assertEqual(result, "application/octet-stream")

    def test_no_extension(self):
        result = determine_media_type("filename")
        self.assertEqual(result, "application/octet-stream")

if __name__ == '__main__':
    unittest.main()
