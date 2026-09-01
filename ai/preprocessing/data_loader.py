import pandas as pd
from pypdf import PdfReader


def load_csv(file_path):
    return pd.read_csv(file_path)


def load_excel(file_path):
    return pd.read_excel(file_path)


def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_file(file_path, file_type):

    if file_type == "csv":
        return load_csv(file_path)

    elif file_type in ["xlsx", "xls"]:
        return load_excel(file_path)

    elif file_type == "pdf":
        return load_pdf(file_path)

    else:
        raise ValueError("Unsupported file type")