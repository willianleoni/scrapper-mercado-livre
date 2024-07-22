import pandas as pd
from datetime import datetime
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import PatternFill, Alignment
from tqdm import tqdm

def products_to_dataframe(products):
    return pd.DataFrame(products)

def add_discount_column(df):
    if 'price' in df.columns and 'discounted_price' in df.columns:
        df['price'] = df['price'].str.replace('.', '').astype(float, errors='ignore')
        df['discounted_price'] = df['discounted_price'].str.replace('.', '').astype(float, errors='ignore')
        df['discount'] = ((df['price'] - df['discounted_price']) / df['price']) * 100
    else:
        df['discount'] = None
    return df

def convert_discount_to_percentage(df):
    df['discount'] = df['discount'].fillna(0)
    df['discount'] = df['discount'].apply(lambda x: str(int(x)) + '%' if not pd.isna(x) else '0%')
    return df

def sort_by_discount(df):
    df['discount_numeric'] = df['discount'].str.rstrip('%').astype(float)
    return df.sort_values(by='discount_numeric', ascending=False).drop(columns=['discount_numeric'])

def save_to_excel(df):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'../data/products_{timestamp}.xlsx'

    # Cria um novo Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    # Adiciona o DataFrame ao Workbook
    for r_idx, row in tqdm(enumerate(dataframe_to_rows(df, index=False, header=True), 1), desc="Writing to Excel"):
        for c_idx, value in enumerate(row, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=value)
            if r_idx == 1:  # Formata a linha de cabeçalho
                cell.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                if r_idx % 2 == 0:
                    cell.fill = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")  # Cinza para linhas pares

    # Ajusta o tamanho das colunas
    for column in ws.columns:
        max_length = 0
        column = [cell for cell in column]
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column[0].column_letter].width = adjusted_width

    wb.save(filename)
    print(f"DataFrame saved and formatted in {filename}")
