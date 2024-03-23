"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Favorite_Planet, Favorite_Character

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Populate data before starting the API
def populate():
    u1 = User(username='john_doe', email='john_doe@example.com', password="password1")
    u2 = User(username='jane_doe', email='jane_doe@example.com', password="password2")
    u3 = User(username='bob_smith', email='bob_smith@example.com', password="password3")
    u4 = User(username='alice_johnson', email='alice_johnson@example.com', password="password4")
    u5 = User(username='michael_brown', email='michael_brown@example.com', password="password5")
    u6 = User(username='sarah_wilson', email='sarah_wilson@example.com', password="password6")

    c1 = Character(name='Luke Skywalker', birth_year='19BBY', gender='male', height='172.0', eye_color='blue', hair_color='blond', skin_color='fair', item_type='character')
    c2 = Character(name='C-3PO', birth_year='112BBY', gender='', height='167.0', eye_color='yellow', hair_color='n/a', skin_color='gold', item_type='character')
    c3 = Character(name='R2-D2', birth_year='33BBY', gender='n/a', height='96.0', eye_color='red', hair_color='n/a', skin_color='white, blue', item_type='character')
    c4 = Character(name='Darth Vader', birth_year='41.9BBY', gender='male', height='202.0', eye_color='yellow', hair_color='none', skin_color='white', item_type='character')
    c5 = Character(name='Leia Organa', birth_year='19BBY', gender='female', height='150.0', eye_color='brown', hair_color='brown', skin_color='light', item_type='character')
    c6 = Character(name='Owen Lars', birth_year='52BBY', gender='male', height='178.0', eye_color='blue', hair_color='brown, grey', skin_color='light', item_type='character')
    c7 = Character(name='Anakin Skywalker', birth_year='41.9BBY', gender='male', height='188.0', eye_color='blue', hair_color='blond', skin_color='fair', item_type='character')
    c8 = Character(name='Padmé Amidala', birth_year='46BBY', gender='female', height='165.0', eye_color='brown', hair_color='brown', skin_color='light', item_type='character')
    c9 = Character(name='Obi-Wan Kenobi', birth_year='57BBY', gender='male', height='182.0', eye_color='blue-gray', hair_color='auburn, white', skin_color='fair', item_type='character')
    c10 = Character(name='Yoda', birth_year='896BBY', gender='male', height='66.0', eye_color='brown', hair_color='white', skin_color='green', item_type='character')
    c11 = Character(name='Qui-Gon Jinn', birth_year='92BBY', gender='male', height='193.0', eye_color='blue', hair_color='brown', skin_color='fair', item_type='character')
    c12 = Character(name='Mace Windu', birth_year='72BBY', gender='male', height='188.0', eye_color='brown', hair_color='none', skin_color='dark', item_type='character')
    c13 = Character(name='Count Dooku', birth_year='102BBY', gender='male', height='193.0', eye_color='brown', hair_color='white', skin_color='fair', item_type='character')
    c14 = Character(name='Darth Maul', birth_year='54BBY', gender='male', height='175.0', eye_color='yellow', hair_color='none', skin_color='red', item_type='character')
    c15 = Character(name='Jango Fett', birth_year='66BBY', gender='male', height='183.0', eye_color='brown', hair_color='black', skin_color='tan', item_type='character')
    c16 = Character(name='Boba Fett', birth_year='31.5BBY', gender='male', height='183.0', eye_color='brown', hair_color='black', skin_color='fair', item_type='character')
    c17 = Character(name='Rey', birth_year='15ABY', gender='female', height='170.0', eye_color='hazel', hair_color='brown', skin_color='light', item_type='character')
    c18 = Character(name='Finn', birth_year='15ABY', gender='male', height='178.0', eye_color='dark', hair_color='black', skin_color='dark', item_type='character')
    c19 = Character(name='Poe Dameron', birth_year='15ABY', gender='male', height='172.0', eye_color='brown', hair_color='brown', skin_color='light', item_type='character')
    c20 = Character(name='Kylo Ren', birth_year='5ABY', gender='male', height='189.0', eye_color='hazel', hair_color='black', skin_color='fair', item_type='character')

    p1 = Planet(name='Tatooine', population='200000', terrain='desert', diameter='10465.0', climate='arid', rotation_period='23.0', item_type='planet')
    p2 = Planet(name='Alderaan', population='2000000000', terrain='grasslands, mountains', diameter='12500.0', climate='temperate', rotation_period='24.0', item_type='planet')
    p3 = Planet(name='Yavin IV', population='1000', terrain='jungle, rainforests', diameter='10200.0', climate='temperate, tropical', rotation_period='24.0', item_type='planet')
    p4 = Planet(name='Hoth', population='5000', terrain='tundra, ice caves, mountain ranges', diameter='7200.0', climate='frozen', rotation_period='23.0', item_type='planet')
    p5 = Planet(name='Dagobah', population='6500', terrain='swamp, jungles', diameter='8900.0', climate='murky', rotation_period='23.0', item_type='planet')
    p6 = Planet(name='Bespin', population='6000000', terrain='gas giant', diameter='118000.0', climate='temperate', rotation_period='12.0', item_type='planet')
    p7 = Planet(name='Endor', population='30000000', terrain='forests, mountains, lakes', diameter='4900.0', climate='temperate', rotation_period='18.0', item_type='planet')
    p8 = Planet(name='Naboo', population='4500000000', terrain='grassy hills, swamps, forests, mountains', diameter='12120.0', climate='temperate', rotation_period='26.0', item_type='planet')
    p9 = Planet(name='Coruscant', population='1000000000000', terrain='cityscape, mountains', diameter='12240.0', climate='temperate', rotation_period='24.0', item_type='planet')
    p10 = Planet(name='Kamino', population='1000000000', terrain='ocean', diameter='19720.0', climate='temperate', rotation_period='27.0', item_type='planet')
    p11 = Planet(name='Geonosis', population='100000000000', terrain='rock, desert, mountain, barren', diameter='11370.0', climate='temperate, arid', rotation_period='30.0', item_type='planet')
    p12 = Planet(name='Utapau', population='95000000', terrain='scrublands, savanna, canyons, sinkholes', diameter='12900.0', climate='temperate, arid, windy', rotation_period='27.0', item_type='planet')
    p13 = Planet(name='Mustafar', population='20000', terrain='volcanoes, lava rivers, mountains, caves', diameter='4200.0', climate='hot', rotation_period='36.0', item_type='planet')
    p14 = Planet(name='Kashyyyk', population='45000000', terrain='jungle, forests, lakes, rivers', diameter='12765.0', climate='tropical', rotation_period='26.0', item_type='planet')
    p15 = Planet(name='Polis Massa', population='1000000', terrain='airless asteroid', diameter='0.0', climate='artificial temperate', rotation_period='24.0', item_type='planet')
    p16 = Planet(name='Mygeeto', population='19000000', terrain='glaciers, mountains, ice canyons', diameter='10088.0', climate='frigid', rotation_period='12.0', item_type='planet')
    p17 = Planet(name='Felucia', population='8500000', terrain='fungus forests', diameter='9100.0', climate='hot, humid', rotation_period='34.0', item_type='planet')
    p18 = Planet(name='Cato Neimoidia', population='10000000', terrain='mountains, fields, forests, rock arches', diameter='0.0', climate='temperate, moist', rotation_period='25.0', item_type='planet')

    db.session.add_all([u1, u2, u3, u4, u5, u6, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18])
    db.session.commit()
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_all_user():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users)) 
    print("GET all_users: ", all_users)
    return jsonify(all_users), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    user = User.query.get(id)

    if user is None:
        raise APIException('User not found', status_code=404)

    print("GET single user: ", user)
    return jsonify(user.serialize()), 200

