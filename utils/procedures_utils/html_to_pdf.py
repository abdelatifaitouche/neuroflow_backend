

from weasyprint import HTML

def export_html_to_pdf(html_content):
    pdf = HTML(string = html_content).write_pdf()
    return pdf

    