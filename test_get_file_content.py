from functions.get_file_content import get_file_content

print(f"Länge des Outputs: {len(get_file_content("calculator","lorem.txt"))}")
print(get_file_content("calculator","lorem.txt"))

print(f"Länge des Outputs: {len(get_file_content("calculator","main.py"))}")
print(get_file_content("calculator","main.py"))

print(f"Länge des Outputs: {len(get_file_content("calculator","pkg/calculator.py"))}")
print(get_file_content("calculator","pkg/calculator.py"))

print(f"Länge des Outputs: {len(get_file_content("calculator","/bin/cat"))}")
print(get_file_content("calculator","/bin/cat"))

print(f"Länge des Outputs: {len(get_file_content("calculator","pkg/does_not_exist.py"))}")
print(get_file_content("calculator","pkg/does_not_exist.py"))