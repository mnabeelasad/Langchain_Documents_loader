# LangChain Document Loader Project

This project demonstrates various document loaders using the LangChain framework. It provides functionality to load and process different types of documents such as text files, CSV files, and PDF files, and offers a flexible way to work with them.

## Project Structure

- **`cricket.txt`**: A sample text file used in the project to demonstrate text loading functionality.
- **`csv_sample.csv`**: A sample CSV file for demonstrating CSV loading functionality.
- **`text_file_loader.py`**: Python script that demonstrates loading text files using LangChain's document loader.
- **`csv_loader.py`**: Python script that demonstrates loading CSV files using LangChain's document loader.
- **`pdf_file_loader.py`**: Python script that demonstrates loading PDF files using LangChain's document loader.
- **`lazy_load.py`**: Script for loading multiple files faster using lazy loading techniques in LangChain.
- **`directort_loader.py`**: Script to load data from directories for use in RAG (Retrieve and Generate) applications.
- **`Webbase_loader.py`**: Python script to load data from web browsers.
- **`books/`**: Directory containing documents or books for further processing.

## Dependencies

This project relies on various external libraries such as LangChain, PyPDF, DirectoryLoader, WebBasedLaoder and CSV etc. Below is the list of dependencies needed to run the project.

## Installation

To get started, clone this repository and install the dependencies listed in `requirements.txt`.

```bash
git clone https://github.com/yourusername/langchain-document-loader.git
cd langchain-document-loader
pip install -r requirements.txt
