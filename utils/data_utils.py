import re
import json
import os
from datetime import datetime

def sanitize_input(text):
    sanitized = re.sub(r'[^\w\s@.+\-:,?!()]', '', text)
    return sanitized.strip()

def extract_candidate_info(messages):
    # Initialize candidate info
    candidate_info = {
        "name": None,
        "email": None,
        "phone": None,
        "experience": None,
        "position": None,
        "location": None,
        "tech_stack": None,
        "questions_asked": [],
        "answers": []
    }
    conversation_text = " ".join([m["content"] for m in messages if m["role"] in ["user", "assistant"]])

    name_match = re.search(r"[Mm]y name is ([^.]+)", conversation_text)
    if name_match:
        candidate_info["name"] = name_match.group(1).strip()
    
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", conversation_text)
    if email_match:
        candidate_info["email"] = email_match.group(0)
    
    phone_match = re.search(r"(\+\d{1,3}|\d{1,4})[\s.-]?\d{3}[\s.-]?\d{3}[\s.-]?\d{4}", conversation_text)
    if phone_match:
        candidate_info["phone"] = phone_match.group(0)
    
    exp_match = re.search(r"(\d+)[\s]*(year|years)", conversation_text, re.IGNORECASE)
    if exp_match:
        candidate_info["experience"] = f"{exp_match.group(1)} {exp_match.group(2)}"
    
    return candidate_info

def save_candidate_data(candidate_info):
    """Save candidate data to a JSON file."""
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name_part = ""
    if candidate_info.get("name"):
        name_part = f"_{candidate_info['name'].replace(' ', '_')}"
    
    filename = f"data/candidate{name_part}_{timestamp}.json"
    
    # Save to file
    with open(filename, "w") as f:
        json.dump(candidate_info, f, indent=2)
    
    return filename