@app.route('/user', methods=['POST'])
def create_user():
    request_body = request.get_json()
    username = request_body.get("username")
    email = request_body.get("email")
    password = request_body.get("password")
    
    # Check if user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400
    
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify(request_body), 200

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    request_body = request.get_json()
    user = User.query.get(user_id)

    if user is None:
        raise APIException('User not found', status_code=404)
    if "username" in request_body:
        user.username = request_body["username"]
    if "email" in request_body:
        user.email = request_body["email"]
    if "password" in request_body:
        user.password = request_body["password"]
    
    db.session.commit()

    print("User property updated: ", request_body)
    return jsonify(request_body), 200

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    if user is None:
        raise APIException('User not found', status_code=404)

    db.session.delete(user)
    db.session.commit()
    response_body = {
         "msg": "User delete successful",
    }
    return jsonify(response_body), 200
@app.route('/populate', methods=['GET'])
def handle_populate():
    try:
        with app.app_context():
            # Check if data is already populated
            if User.query.first() is not None:
                response_body = {
                    "msg": "Data already populated"
                }
                return jsonify(response_body), 200
            
            # Populate data
            populate()
            
            response_body = {
                "msg": "Data populated successfully"
            }
            return jsonify(response_body), 200
    except Exception as e:
        response_body = {
            "error": str(e)
        }
        return jsonify(response_body), 500
