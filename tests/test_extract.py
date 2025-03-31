import unittest
import os
import sys
from PyPDF2 import PdfWriter

# Add parent directory to sys.path so we can import extractPDFtoTXT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the function from extractPDFtoTXT.py
from pdf_to_text.extract import extract_text_from_pdf

class TestPDFExtraction(unittest.TestCase):
    
    def setUp(self):
        """Create a valid dummy PDF file for testing."""
        self.test_pdf = "test.pdf"
        
        writer = PdfWriter()  # Create an empty but valid PDF
        with open(self.test_pdf, "wb") as f:
            writer.write(f)  # Save the empty PDF

    def tearDown(self):
        """Cleanup test files after each test."""
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)

    def test_strip_whitespace(self):
        """Ensure leading/trailing spaces in input paths do not cause issues."""
        clean_path = extract_text_from_pdf(f"  {self.test_pdf}  ")
        self.assertTrue(os.path.exists(clean_path))
        os.remove(clean_path)  # Cleanup output file

    def test_non_existing_output_filename(self):
        """Ensure text is saved in a user-defined, non-existing file."""
        output_file = "outputs/test_output.txt"
        if os.path.exists(output_file):
            os.remove(output_file)  # Clean up previous test runs

        result_path = extract_text_from_pdf(self.test_pdf, output_file)
        self.assertEqual(result_path, output_file)
        self.assertTrue(os.path.exists(output_file))

        os.remove(output_file)  # Cleanup

    def test_output_directory(self):
        """Ensure text is saved inside a user-defined directory."""
        output_dir = "custom_output"
        os.makedirs(output_dir, exist_ok=True)
        result_path = extract_text_from_pdf(self.test_pdf, output_dir)
        self.assertTrue(result_path.startswith(output_dir))
        
        # Cleanup
        os.remove(result_path)
        os.rmdir(output_dir)

    def test_file_not_found(self):
        """Ensure proper handling of non-existent PDFs."""
        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf("non_existent.pdf")

if __name__ == "__main__":
    unittest.main()
