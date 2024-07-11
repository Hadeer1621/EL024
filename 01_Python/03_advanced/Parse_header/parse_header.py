
import re
import openpyxl

def parse_header(header_file):
    function_prototypes = []
    unique_id_counter = 0
    id_prefix = "IDX"

    # Regular expression to match function prototypes
    func_proto_pattern = r'^\s*(\w+\s+\**\w+)\s*\((.*)\);$'

    with open(header_file, 'r') as file:
        for line in file:
            match = re.match(func_proto_pattern, line.strip())
            if match:
                return_type, parameters = match.groups()
                Prototypes = match.group()
                unique_id = f"{id_prefix}{unique_id_counter}"
                function_prototypes.append((Prototypes,unique_id, return_type, parameters))
                unique_id_counter += 1

    return function_prototypes

def write_to_excel(function_prototypes, output_file):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Function Prototypes'

    # Write headers
    sheet['A1'] = 'Prototypes'
    sheet['C1'] = 'ID'
    sheet['D1'] = 'Return Type'
    sheet['F1'] = 'Parameters'

    # Write function prototypes
    for row_idx, (Prototypes,unique_id, return_type, parameters) in enumerate(function_prototypes, start=2):
        sheet[f'A{row_idx}'] = Prototypes
        sheet[f'C{row_idx}'] =unique_id
        sheet[f'D{row_idx}'] = return_type
        sheet[f'F{row_idx}'] = parameters

    # Save workbook
    wb.save(output_file)
    print(f"Function prototypes written to {output_file}")

# Example usage
if __name__ == "__main__":
    header_file = input("Enter the path to the header file: ")
    excel_file = "function_prototypes.xlsx"
# Parse header file
function_prototypes = parse_header(header_file)
# Write to Excel
write_to_excel(function_prototypes, excel_file)
