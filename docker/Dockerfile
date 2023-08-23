# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /json-parser

# Copy the script from the host into the container
COPY cc_json/json_parser.py /json-parser/cc_json/json_parser.py
COPY cc_json/lexer.py /cc_json/lexer.py
COPY cc_json/parser.py /cc_json/parser.py
COPY cc_json/lexer_tokens.py /cc_json/lexer_tokens.py

# Copy additional files
COPY tests /tests
COPY test_py /test_py

# Install required Python packages
RUN pip install pytest
RUN pip install --no-cache-dir pytest python-dotenv

# Set the default command for the container
CMD ["python", "cc_json/json_parser.py"]
