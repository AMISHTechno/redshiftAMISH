import re
import os
import pandas as pd
from typing import List, Tuple
import h5py
import json
from datetime import datetime
from collections import Counter


def extract_timestamps(logs: List[str]) -> List[datetime]:
    """
    Extracts and converts timestamps from log entries to datetime objects.
    """
    timestamps = []
    for log in logs:
        match = re.search(r"\b[A-Za-z]{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\b", log)
        if match:
            timestamp = datetime.strptime(match.group(), "%b %d %H:%M:%S")
            timestamps.append(timestamp)
    return timestamps


def extract_log_levels(logs: List[str]) -> List[str]:
    """
    Extracts log levels from log entries.
    """
    log_levels = []
    for log in logs:
        match = re.search(r"\b(INFO|ERROR|WARN|DEBUG)\b", log)
        log_levels.append(match.group() if match else "UNKNOWN")
    return log_levels


def tokenize_logs(logs: List[str]) -> List[List[str]]:
    """
    Tokenizes log messages into words.
    """
    return [re.findall(r"\b\w+\b", log) for log in logs]


def count_unique_words(tokenized_logs: List[List[str]]) -> Counter:
    """
    Counts unique words in the tokenized log messages.
    """
    word_counts = Counter()
    for tokens in tokenized_logs:
        word_counts.update(tokens)
    return word_counts


def filter_by_keyword(logs: List[str], keyword: str) -> List[str]:
    """
    Filters log entries containing a specific keyword.
    """
    return [log for log in logs if keyword in log]


""" Final Processing
    1. Tokenize and Extract Key Information: Extract timestamps, log levels, and potentially service names.
    2. Identify and Tag Key Entities: Focus on service names or actions as key entities for NER.
    3. Prepare Data for Analysis: Format the extracted information for easy analysis and model training.
    4. Save in DataFrame and CSV: Store the structured data in both formats.
"""


def extract_key_entities_from_hdf5(
    file_path: str,
) -> List[Tuple[str, str, str, str]]:
    """
    Extracts key entities such as timestamp, log level, service name, and action from an HDF5 log file.

    Args:
        file_path (str): Path to the HDF5 log file.

    Returns:
        List[Tuple[str, str, str, str]]: A list of tuples containing the timestamp, log level, service name, and action.
    """
    key_entities = []

    with h5py.File(file_path, "r") as file:
        # Assuming log data is stored in a dataset named 'log_data'
        # Adjust the dataset name as per your HDF5 file structure
        log_data = file["log_data"][:]

    for log_entry in log_data:
        # Assuming log_entry is a byte string, decode it if necessary
        log_entry = (
            log_entry.decode("utf-8")
            if isinstance(log_entry, bytes)
            else log_entry
        )
        timestamp, log_level, service, action = extract_key_entities(log_entry)
        key_entities.append((timestamp, log_level, service, action))

    return key_entities


def prepare_log_data_for_analysis(logs: List[str]) -> pd.DataFrame:
    """
    Prepares log data for post-analysis by extracting key information and structuring it in a DataFrame.
    """
    # Extracting key information
    timestamps = extract_timestamps(logs)
    log_levels = extract_log_levels(logs)
    tokenized_logs = tokenize_logs(logs)

    # Identifying key entities (e.g., service names, actions)
    service_names, actions = zip(
        *[extract_key_entities(tokens) for tokens in tokenized_logs]
    )

    # Preparing data for analysis
    analysis_data = {
        "Timestamp": timestamps,
        "LogLevel": log_levels,
        "ServiceName": service_names,
        "Action": actions,
    }
    df = pd.DataFrame(analysis_data)

    return df


def extract_key_entities_from_directory(
    directory: str,
) -> List[Tuple[str, str]]:
    """
    Extracts key entities such as service names and actions from all log files in the specified directory.

    Args:
        directory (str): Path to the directory containing log files.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing extracted service names and actions.
    """
    key_entities = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.endswith(
            ".log"
        ):  # Process only log files
            with open(file_path, "r") as file:
                logs = file.readlines()
                for log in logs:
                    tokens = re.findall(
                        r"\b\w+\b", log
                    )  # Tokenize each log entry
                    service_name, action = extract_key_entities(tokens)
                    key_entities.append((service_name, action))

    return key_entities


# Placeholder function to extract key entities like service names and actions


def extract_key_entities_from_serialized_file(
    file_path: str,
) -> List[Tuple[str, str, str, str]]:
    """
    Extracts key entities such as timestamp, log level, service name, and action from a serialized log file.

    Args:
        file_path (str): Path to the serialized log file.

    Returns:
        List[Tuple[str, str, str, str]]: A list of tuples containing the timestamp, log level, service name, and action.
    """
    key_entities = []

    with open(file_path, "r") as file:
        logs = json.load(file)  # Assuming the file is in JSON format

    for log_entry in logs:
        timestamp, log_level, service, action = extract_key_entities(log_entry)
        key_entities.append((timestamp, log_level, service, action))

    return key_entities


def extract_key_entities(log: str) -> Tuple[str, str, str, str]:
    """
    Extracts key entities such as timestamp, log level, service name, and action from a log entry.
    """
    # ... existing code ...


# Example usage
serialized_file_path = "path/to/your/serialized_log_file.json"
entities = extract_key_entities_from_serialized_file(serialized_file_path)
