# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /cc-json

# Copy the scripts from the host into the container at /ccwc
COPY cc-json/lexer.py cc-json/lexer.py
COPY cc-json/lexer_token.py cc-json/lexer_tokens.py
COPY cc-json/parser.py cc-json/parser.py
COPY cc-json/json_parser cc-json/json_parser.py

# Copy additional files
COPY tests /tests
COPY tests /test-py

# Install required Python packages
RUN pip install pytest

# Set the default command for the container
CMD ["python", "json_parser/json_parser.py"]
