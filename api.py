from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLAlchemy URI to connect to SQL Server using Windows Authentication
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://DESKTOP-QJO9A7U/AdventureWorksDW2019?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking (optional)

# Initialize SQLAlchemy and the API
db = SQLAlchemy(app)
api = Api(app)

# Define the User model for the SQL Server database
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"
    

    # Set up request parsing for creating users
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")

# Define fields for returning data in the response
userFields = {
    'CustomerKey': fields.Integer,
    'FirstName': fields.String,
    'LastName': fields.String,
    'EnglishOccupation': fields.String,
    'email': fields.String,
}


# Create a resource for handling all users

# Create a resource for handling all users
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
# Create a resource for handling a single user by ID
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        return user

    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user

    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users
# Set up routes for the API
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

# Home route
@app.route('/')
def home():
    return '<h1>Flask REST API connected to SQL Server</h1>'

if __name__ == '__main__':
    app.run(debug=True)