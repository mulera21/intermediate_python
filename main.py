import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photos.jpeg",)

with col2:
    st.title("Edmond Mulera")
    content = """Hi, Iam Edmond Mulera a python programmer, a teacher and founder of next level company 
    i graduated in 2023 with a bachelor's degree in mathematics and computer science and specialised in computer engineering,
    from Kenya Methodist University in Kenya.
    i have done programming courses  in udemy to increase my skills in programming and at per now am focusing on,
     enrolling AWS course. The skills i have encompass writing Python code,
    debugging programs, and solving problems using Python scripts.also familiar with 
    popular Python libraries and frameworks such as streamlit,django and flask.
    """
    st.info(content)

content1 = ("""Below you can find some of the apps i have built in
            python feel free to contact me""")
st.info(content1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[sourcecode]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[sourcecode]({row['url']})")
