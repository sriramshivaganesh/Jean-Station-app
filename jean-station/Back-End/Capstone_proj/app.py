from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

client = MongoClient("mongodb://db:27017/")
db = client["total_items"]
men_products_collection = db["mens_wear"]
women_products_collection = db["womens_wear"]

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Product name is required")
parser.add_argument("size", type=str, required=True, help="size is required")
parser.add_argument("color", type=str, required=True, help="color is required")
parser.add_argument("price", type=float, required=True, help="Price is required")
parser.add_argument("Id", type=int, required=True, help="Product name is required")
parser.add_argument("image_url", type=str, required=True, help="image is required")


class MenProducts(Resource):
    def get(self, product_id=None):
        if product_id:
            detail = men_products_collection.find_one({"_id": ObjectId(product_id)})
            if detail:
                detail['_id'] = str(detail['_id'])
                return detail, 200
            return {"message": "product not found!"}
        else:
            all_men_products = list(men_products_collection.find())
            for product in all_men_products:
                product['_id'] = str(product['_id'])
            return all_men_products, 200

    def post(self):
        args = parser.parse_args()
        product_exist = men_products_collection.find_one({"Id": args['Id']})

        if product_exist:
            return {"message": "Product already exists"}, 409
        else:
            data = {
                "name": args["name"],
                "size": args["size"],
                "color": args["color"],
                "price": args["price"],
                "Id": args["Id"],
                "image_url": args["image_url"]
            }
            men_products_collection.insert_one(data)
            return "Men's product added successfully", 201


class MenProduct(Resource):
    def put(self, product_id):
        args = parser.parse_args()
        data = {
            "name": args["name"],
            "size": args["size"],
            "color": args["color"],
            "price": args["price"],
            "Id": args["Id"],
            "image_url": args["image_url"]
        }
        men_products_collection.update_one({"_id": ObjectId(product_id)}, {"$set": data})
        return "Men's product updated successfully"

    def delete(self, product_id):
        men_products_collection.delete_one({"_id": ObjectId(product_id)})
        return "Men's product deleted successfully", 204


class WomenProducts(Resource):
    def get(self, product_id=None):
        if product_id:
            detail = women_products_collection.find_one({"_id": ObjectId(product_id)})
            if detail:
                detail['_id'] = str(detail['_id'])
                return detail, 200
            return {"message": "product not found!"}
        else:
            all_women_products = list(women_products_collection.find())
            for product in all_women_products:
                product['_id'] = str(product['_id'])
            return all_women_products, 200

    def post(self):
        args = parser.parse_args()
        product_exist = women_products_collection.find_one({"Id": args['Id']})

        if product_exist:
            return {"message": "Product already exists"}, 409
        else:
            data = {
                "name": args["name"],
                "size": args["size"],
                "color": args["color"],
                "price": args["price"],
                "Id": args["Id"],
                "image_url": args["image_url"]
            }
            women_products_collection.insert_one(data)
            return "Women's product added successfully", 201


class WomenProduct(Resource):
    def put(self, product_id):
        args = parser.parse_args()
        data = {
            "name": args["name"],
            "size": args["size"],
            "color": args["color"],
            "price": args["price"],
            "id": args["id"],
            "image_url": args["image_url"]
        }
        women_products_collection.update_one({"_id": ObjectId(product_id)}, {"$set": data})
        return "Women's product updated successfully"

    def delete(self, product_id):
        women_products_collection.delete_one({"_id": ObjectId(product_id)})
        return "Women's product deleted successfully", 204


api.add_resource(MenProducts, "/men-products", "/men-products/<string:product_id>")
api.add_resource(WomenProducts, "/women-products",  "/women-products/<string:product_id>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
