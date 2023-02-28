# mutations.py
from datetime import date
import re
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Post, Country, Address, Client


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        today = date.today()
        post = Post(
            title=title, description=description, created_at=today.strftime(
                "%b-%d-%Y")
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if post:
            post.title = title
            post.description = description
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def create_country_resolver(obj, info, name):
    try:
        country = Country(
            name=name, created_at=date.today().strftime("%b-%d-%Y"))
        db.session.add(country)
        db.session.commit()
        payload = {
            "success": True,
            "country": country.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_country_resolver(obj, info, id, name):
    try:
        country = Country.query.get(id)
        if country:
            country.name = name
        db.session.add(country)
        db.session.commit()
        payload = {
            "success": True,
            "country": country.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload
        
@convert_kwargs_to_snake_case
def delete_country_resolver(obj, info, id):
    try:
        country = Country.query.get(id)
        db.session.delete(country)
        db.session.commit()
        payload = {"success": True, "country": country.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def create_address_resolver(obj, info, country_id, city, state):
    try:
        address = Address(
            country_id=country_id,
            city=city,
            state=state,
            created_at=date.today().strftime("%b-%d-%Y")
        )
        db.session.add(address)
        db.session.commit()
        payload = {
            "success": True,
            "address": address.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload
        
@convert_kwargs_to_snake_case
def update_address_resolver(obj, info, id, country_id, city, state):
    try:
        address = Address.query.get(id)
        if address:
            address.country_id = country_id
            address.city = city
            address.state = state
        db.session.add(address)
        db.session.commit()
        payload = {
            "success": True,
            "address": address.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload
        
@convert_kwargs_to_snake_case
def delete_address_resolver(obj, info, id):
    try:
        address = Address.query.get(id)
        db.session.delete(address)
        db.session.commit()
        payload = {"success": True, "address": address.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def create_client_resolver(obj, info, name, last_name, email, phone, address_id):
    try:
        client = Client(
            name=name,
            last_name=last_name,
            email=email,
            phone=phone,
            address_id=address_id,
            created_at=date.today().strftime("%b-%d-%Y")
        )
        db.session.add(client)
        db.session.commit()
        payload = {
            "success": True,
            "client": client.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_client_resolver(obj, info, id, name, last_name, email, phone, address_id):
    try:
        client = Client.query.get(id)
        if client:
            client.name = name
            client.last_name = last_name
            client.email = email
            client.phone = phone
            client.address_id = address_id
        db.session.add(client)
        db.session.commit()
        payload = {
            "success": True,
            "client": client.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_client_resolver(obj, info, id):
    try:
        client = Client.query.get(id)
        db.session.delete(client)
        db.session.commit()
        payload = {"success": True, "client": client.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload