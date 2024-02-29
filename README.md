# URL Shortener Web Application  

live AWS Instance  : http://3.144.88.118:5000/  

##Introduction  

Welcome to the documentation for the URL shortener web application. This document provides a comprehensive   guide to understanding, deploying the URL shortener application built using Flask, a Python web framework. The application is hosted on AWS t2 instances.  


# Installation  

Clone the repository from GitHub:
git clone <repository-url>  

Navigate to the project directory:
cd url--shortner  

Install the required dependencies using pip:
pip install -r requirements.txt  

# Usage  
To run the URL shortener web application locally, execute the following command:

python app.py  

---------------------------------------------------------------------------
# ACHIEVEMENT
---------------------------------------------------------------------------  
Built a web page with a form for entering URLs.  
Shortens URLs and ensures unique slugs for each.  
Redirects shortened URLs to their original long URLs.  
Displays a 404 Not Found page for invalid slugs.  
Accepts and validates input URLs.  
Implements an algorithm to generate unique slugs.  
Stores URL mappings and fetches data efficiently.  
Responds to requests and performs redirection seamlessly.  
Validates entered URLs for correctness.  
Provides a user-friendly option to copy generated URLs to the clipboard.  
Calculates the maximum number of unique slugs possible.  
Allows users to edit the slug of generated URLs.  
Ensures uniqueness of custom slugs entered by users.  
Supports user accounts for managing and viewing created short URLs.  
Tracks visits to short URLs and provides analytics to owners.  
