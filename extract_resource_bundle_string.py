import re

def extract_values(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use a regular expression to find all the strings inside quotes (both double and single) that come after a colon
    pattern = r"['\"]\s*:\s*['\"]([^'\"].*?)['\"]"
    matches = re.findall(pattern, content)

    return matches

values = extract_values('app.component.ts')

# Save the extracted values into an output file with UTF-8 encoding
with open("output.txt", "w", encoding='utf-8') as out_file:
    for value in values:
        out_file.write(value + "\n")
