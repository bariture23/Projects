

import re

def get_user_input():
    return input("Enter input string: ")

def print_input(input_str):
    print(input_str)

def clean_input(input_str):
    cleaned_str = re.sub(r'[?.!,"\(\)]', '', input_str)
    cleaned_str = re.sub(r' {2,}', ' ', cleaned_str)
    return cleaned_str.strip().lower()

def word_freq(input_str):
    words = input_str.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

def sort_by_value(freq_dict):
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return [(index + 1, freq, word) for index, (word, freq) in enumerate(sorted_freq)]

div_freq = "div-table"
headers_freq = ["Rank", "Count", "Word"]
data_freq = [(1, 52, "words"), (2, 50, "dog")]

def add_table(div_id, headers, data):
    print(f"<table id='{div_id}'>")
    print("<tr>")
    for header in headers:
        print(f"<th>{header}</th>")
    print("</tr>")
    for row in data:
        print("<tr>")
        for value in row:
            print(f"<td>{value}</td>")
        print("</tr>")
    print("</table>")

def process_data():
    input_str = get_user_input()
    cleaned_input = clean_input(input_str)
    freq_dict = word_freq(cleaned_input)
    sorted_freq = sort_by_value(freq_dict)
    
    add_table(div_freq, headers_freq, sorted_freq)

process_data()