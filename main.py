import streamlit as st
import psycopg2

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postres'
DB_PASSWORD = 'openpgpwd'

# Function to insert form data into PostgreSQL
def insert_data(name, email, message):
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    conn.commit()
    cur.close()
    conn.close()

# Streamlit app
def main():
    st.title("Contact Us Form")
    st.write("Please fill out the form below to get in touch.")

    # Form inputs
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    # Submit button
    if st.button("Submit"):
        if name and email and message:
            insert_data(name, email, message)
            st.success("Thank you! Your message has been submitted.")
            # Optionally, you can clear the form inputs after submission
            # name, email, message = '', '', ''

if __name__ == "__main__":
    main()
