import argparse
from .extract import extract_text_from_pdf

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("-path", required=True, help="Path to the PDF file")
    parser.add_argument("-output", help="Path to the output file or directory (optional)")
    args = parser.parse_args()

    extract_text_from_pdf(args.path, args.output)

if __name__ == "__main__":
    main()
