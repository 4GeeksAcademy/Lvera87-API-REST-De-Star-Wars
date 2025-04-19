import os
from flask_admin import Admin
from models import db, User, Person, Planet, Vehicle, FavoritePerson,FavoritePlanet, FavoriteVehicle
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class UserModelView(ModelView): # esto es una clase que hereda de ModelView y sirve para personalizar el admin
        column_list = ('id','email', 'password', 'first_name', 'last_name', 'subscription_date', 'is_ative',"favorite_people", "favorite_planets", "favorite_vehicles")

    class PersonModelView(ModelView): 
        column_list = ("id", "name", "height", "mass", "hair_color", "skin_color", "eye_color" "birth_year", "gender", "homeworld_id", "homeworld", "favorited_by")

    class PlanetModelView(ModelView): 
        column_list = ("id", "name", "diameter", "orbital_period", "orbital_period", "gravity", "population", "climate", "terrain", "surface_water", "resident_ids", "favorited_by", "residents")

    class VehicleModelView(ModelView):
        column_list = ("id", "name", "model", "manufacturer", "cost_in_credits", "length", "max_atmosphering_speed", "crew", "passengers", "cargo_capacity", "consumables", "vehicle_class", "favorited_by")

    class FavoritePersonModelView(ModelView):
        column_list = ("user_id", "person_id", "user", "person")

    class FavoriteVehicleModelView(ModelView):
        column_list = ("user_id", "vehicle_id", "user", "vehicle")
        
    class FavoritePlanetModelView(ModelView):
        column_list = ("user_id", "planet_id", "user", "planet")

    # Add your models here, for example this is how we add a the User model to the admin

    admin.add_view(UserModelView(User, db.session)) # esto es para el modelo User y muestra los campos que queremos ver en el admin
    admin.add_view(PersonModelView(Person, db.session))
    admin.add_view(PlanetModelView(Planet, db.session))
    admin.add_view(VehicleModelView(Vehicle, db.session))
    admin.add_view(FavoritePersonModelView(FavoritePerson, db.session))
    admin.add_view(FavoritePlanetModelView(FavoritePlanet, db.session))
    admin.add_view(FavoriteVehicleModelView(FavoriteVehicle, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))