@app.route('/people', methods=['GET'])
def get_all_people():
    try:
        people = Character.query.all()
        result = []
        for person in people:
            person_data = {
                "id": person.id,
                "name": person.name,
                "birth_year": person.birth_year,
                "gender": person.gender,
                "height": person.height,
                "eye_color": person.eye_color,
                "hair_color": person.hair_color,
                "skin_color": person.skin_color
            }
            result.append(person_data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
        person = Character.query.get(people_id)
        if person is None:
            return jsonify({"error": "Character not found"}), 404
        person_data = {
            "id": person.id,
            "name": person.name,
            "birth_year": person.birth_year,
            "gender": person.gender,
            "height": person.height,
            "eye_color": person.eye_color,
            "hair_color": person.hair_color,
            "skin_color": person.skin_color
        }
        return jsonify(person_data), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():
        planets = Planet.query.all()
        result = []
        for planet in planets:
            planet_data = {
                "id": planet.id,
                "name": planet.name,
                "population": planet.population,
                "terrain": planet.terrain,
                "diameter": planet.diameter,
                "climate": planet.climate,
                "rotation_period": planet.rotation_period
            }
            result.append(planet_data)
        return jsonify(result), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
        planet = Planet.query.get(planet_id)
        if planet is None:
            return jsonify({"error": "Planet not found"}), 404
        planet_data = {
            "id": planet.id,
            "name": planet.name,
            "population": planet.population,
            "terrain": planet.terrain,
            "diameter": planet.diameter,
            "climate": planet.climate,
            "rotation_period": planet.rotation_period
        }
        return jsonify(planet_data), 200
    
###### Favorites ########
@app.route('/user/favorites/<int:user_id>', methods=['POST'])
def add_favorite(user_id):
    request_body = request.get_json()
    item_id = request_body.get("item_id")
    item_type = request_body.get("item_type")
    
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    
    if item_type == "planet":
        existing_planet = Planet.query.get(item_id)
        if existing_planet is None:
            raise APIException('Planet not found', status_code=404)
        existing_favorite = Favorite_Planet.query.filter_by(user_id=user_id, item_id=item_id).first()
        if existing_favorite:
            raise APIException('Favorite planet already exists', status_code=400)
        favorite = Favorite_Planet(user_id=user_id, item_id=item_id)
    elif item_type == "character":
        existing_character = Character.query.get(item_id)
        if existing_character is None:
            raise APIException('Character not found', status_code=404)
        existing_favorite = Favorite_Character.query.filter_by(user_id=user_id, item_id=item_id).first()
        if existing_favorite:
            raise APIException('Favorite character already exists', status_code=400)
        favorite = Favorite_Character(user_id=user_id, item_id=item_id)
    else:
        raise APIException('Invalid item type', status_code=400)
    
    db.session.add(favorite)
    db.session.commit()
    
    return jsonify({"message": f"Item with id {item_id} and type {item_type} has been successfully added to user with id {user_id}"}), 200
@app.route('/user/favorites/all/<int:user_id>', methods=['GET'])
def get_user_favorites(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    
    favorite_planets = Favorite_Planet.query.filter_by(user_id=user_id).all()
    favorite_characters = Favorite_Character.query.filter_by(user_id=user_id).all()
    if not favorite_planets and not favorite_characters:
        raise APIException('No favorites found', status_code=404)
    favorites = {
        "favorite_planets": list(map(lambda x: Planet.query.get(x.serialize()['item_id']).serialize(), favorite_planets)),
        "favorite_characters": list(map(lambda x: Character.query.get(x.serialize()['item_id']).serialize(), favorite_characters))
    }
    user = jsonify(user.serialize())
    msg = {
            "message": "Favorites List found successfully",
            "user" : user.json,
            "favorites" : favorites
        }
    return jsonify(msg), 200
@app.route('/user/favorites/<int:user_id>/<item_type>/<int:item_id>', methods=['GET'])
def get_favorite(user_id,item_type, item_id):
    favorite = None
    try:
        user = User.query.get(user_id)
        if user is None:
            raise APIException('User not found', status_code=404)
        elif item_type == "planet":
            favorite_planet = Favorite_Planet.query.filter_by(user_id=user_id,item_id=item_id).first()
            if favorite_planet is None:
                raise APIException('Favorite planet not found', status_code=404)
            favorite = Planet.query.get(item_id)
            
        elif item_type == "character":
            favorite_character = Favorite_Character.query.filter_by(user_id=user_id,item_id=item_id).first()
            if favorite_character is None:
                raise APIException('Favorite character not found', status_code=404)
            favorite = Character.query.get(item_id)
            
        else:
            raise APIException('Invalid item type', status_code=400)
        favorite = jsonify(favorite.serialize())
        user = jsonify(user.serialize())
        msg = {
            "message": f"Favorite {item_type} found successfully",
            "user" : user.json,
            "item" : favorite.json
        }
        return jsonify(msg), 200
    
    except APIException as e:
        return jsonify({"error": str(e.message)}), e.status_code

@app.route('/user/favorites/<int:user_id>/<item_type>/<int:item_id>', methods=['DELETE'])
def delete_favorite(user_id,item_type,item_id):
    favorite = None
    try:
        user = User.query.get(user_id)
        if user is None:
            raise APIException('User not found', status_code=404)
        elif item_type == "planet":
            favorite = Favorite_Planet.query.filter_by(user_id=user_id,item_id=item_id).first()
            if favorite is None:
                raise APIException('Favorite planet not found', status_code=404)
        elif item_type == "character":
            favorite = Favorite_Character.query.filter_by(user_id=user_id,item_id=item_id).first()
            if favorite is None:
                raise APIException('Favorite character not found', status_code=404)
        else:
            raise APIException('Invalid item type', status_code=400)
        
        db.session.delete(favorite)
        db.session.commit()
        
    except APIException as e:
        return jsonify({"error": str(e.message)}), e.status_code
    user = jsonify(user.serialize())
    favorite = jsonify(favorite.serialize())
    msg = {
            "message": f"Favorite {item_type} deleted successfully",
            "user" : user.json,
            "item deleted" : favorite.json
        }
    return jsonify(msg), 200

@app.route('/user/favorites/all/<int:user_id>', methods=['DELETE'])
def delete_all_favorites(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User does not exist"}), 404
    favorite_planets = Favorite_Planet.query.filter_by(user_id=user_id).all()
    favorite_characters = Favorite_Character.query.filter_by(user_id=user_id).all()
    
    if not favorite_planets and not favorite_characters:
        return jsonify({"message": "No favorites found for the user"}), 404
    
    for favorite in favorite_planets:
        db.session.delete(favorite)
    for favorite in favorite_characters:
        db.session.delete(favorite)
    
    db.session.commit()
    user = jsonify(user.serialize())
    msg = {
            "message": "All favorites deleted successfully",
            "user" : user.json,
        }
    return jsonify(msg), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
