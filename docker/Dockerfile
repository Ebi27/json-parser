# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /cc_json

# Copy the scripts from the host into the container at /ccwc
COPY cc_json/lexer.py cc_json/lexer.py
COPY cc_json/lexer_token.py cc_json/lexer_tokens.py
COPY cc_json/parser.py cc_json/parser.py
COPY cc_json/json_parser cc_json/json_parser.py

# Copy additional files
COPY tests /tests
COPY tests /test_py

# Install required Python packages
RUN pip install pytest

# Set the default command for the container
CMD ["python", "json_parser/json_parser.py"]
