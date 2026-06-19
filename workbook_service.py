import io

import pandas as pd

from config import EXPORT_SHEET_NAME
from excel_formatter import apply_excel_theme


def append_summary_row(df: pd.DataFrame) -> pd.DataFrame:
    """Append a totals row for numeric columns and labels for the first text column."""
    summary_row = {}

    for column_name in df.columns:
        if pd.api.types.is_numeric_dtype(df[column_name]):
            summary_row[column_name] = df[column_name].sum()
        else:
            summary_row[column_name] = "Total / Summary" if column_name == df.columns[0] else ""

    return pd.concat([df, pd.DataFrame([summary_row])], ignore_index=True)


def build_excel_file(df: pd.DataFrame, theme_name: str, include_summary: bool) -> bytes:
    """Create the final Excel workbook in memory and return its bytes."""
    final_df = append_summary_row(df.copy()) if include_summary else df.copy()

    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        final_df.to_excel(writer, index=False, sheet_name=EXPORT_SHEET_NAME)
        apply_excel_theme(writer, final_df, theme_name)

    return excel_buffer.getvalue()
