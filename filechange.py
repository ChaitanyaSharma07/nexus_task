import pandas as pd

def excel_to_csv_pandas(excel_file, csv_file, sheet_name=0):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        # Convert the DataFrame to a CSV file
        # index=False prevents writing the DataFrame index as a column in the CSV
        df.to_csv(csv_file, index=False, encoding='utf-8')
        
        print(f"Successfully converted '{excel_file}' (Sheet: {sheet_name}) to '{csv_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_excel = 'your_workbook.xlsx'
output_csv = 'output_data.csv'
excel_to_csv_pandas("NEXUS_RECRUITMENT_DATA.xlsx", "nexus_data")
