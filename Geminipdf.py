import PyPDF2  # Library to extract text from PDF
import google.generativeai as genai
import mysql.connector as con

mycon = con.connect(host="localhost", user="root", passwd="root", database="practice")
cursor = mycon.cursor()
cursor.execute("Select * from pdfstorage")
data = cursor.fetchall()
for i in data:
    print(i)
code = input("Enter code of subject:")
st = "select pdf_loc from pdfstorage where pdfnumber=" + code
print(st)
cursor.execute(st)
data = cursor.fetchall()
for i in data:
    print(i[0])
if len(data) != 0:
    # Configure the API key for Gemini API access
    genai.configure(api_key="XXXXXXXXXX")


    # Function to extract text from the PDF file locally
    def extract_text_from_pdf(pdf_path):
        """Extracts text from the given PDF file."""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
        return text


    # Create the generative model configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Initialize the generative model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )

    # Replace with your local PDF file path
    pdf_path = i[0]

    # Extract text from the PDF file locally
    pdf_text = extract_text_from_pdf(pdf_path)

    # Start a chat session
    chat_session = model.start_chat(history=[])

    # Ask Gemini to summarize the extracted text
    response = chat_session.send_message(f"generate a mcq paper from this pdf {pdf_text}")

    # Print the response
    print("Summary of PDF:", response.text)
else:
    print("Error input")
