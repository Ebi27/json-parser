# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /cc_json

# Copy the script from the host into the container
COPY json_parser.py /cc_json/json_parser.py

# Copy additional files
COPY tests /cc_json/tests
COPY test_py /cc_json/test_py

# Install required Python packages
RUN pip install pytest
RUN pip install --no-cache-dir pytest python-dotenv

# Set the default command for the container
CMD ["python", "cc_json/json_parser.py"]
