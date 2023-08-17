import streamlit as st

# Page Title
st.title("Streamlit Website Example")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("This is some text.")

# Markdown
st.markdown("### This is a markdown header")

# Image
st.image("https://via.placeholder.com/150")

# Button
if st.button("Click me"):
    st.write("Button clicked!")

# Checkbox
checkbox_state = st.checkbox("Check me")
if checkbox_state:
    st.write("Checkbox is checked!")

# Radio Buttons
radio_option = st.radio("Choose an option", ("Option 1", "Option 2", "Option 3"))
st.write(f"Selected option: {radio_option}")

# Selectbox
select_option = st.selectbox("Select an option", ["Option A", "Option B", "Option C"])
st.write(f"Selected option: {select_option}")

# Multiselect
multiselect_options = st.multiselect("Select multiple options", ["Option X", "Option Y", "Option Z"])
st.write("Selected options:", multiselect_options)

# Slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"Selected value: {slider_value}")

# Text Input
text_input = st.text_input("Enter some text", "Default text")
st.write("Entered text:", text_input)

# Number Input
number_input = st.number_input("Enter a number", 0.0, 100.0, 50.0)
st.write("Entered number:", number_input)

# Text Area
text_area = st.text_area("Enter a long text", "Default long text")
st.write("Entered text:", text_area)

# Date Input
date_input = st.date_input("Select a date")
st.write("Selected date:", date_input)

# Time Input
time_input = st.time_input("Select a time")
st.write("Selected time:", time_input)

# File Uploader
uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "pdf"])
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

# Progress Bar
progress_value = st.progress(0)
for i in range(101):
    progress_value.progress(i)
    st.write(f"Progress: {i}%")
    
# Placeholder
placeholder = st.empty()
placeholder.text("This is a placeholder with custom text")

# Expander
with st.expander("Click to expand"):
    st.write("This is some hidden content.")

# Code Block
with st.echo():
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Streamlit"))

# Columns
col1, col2, col3 = st.columns(3)
col1.write("Column 1")
col2.write("Column 2")
col3.write("Column 3")
