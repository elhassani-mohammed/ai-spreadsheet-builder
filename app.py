import streamlit as st

from ai_service import generate_dataframe
from config import (
    APP_DESCRIPTION,
    EXPORT_FILE_NAME,
    FOOTER_HTML,
    MODEL_OPTIONS,
    PAGE_ICON,
    PAGE_LAYOUT,
    PAGE_TITLE,
    THEME_OPTIONS,
)
from workbook_service import build_excel_file


def render_sidebar():
    with st.sidebar:
        st.header("⚙️ Settings")
        api_key = st.text_input("OpenRouter API Key", type="password")
        st.caption("🔑 Get your API key from [OpenRouter Dashboard](https://openrouter.ai/keys)")

        model_choice = st.selectbox("AI Engine", MODEL_OPTIONS)
        st.write("---")
        st.header("🎨 Styling Controls")
        theme_selection = st.selectbox("Sheet Theme", THEME_OPTIONS)
        include_summary = st.checkbox("Append Auto-Calculated Totals Row", value=True)

    return api_key, model_choice, theme_selection, include_summary


def handle_generate_click(api_key: str, model_choice: str, user_prompt: str):
    if not api_key:
        st.error("Please provide an OpenRouter API key.")
        return

    if not user_prompt:
        st.warning("Please supply a descriptive prompt.")
        return

    with st.spinner("Processing token-efficient compression schemas..."):
        try:
            st.session_state.working_df = generate_dataframe(
                api_key=api_key,
                model_name=model_choice,
                user_prompt=user_prompt,
            )
            st.success("Data successfully generated!")
        except Exception as exc:
            st.error(f"Failed to generate structured data: {exc}")


def handle_export_click(edited_df, theme_selection: str, include_summary: bool):
    try:
        excel_bytes = build_excel_file(
            df=edited_df,
            theme_name=theme_selection,
            include_summary=include_summary,
        )
        st.success("Excel sheet parsed, stylized, and verified completely safely.")
        st.download_button(
            label="📥 Download Production-Ready Excel File",
            data=excel_bytes,
            file_name=EXPORT_FILE_NAME,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
    except Exception as exc:
        st.error(f"Compilation pipeline error: {exc}")


def main():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=PAGE_LAYOUT)
    st.title(PAGE_TITLE)
    st.write(APP_DESCRIPTION)

    api_key, model_choice, theme_selection, include_summary = render_sidebar()

    user_prompt = st.text_area(
        "What specific dataset should the agent curate?",
        placeholder=(
            "e.g., A projection list of 10 international markets for solar energy "
            "expansion with Columns: Country, Target MW, Entry Risk Index (1-10), "
            "Setup Cost Millions USD."
        ),
        height=100,
    )

    if "working_df" not in st.session_state:
        st.session_state.working_df = None

    if st.button("Generate", type="primary"):
        handle_generate_click(api_key, model_choice, user_prompt)

    if st.session_state.working_df is not None:
        st.markdown("### 📝 Interactive Data Validation Studio")
        st.info(
            "The AI work is rendered below. You can safely change cells, delete "
            "entries, or append rows right within the table grid."
        )

        edited_df = st.data_editor(
            st.session_state.working_df,
            num_rows="dynamic",
            use_container_width=True,
        )

        if st.button("🚀 Compile and Format Final Excel Workbook"):
            handle_export_click(edited_df, theme_selection, include_summary)

    st.markdown("---")
    st.markdown(FOOTER_HTML, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
