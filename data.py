import streamlit as st
import csv

# Streamlit app
def main():
    st.markdown("<h1 style='text-align: center; color: #ff5c5c;'>Registration</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #f76190;'>Match over a cup of coffee!</h3>", unsafe_allow_html=True)
    
    with st.form(key='registration_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        university = st.selectbox("University", [
            "National Forensic Sciences University",
            "Nirma University",
            "DAIICT (Dhirubhai Ambani Institute of Information and Communication Technology)",
            "Karnavati University",
            "GNLU (Gujarat National Law University)",
            "PDEU (Pandit Deendayal Energy University)"
        ])
        desc_yourself = st.text_area("Describe yourself in 10 words")
        hobbies_interests = st.text_area("List 5 hobbies and interests (comma-separated)")
        age = st.selectbox("Age", list(range(18, 26)))  # Dropdown for ages 18 to 25
        looking_for = st.text_area("What are you looking for in 10 words")
        
        submit_button = st.form_submit_button(label='Register')
    
    if submit_button:
        if len(desc_yourself.split()) <= 10 and len(looking_for.split()) <= 10 and len(hobbies_interests.split(',')) == 5:
            data = [name, email, phone, gender, university, desc_yourself, hobbies_interests, age, looking_for]
            
            # Append to CSV file
            with open("https://docs.google.com/spreadsheets/d/1_-NZB_ECz8MGrYwN5tlu-EGSxzpE735BHrTAP8cmO9w/", mode='a', newline='') as file:
                writer = csv.writer(file)
                # Write header if file is empty
                if file.tell() == 0:
                    writer.writerow(["Name", "Email", "Phone Number", "Gender", "University", "Describe Yourself", "Hobbies/Interests", "Age", "Looking For"])
                writer.writerow(data)
            
            st.success("Registration successful!")
        else:
            if len(desc_yourself.split()) != 10:
                st.error("Please describe yourself in exactly 10 words.")
            if len(looking_for.split()) != 10:
                st.error("Please describe what you're looking for in exactly 10 words.")
            if len(hobbies_interests.split(',')) != 5:
                st.error("Please list exactly 5 hobbies and interests.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Powered by <strong>CollegeCupid</strong></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
