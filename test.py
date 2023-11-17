from weasyprint import HTML

# Path to the HTML file
html_file_path = 'multi_page_invoice.html'

# Path for the output PDF file
pdf_file_path = 'multi_page_invoice.pdf'

# Convert HTML to PDF
HTML(html_file_path).write_pdf(pdf_file_path)

print("PDF generated successfully!")
