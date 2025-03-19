# Project: Flask REST API with SQL Server

## Description
This project is a RESTful API built using Flask, Flask-RESTful, and SQLAlchemy, integrated with SQL Server. The API allows CRUD operations on a user model.

## Technologies Used
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQL Server
- Python

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ertiza/APIs.git
   ```
2. Navigate to the project directory:
   ```bash
   cd APIs
   ```
3. Create a virtual environment:
   ```bash
   python -m venv my_api_environment
   ```
4. Activate the virtual environment:
   ```bash
   # On Windows
   my_api_environment\Scripts\activate
   
   # On Mac/Linux
   source my_api_environment/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Database Configuration
- **Database Name:** Adventures works
- **Server Name:** multi-la-asw1
- **Authentication:** 12AP/AWS-25

Ensure SQL Server is running and update `SQLALCHEMY_DATABASE_URI` in the Flask app configuration as needed.

## Running the API
```bash
python api.py
```

## API Endpoints
- `GET /api/users/` - Retrieve all users
- `POST /api/users/` - Create a new user
- `GET /api/users/<int:id>` - Retrieve a specific user
- `PATCH /api/users/<int:id>` - Update a user
- `DELETE /api/users/<int:id>` - Delete a user

## Author
- **LinkedIn:** [Ertiza Abbas](https://www.linkedin.com/in/abbas-ertiza/)
- **SSRN:** [Ertiza Abbas (Author ID: 7375922)](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7375922)
- **ORCID:** [0009-0000-5529-1683](https://orcid.org/0009-0000-5529-1683)

## License
This project is licensed under the MIT License.

