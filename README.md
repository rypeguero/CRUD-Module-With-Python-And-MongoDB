# Grazioso Salvare Dashboard

## Overview
This project was developed for **CS-340: Client/Server Development** at Southern New Hampshire University (SNHU).  
It demonstrates connecting a **MongoDB database** to a **Python CRUD module** and an interactive **dashboard** using Jupyter Dash.  

The project simulates a real-world client, **Grazioso Salvare**, who needs to identify animals in shelters that are good candidates for search-and-rescue training.  

---

## Features
- **CRUD Python Module (`animal_shelter.py`)**  
  - Encapsulates Create, Read, Update, and Delete operations with MongoDB  
  - Centralized error handling with `PyMongoError`  
  - Reusable design for future projects  

- **Interactive Dashboard (`ProjectTwoDashboard.ipynb`)**  
  - Filter animals by criteria (age, breed, outcome type, etc.)  
  - Display results in a sortable, paginated data table  
  - Show live charts (breed distribution, outcome distribution)  
  - Display an interactive map with the selected animal’s location  

- **CSV Fallback**  
  Works with local data if MongoDB is unavailable  

- **Error Handling**  
  Graceful exception handling to keep dashboard functional  

---

## Installation / Quick Start
```bash
# Clone the repository
git clone https://github.com/<your-username>/cs340-grazioso-dashboard.git
cd cs340-grazioso-dashboard

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Jupyter Notebook
jupyter notebook ProjectTwoDashboard.ipynb
