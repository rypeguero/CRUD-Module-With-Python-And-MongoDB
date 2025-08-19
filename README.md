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

# Screenshots
![Dashboard Overview](assets/dashboard_overview.png)
![Filtered Table](assets/filtered_table.png)
![Breed Distribution Chart](assets/breed_chart.png)
![Map View](assets/map_view.png)


  # Reflection
- ## Questions and Answers

### 1. How do you write programs that are maintainable, readable, and adaptable?  
Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
 
For this project I separated concerns into a small, well-named CRUD module and a dashboard UI. The `AnimalShelter` class encapsulates database access (connect, create, read, update, delete) so the dashboard stays focused on UI logic instead of raw database calls. Clear method names, docstrings, and centralized error handling with `PyMongoError` make failures easier to diagnose and fix.  

**Advantages in this project:**  
- Modular and reusable code  
- One place to update database logic  
- Easier to test and maintain  

**Future use:**  
I can reuse this CRUD module in other analytics notebooks, a Flask/FastAPI microservice, or automation scripts. Extending it with schema validation, logging, and typed models (Pydantic) would make it even more production-ready.  

---

### 2. How do you approach a problem as a computer scientist?  
Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
 
I start by clarifying requirements, mapping them to data flows, and choosing minimal tools that satisfy constraints. For Grazioso Salvare, I aligned requirements (filtering candidates, visualizing breeds, mapping locations) to dashboard components (table, chart, map) and connected them to the CRUD layer. Compared with earlier coursework, I relied more on **iterative prototyping** (getting one feature working end-to-end) and **observable state** (tables/charts/map all update from the same filtered dataset).  

**Strategies for future databases:**  
- Define schema and CRUD contract early  
- Add validation and logging early  
- Prototype smallest vertical slice before scaling  
- Provide fallback/seed data for demos and tests  

---

### 3. What do computer scientists do, and why does it matter?  
How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists translate domain needs into reliable systems. In this project, I turned shelter data into actionable insights: the dashboard filters animals by rescue profile, shows breed distribution, and pins a selected animal’s location so trainers can act faster.  

**For Grazioso Salvare, this means:**  
- Saving time by filtering shelter records quickly  
- Making better selections for search-and-rescue training  
- Improving outcomes through data-driven decision making  

This demonstrates how computer science work directly impacts real organizations.  

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
