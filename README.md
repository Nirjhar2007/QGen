@Author: Nirjhar Chatterjee [nirjhar.chatterjee@gmail.com]
PDF Processing with Gemini AI

This program extracts text from PDF files stored in a database, uses the Gemini AI API to generate content (e.g., MCQ papers), and displays the results.

Features
--------
- Retrieve PDF file paths from a MySQL database.
- Extract text from the PDFs using the `PyPDF2` library.
- Interact with the Gemini AI API to process the PDF content.
- Secure configuration for API keys and database access.

Prerequisites
-------------
Before using the program, ensure you have the following installed:
- Python 3.8 or later
- MySQL server
- Required Python packages (`PyPDF2`, `google-generativeai`, `mysql-connector-python`)

Installation
------------

1. Clone the repository or copy the code files into a directory on your system.

2. Install Required Packages:
   Run the following command to install the required dependencies:
   ```bash
   python install_dependencies.py
   ```

3. Set Up MySQL Database:
   Create a MySQL database named `practice` and set up the `pdfstorage` table using the following script:
   ```sql
   CREATE DATABASE practice;

   USE practice;

   CREATE TABLE pdfstorage (
       Subject VARCHAR(10) NULL,
       Chapter VARCHAR(20) NULL,
       pdf_loc VARCHAR(50) NULL,
       pdfnumber VARCHAR(5) NULL
   );
   ```

4. Populate the `pdfstorage` Table:
   Insert sample data into the `pdfstorage` table:
   ```sql
   INSERT INTO pdfstorage (Subject, Chapter, pdf_loc, pdfnumber)
   VALUES
       ('Math', 'Algebra', '/path/to/algebra.pdf', '001'),
       ('Science', 'Biology', '/path/to/biology.pdf', '002');
   ```

5. Configure API Key:
   Set up your Gemini AI API key:
   - Run the `build_script.py` and select the "Configure API key" option, or manually create a `.env` file in the project directory and add:
     GENAI_API_KEY=your_api_key_here

Usage
-----

1. Run the Program:
   Execute the main program:
   ```bash
   python main_program.py
   ```

2. Enter PDF Code:
   When prompted, enter the `pdfnumber` associated with the PDF file you want to process.

3. Generated Output:
   - The program will extract text from the specified PDF and send it to the Gemini AI API.
   - The output (e.g., MCQs or a summary) will be displayed in the terminal.

Example Workflow
----------------

1. Start the program:
   ```bash
   python main_program.py
   ```

2. Enter the code of the subject when prompted:
   Enter code of subject: 001

3. The program retrieves the PDF location from the database, extracts the text, and sends it to the Gemini AI API. The results are displayed in the terminal.

File Descriptions
-----------------

- `main_program.py`:
  The main application logic that integrates PDF text extraction, database interaction, and Gemini AI API calls.

- `install_dependencies.py`:
  A script to install all required Python packages.

- `build_script.py`:
  An interactive build script to set up the environment, configure the database, and save the Gemini API key.

- `.env`:
  A file used to securely store the Gemini API key.

Troubleshooting
---------------

- Database Connection Issues:
  - Ensure the MySQL server is running and the credentials in the program are correct.

- API Key Error:
  - Ensure you’ve correctly configured the Gemini API key in the `.env` file or via the build script.

- PDF Path Issues:
  - Verify that the file paths in the `pdfstorage` table are correct and accessible by the program.

- Missing Dependencies:
  - Run `python install_dependencies.py` to ensure all required packages are installed.

License
-------

This project is open-source and free to use.
