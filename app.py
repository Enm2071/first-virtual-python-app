import imp
from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listPosts_resolver, getPost_resolver, listCountries_resolver, getCountry_resolver, getAddress_resolver, getClient_resolver, listAddresses_resolver, listClients_resolver, getClientsbyCountry_resolver
from api.mutations import create_client_resolver, create_post_resolver, update_post_resolver, delete_post_resolver, create_country_resolver, update_country_resolver, delete_country_resolver, create_address_resolver, update_address_resolver, delete_address_resolver, update_client_resolver, delete_client_resolver

query = ObjectType("Query")

query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)
query.set_field("listCountries", listCountries_resolver)
query.set_field("getCountry", getCountry_resolver)
query.set_field("listAddresses", listAddresses_resolver)
query.set_field("getAddress", getAddress_resolver)
query.set_field("listClients", listClients_resolver)
query.set_field("getClient", getClient_resolver)
query.set_field("getClientsByCountry", getClientsbyCountry_resolver)

mutation = ObjectType("Mutation")

mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)
mutation.set_field("createCountry", create_country_resolver)
mutation.set_field("updateCountry", update_country_resolver)
mutation.set_field("deleteCountry", delete_country_resolver)
mutation.set_field("createAddress", create_address_resolver)
mutation.set_field("updateAddress", update_address_resolver)
mutation.set_field("deleteAddress", delete_address_resolver)
mutation.set_field("createClient", create_client_resolver)
mutation.set_field("updateClient", update_client_resolver)
mutation.set_field("deleteClient", delete_client_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


print("[INFO] Starting API server...")
