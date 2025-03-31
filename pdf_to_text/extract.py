import os
import PyPDF2
from datetime import datetime

def extract_text_from_pdf(pdf_path, output_path=None):
    """Extract text from a PDF file and save it to a specified .txt file."""
    
    pdf_path = pdf_path.strip().strip('\"')

    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"Error: File '{pdf_path}' not found.")

    pdf_filename = os.path.basename(pdf_path)
    base_name = os.path.splitext(pdf_filename)[0]  

    if not output_path:
        output_dir = "outputs"
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = os.path.join(output_dir, f"{base_name}_{timestamp}.txt")

    else:
        output_path = output_path.strip().strip('\"')

        if os.path.isdir(output_path):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_path = os.path.join(output_path, f"{base_name}_{timestamp}.txt")

        elif not os.path.exists(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

        else:
            raise FileExistsError(f"Error: Output file '{output_path}' already exists.")

    extracted_text = ''
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text += page.extract_text() or ''  
    except Exception as e:
        raise RuntimeError(f"Error processing PDF: {e}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    print(f"✅ Extracted text saved to: {output_path}")
    return output_path
