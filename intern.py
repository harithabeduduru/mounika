import requests

# Specify the URL of the PDF file in the repository
pdf_url = "https://drive.google.com/file/d/1CLl2OruM9oPscyjaBhXiUD-dfdDNYDII/view?usp=sharing"

# Send a GET request to download the PDF file
response = requests.get(pdf_url)

# Check if the request was successful
if response.status_code == 200:
    # Access the PDF content
    pdf_content = response.content
    # Your code to work with the PDF content goes here
    # For example, you can save it to a local file or process it further
else:
    print("Failed to retrieve the PDF file.")
