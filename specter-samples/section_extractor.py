import re

def extract_sections(file_path):
    """
    Extracts all sections that start with a Roman numeral, followed by a capitalized heading,
    and includes the first line of section content.
    Returns a list of tuples: (section_heading, first_content_line)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: Roman numeral at line start, dot, newline, capitalized heading, newline, then content line
    pattern = re.compile(
        r"^([IVXLCDM]+)\.\s*\n([A-Z][A-Z\s&/-]+)\n([^\n]+)",
        re.MULTILINE
    )

    results = []
    for match in pattern.finditer(content):
        roman = match.group(1)
        heading = match.group(2).strip()
        first_content = match.group(3).strip()

        section_text = f"{roman}.\n{heading}\n{first_content}"
        results.append(section_text)
    return results

if __name__ == "__main__":
    # update file path here
    sections = extract_sections('file_path')
    for section in sections:
        print("--- Section ---")
        print(section)
        print()