import streamlit as st
import pandas as pd
import datetime
from io import BytesIO

def modify_file(uploaded_file):
    """Modify the uploaded Excel file by adding today's date to it."""
    df = pd.read_excel(uploaded_file)
    df['Modified Date'] = datetime.date.today()
    
    # Save modified file to BytesIO
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Modified')
    output.seek(0)
    
    return output


def main():
# Streamlit UI
    st.title("Excel File Modifier")

    # Upload file
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])

    if uploaded_file:
        modified_file = modify_file(uploaded_file)
        st.success("File has been modified!")
        
        # Provide download link
        st.download_button(label="Download Modified File",
                        data=modified_file,
                        file_name="modified_file.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        

if __name__ == '__main__':
    main()
