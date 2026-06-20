PAGE_TITLE = "AI Spreadsheet Builder"
PAGE_ICON = "🚀"
PAGE_LAYOUT = "wide"

APP_DESCRIPTION = (
    "Secure architecture leveraging high-compression JSON and interactive "
    "Streamlit controls."
)

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

MODEL_OPTIONS = [
    "meta-llama/llama-3-70b-instruct",
    "meta-llama/llama-4-scout",
]

THEME_OPTIONS = [
    "Classic Navy",
    "Emerald Green",
    "Charcoal Tech",
]

DEFAULT_THEME = "Classic Navy"
EXPORT_SHEET_NAME = "Data Export"
EXPORT_FILE_NAME = "secure_templated_report.xlsx"

SYSTEM_INSTRUCTION = (
    "You are a dense vector data serializer. Your sole purpose is to output "
    "data matching the user prompt using highly compressed 'split' JSON. "
    "Never output conversational filler or text.\n\n"
    "Output format must strictly be standard JSON with exactly two fields "
    "('columns' and 'data'):\n"
    "{\n"
    '  "columns": ["Column1", "Column2"],\n'
    '  "data": [["Row1Value1", 100], ["Row2Value1", 200]]\n'
    "}"
)

FOOTER_HTML = """
<div style="text-align: center; color: #888888; font-size: 0.85rem;">
    AI Spreadsheet Builder • Build By Mohammed El Hassani

</div>
"""
