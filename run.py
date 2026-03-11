from data import Run, all_runs

def read_file(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        return f.read()

def create_temp_dir() -> str:
    import tempfile
    temp_dir = tempfile.mkdtemp()
    return temp_dir


def create_scribus_file(content: str, path: str, encoding: str = "utf-8") -> None:
    with open(path, "w", encoding=encoding) as f:
        f.write(content)

def add_background(temp_dir: str) -> None:
    import os
    import shutil
    shutil.copy("background.png", os.path.join(temp_dir, "background.png"))

def create_pdf(temp_dir: str, template: str, id : str, run_name:str, number:int) -> str:
    import scribus
    import os
    content = (
        template
        .replace("RUN_PLACEHOLDER", run_name)
        .replace("NUMBER_PLACEHOLDER", str(number))
    )
    temp_file_name = os.path.join(temp_dir, f"{id}_{number}")
    create_scribus_file(content, f"{temp_file_name}.sla")
    scribus.openDoc(f"{temp_file_name}.sla")
    scribus.redrawAll()
    pdf = scribus.PDFfile()
    pdf.file = f"{temp_file_name}.pdf"
    pdf.save()
    return pdf.file

def join_all_pdfs(temp_dir: str) -> None:
    return

def merge_pdfs(pdf_files: list[str], output_file: str) -> None:
    from PyPDF2 import PdfMerger
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()

def main() -> None:
    import shutil
    template = read_file("template.sla")
    temp_dir = create_temp_dir() 
    add_background(temp_dir)

    pdfs = []
    for run in all_runs:
        for number in run.number_range:
            pdf_file = create_pdf(temp_dir, template, run.id, run.name, number)
            pdfs.append(pdf_file)

    merge_pdfs(pdfs, "output.pdf")
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()