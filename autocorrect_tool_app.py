import streamlit as st
import language_tool_python

st.set_page_config(page_title="Autocorrect Tool", layout="centered")
st.title("✍️ AI Autocorrect Tool")
st.markdown("Improve your text with grammar and spelling corrections.")

st.markdown("""
<style>
    .stApp {
        background-color: #cceeff; /* Sky blue background */
        color: #003366; /* Darker blue text */
    }
    h1, h2, h3, h4, h5, h6, p, div {
        color: #003366 !important;
    }
</style>
""", unsafe_allow_html=True)

tool = language_tool_python.LanguageTool('en-US')

input_text = st.text_area("Enter your text:", height=200)

if st.button("Correct Text") and input_text.strip():
    corrected_text = tool.correct(input_text)
    matches = tool.check(input_text)

    st.subheader("✅ Corrected Text")
    st.write(corrected_text)

    if matches:
        st.subheader("🔍 Suggestions")
        for match in matches:
            if match.replacements:
                st.markdown(f"**{match.context}** ➜ `{', '.join(match.replacements)}`")
    else:
        st.success("No issues found! ✨")
else:
    st.info("✏️ Type something above and click 'Correct Text'")
