from .models import Post, Country, Address, Client
from ariadne import convert_kwargs_to_snake_case

def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def listCountries_resolver(obj, info):
    try:
        countries = [country.to_dict() for country in Country.query.all()]
        payload = {
            "success": True,
            "countries": countries
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getCountry_resolver(obj, info, id):
    try:
        country = Country.query.get(id)
        payload = {
            "success": True,
            "country": country.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Country item matching {id} not found"]
        }
        
    return payload

@convert_kwargs_to_snake_case
def getAddress_resolver(obj, info, id):
    try:
        address = Address.query.get(id)
        country = Country.query.get(int(address.country_id))
        payload = {
            "success": True,
            "address": address.to_dict(),
            "country": country.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Address item matching {id} not found"]
        }
        
    return payload

@convert_kwargs_to_snake_case
def listAddresses_resolver(obj, info):
    try:
        addresses = [ address.to_dict() for address in Address.query.all()]
        payload = {
            "success": True,
            "addresses": addresses
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def listClients_resolver(obj, info):
    try:
        clients = [client.to_dict() for client in Client.query.all()]
        payload = {
            "success": True,
            "clients": clients
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getClient_resolver(obj, info, id):
    try:
        client = Client.query.get(id)
        payload = {
            "success": True,
            "client": client.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Client item matching {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def getClientsbyCountry_resolver(obj, info, country_id):
    try:
        clients = [client.to_dict() for client in Client.query.join(Address).filter(Address.country_id == country_id)]
        payload = {
            "success": True,
            "clients": clients
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload