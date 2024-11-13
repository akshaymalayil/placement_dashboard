import re
import spacy
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Function to extract contact information
def extract_contact_info(text):
    name = "--"
    phone = "--"
    email = "--"
    linkedin = "--"
    location = "--"
    
    # Search for email and phone number
    email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", text)
    phone_match = re.search(r"\+?\d[\d -]{8,12}\d", text)
    
    # Extract email and phone if found
    if email_match:
        email = email_match.group(0)
    if phone_match:
        phone = phone_match.group(0)
    
    # Extract name and location using spaCy entities
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON" and name == "--":
            name = ent.text
        elif ent.label_ == "GPE" and location == "--":  # Location entity
            location = ent.text
    
    # Search for LinkedIn profile link
    linkedin_match = re.search(r"(https?://www\.linkedin\.com/in/[A-Za-z0-9-]+)", text)
    if linkedin_match:
        linkedin = linkedin_match.group(0)
    
    return {"name": name, "phone": phone, "email": email, "linkedin": linkedin, "location": location}

# Function to extract education details
def extract_education(text):
    degree = "--"
    university = "--"
    grad_date = "--"
    
    # Extracting degree and university based on keywords
    degree_match = re.search(r"(Bachelor|Master|Engineer|B\.Tech|M\.Tech)", text)
    if degree_match:
        degree = degree_match.group(0)
    
    # Extracting graduation date
    grad_date_match = re.search(r"(20\d{2})", text)
    if grad_date_match:
        grad_date = grad_date_match.group(0)
    
    # Using spaCy for organization detection as university
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            university = ent.text
            break
    
    return {"degree": degree, "university": university, "graduation_date": grad_date}

# Function to extract skills
def extract_skills(text):
    skills = {
        "programming_languages": [],
        "software_tools": [],
        "technical_skills": []
    }
    
    # Define common keywords for skills
    programming_languages = ["C++", "Java", "Python", "SQL", "MongoDB", "HTML", "CSS"]
    software_tools = ["MATLAB", "AutoCAD", "SolidWorks"]
    technical_skills = ["circuit design", "3D modelling", "data analysis"]
    
    # Search for skills
    for lang in programming_languages:
        if lang in text:
            skills["programming_languages"].append(lang)
    for tool in software_tools:
        if tool in text:
            skills["software_tools"].append(tool)
    for skill in technical_skills:
        if skill in text:
            skills["technical_skills"].append(skill)
    
    # Fill missing fields with "--"
    for key in skills:
        if not skills[key]:
            skills[key] = ["--"]
    
    return skills

# Function to extract experience details
def extract_experience(text):
    experience = []
    
    # Regular expressions for job titles, companies, and dates
    job_title_match = re.findall(r"[A-Za-z\s]+ – [A-Za-z\s]+, [A-Za-z\s]+", text)
    if job_title_match:
        for job in job_title_match:
            experience.append(job)
    
    if not experience:
        experience = ["--"]
    
    return experience

# Main function to process resume
def process_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    contact_info = extract_contact_info(text)
    education = extract_education(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    
    # Compile the final resume data
    resume_data = {
        "contact_info": contact_info,
        "summary": "--",  # Assume no summary provided unless further processing is specified
        "education": education,
        "skills": skills,
        "experience": experience,
        "certifications": ["--"],  # Placeholder for simplicity
        "extracurricular_activities": ["--"],  # Optional
        "awards_honors": ["--"],  # Optional
        "volunteer_experience": ["--"],  # Optional
        "languages": ["--"]  # Optional
    }
    
    return resume_data

# Function to fill HTML profile with extracted resume data
# Function to fill HTML profile with extracted resume data
def fill_profile_html(resume_data, template_path, output_path):
    with open(template_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Helper function to safely set text content
    def set_text(soup, element_id, text):
        element = soup.find(id=element_id)
        if element:
            element.string = text

    # Fill the contact information
    set_text(soup, "name", resume_data["contact_info"].get("name", "--"))
    set_text(soup, "email", resume_data["contact_info"].get("email", "--"))
    set_text(soup, "phone", resume_data["contact_info"].get("phone", "--"))
    set_text(soup, "linkedin", resume_data["contact_info"].get("linkedin", "--"))
    set_text(soup, "location", resume_data["contact_info"].get("location", "--"))

    # Fill the profile summary
    set_text(soup, "summary", resume_data.get("summary", "--"))

    # Fill education details
    set_text(soup, "degree", resume_data["education"].get("degree", "--"))
    set_text(soup, "university", resume_data["education"].get("university", "--"))
    set_text(soup, "graduation_date", resume_data["education"].get("graduation_date", "--"))

    # Fill skills
    set_text(soup, "programming_languages", ", ".join(resume_data["skills"].get("programming_languages", ["--"])))
    set_text(soup, "software_tools", ", ".join(resume_data["skills"].get("software_tools", ["--"])))
    set_text(soup, "technical_skills", ", ".join(resume_data["skills"].get("technical_skills", ["--"])))

    # Fill experience
    experience_section = soup.find(id="experience")
    if experience_section:
        experience_section.clear()  # Clear previous entries if any
        for exp in resume_data.get("experience", ["--"]):
            experience_item = soup.new_tag("li")
            experience_item.string = exp
            experience_section.append(experience_item)

    # Save the modified HTML to a new file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(str(soup))
    print(f"Profile data filled and saved to {output_path}")


# Example usage
pdf_path = "RESUME.pdf"  # Replace with actual PDF path
template_path = "C:/Users/alakh/OneDrive/Desktop/BE_Project/Dashboard/profile.html"  # Replace with actual HTML template path
output_path = "C:/Users/alakh/OneDrive/Desktop/BE_Project/Dashboard/Filled_Profile.html"  # Output path for the filled HTML

resume_data = process_resume(pdf_path)
fill_profile_html(resume_data, template_path, output_path)
