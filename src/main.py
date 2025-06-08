import pymongo
import json

def connect_to_mongo(uri, db_name):
    client = pymongo.MongoClient(uri)
    db = client[db_name]
    return db

def insert_documents(db, collection_name, documents):
    collection = db[collection_name]
    result = collection.insert_many(documents)
    return result.inserted_ids

def find_documents(db, collection_name, query):
    collection = db[collection_name]
    documents = collection.find(query)
    return list(documents)

def update_documents(db, collection_name, query, update):
    collection = db[collection_name]
    result = collection.update_many(query, update)
    return result.modified_count

def delete_documents(db, collection_name, query):
    collection = db[collection_name]
    result = collection.delete_many(query)
    return result.deleted_count

def main():
    uri = "mongodb://localhost:27017/"
    db_name = "arxiv"
    collection_name = "articles"

    # Connect to MongoDB
    db = connect_to_mongo(uri, db_name)

    # Load data from JSON file
    with open('src/data/uarxiv-rol1-rol2.json') as f:
        documents = json.load(f)

    # Insert documents into the collection
    inserted_ids = insert_documents(db, collection_name, documents)
    print(f"Inserted document IDs: {inserted_ids}")

    # Example query to find documents
    query = {"title": {"$regex": "machine learning", "$options": "i"}}
    found_documents = find_documents(db, collection_name, query)
    print(f"Found documents: {found_documents}")

    # Example update operation
    update_query = {"title": {"$regex": "machine learning", "$options": "i"}}
    update = {"$set": {"updated": True}}
    modified_count = update_documents(db, collection_name, update_query, update)
    print(f"Modified document count: {modified_count}")

    # Example delete operation
    delete_query = {"title": {"$regex": "old research", "$options": "i"}}
    deleted_count = delete_documents(db, collection_name, delete_query)
    print(f"Deleted document count: {deleted_count}")

if __name__ == "__main__":
    main()