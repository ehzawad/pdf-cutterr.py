from PyPDF2 import PdfReader, PdfWriter

def extract_page_range(pdf_path, start_printed_page, end_printed_page, output_pdf_name, page_offset=21):
    """
    Extracts a range of pages from a PDF, considering an offset between the printed page numbers and actual PDF page numbers.
    """
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    total_pages = len(reader.pages)

    actual_start_page = start_printed_page + page_offset
    actual_end_page = end_printed_page + page_offset

    if actual_start_page < 1 or actual_end_page > total_pages:
        print(f"Requested range is out of bounds. The PDF has {total_pages - page_offset} printable pages.")
        return

    for i in range(actual_start_page - 1, actual_end_page):
        writer.add_page(reader.pages[i])

    output_pdf_path = f"{output_pdf_name}.pdf"
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Extracted pages {start_printed_page} to {end_printed_page} into {output_pdf_path}")

def extract_specific_pages(pdf_path, printed_pages, output_pdf_name, page_offset=21):
    """
    Extracts specific pages based on a list of printed page numbers, considering an offset.
    """
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    total_pages = len(reader.pages)

    for printed_page in printed_pages:
        actual_page = printed_page + page_offset
        if actual_page < 1 or actual_page > total_pages:
            print(f"Page {printed_page} is out of bounds and will be skipped.")
            continue
        writer.add_page(reader.pages[actual_page - 1])

    output_pdf_path = f"{output_pdf_name}.pdf"
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Extracted pages {printed_pages} into {output_pdf_path}")

def extract_each_page_as_pdf(pdf_path, printed_pages, output_pdf_name_prefix, page_offset=21):
    """
    Extracts each specified printed page number into a separate PDF file, considering an offset.
    """
    reader = PdfReader(pdf_path)
    output_paths = []

    for printed_page in printed_pages:
        writer = PdfWriter()
        actual_page = printed_page + page_offset

        if actual_page < 1 or actual_page > len(reader.pages):
            print(f"Page {printed_page} is out of bounds and will be skipped.")
            continue

        writer.add_page(reader.pages[actual_page - 1])
        output_pdf_path = f"{output_pdf_name_prefix}_Page_{printed_page}.pdf"
        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)

        output_paths.append(output_pdf_path)
        print(f"Extracted page {printed_page} into {output_pdf_path}")

    return output_paths

# Example usage:
pdf_path = "path_to_your_pdf_file.pdf"  # Update this to the path of your PDF
extract_page_range(pdf_path, 146, 227, "Example_Range")  # Example for extracting a range
extract_specific_pages(pdf_path, [1141, 1222], "Merged_Specific_Pages")  # Example for extracting specific pages into a merged PDF
extract_each_page_as_pdf(pdf_path, [1141, 1222], "Individual_Page")  # Example for extracting specific pages as individual PDFs
