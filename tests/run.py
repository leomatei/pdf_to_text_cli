import unittest
import os
import sys

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the function
from pdf_to_text.extract import extract_text_from_pdf

class TestPDFExtraction(unittest.TestCase):
    
    def setUp(self):
        """Set up a dummy PDF file for testing."""
        self.test_pdf = "test.pdf"
        with open(self.test_pdf, "wb") as f:
            f.write(b"%PDF-1.4\n%Fake PDF Content")

    def tearDown(self):
        """Remove test files after tests run."""
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)

    def test_strip_whitespace(self):
        """Test that whitespace around paths is removed."""
        clean_path = extract_text_from_pdf(f"  {self.test_pdf}  ")
        self.assertTrue(os.path.exists(clean_path))

    def test_non_existing_output_filename(self):
        """Test saving to a user-defined non-existing output filename."""
        output_file = "outputs/test_output.txt"
        if os.path.exists(output_file):
            os.remove(output_file)  # Ensure clean test
        result_path = extract_text_from_pdf(self.test_pdf, output_file)
        self.assertEqual(result_path, output_file)
        self.assertTrue(os.path.exists(output_file))

    def test_output_directory(self):
        """Test saving inside a user-defined directory."""
        output_dir = "custom_output"
        os.makedirs(output_dir, exist_ok=True)
        result_path = extract_text_from_pdf(self.test_pdf, output_dir)
        self.assertTrue(result_path.startswith(output_dir))

    def test_file_not_found(self):
        """Test handling of non-existent PDF paths."""
        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf("non_existent.pdf")

if __name__ == "__main__":
    unittest.main()
