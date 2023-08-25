"""
Batch Process C: Third transformation

Read from a file, transform, write to a new file.
In this case, covert degree K to degree F.

Note: 
This is a batch process, but the file objects we use are 
often called 'file-like objects' or 'streams'.
Streaming differs in that the input data is unbounded.

Use logging, very helpful when working with batch and streaming processes. 

"""

# Import from Python Standard Library

import csv
import logging

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Declare program constants

INPUT_FILE_NAME = "batchfile_2_kelvin.csv"
OUTPUT_FILE_NAME = "batchfile_3_farenheit.csv"

# Define program functions (bits of reusable code)
# Use docstrings - and indentation matters!


def convert_k_to_f(temp_k):
    return (temp_k - 273.15) * 9/5 + 32  # Conversion formula

def process_rows(input_file_name, output_file_name):
    with open(input_file_name, mode="r") as input_file, open(output_file_name, mode="w", newline="") as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        header = next(csv_reader)
        header.append("Fahrenheit")  # Add a new header column
        csv_writer.writerow(header)

        for row in csv_reader:
            temp_k = float(row[0])
            temp_f = convert_k_to_f(temp_k)
            row.append(temp_f)
            csv_writer.writerow(row)


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process C.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
