# Phase 3 Code Challenge: Library Management System

This project is part of the **Phase 3 Code Challenge**.  
It models a simple **Library Management System** using Python and Object-Oriented Programming (OOP).  

The main goal is to demonstrate:
- Class design
- Object relationships (one-to-many, many-to-many)
- Aggregate methods
- Following Python best practices

---

## 📖 Project Overview

We created three main classes:

- **Author** → can write multiple books  
- **Book** → belongs to one author and one publisher  
- **Publisher** → can publish multiple books, and therefore multiple authors  

This structure lets us ask questions like:
- How many books has an author written?
- Which publisher published the most books?
- Which authors are connected to a given publisher?

---

## 🛠️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone git@github.com:Kujo254/phase-3-code-challenge.git
   cd phase-3-code-challenge

2. Install dependencies
     pip install pytest
3. Run tests
      pytest
