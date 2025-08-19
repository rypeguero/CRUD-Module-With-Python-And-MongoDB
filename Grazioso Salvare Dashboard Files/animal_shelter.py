from pymongo import MongoClient 
from pymongo.errors import PyMongoError 
 
class AnimalShelter(object): 
    """ 
    CRUD operations for Animal collection in MongoDB. 
    """ 
     
    def __init__(self,  
                 username='aacuser',  
                 password='mypassword1', 
                 host='nv-desktop-services.apporto.com', 
                 port=33900, 
                 db='AAC', 
                 collection='animals'): 
        """ 
        Initialize MongoDB connection. 
        """ 
        try: 
            self.client = MongoClient( 
                f'mongodb://{username}:{password}@{host}:{port}/?authSource=admin' 
            ) 
            self.database = self.client[db] 
            self.collection = self.database[collection] 
        except PyMongoError as e: 
            print("Error connecting to MongoDB:", e) 
            raise 
 
    def create(self, data): 
        """ 
        Inserts a document into the collection. 
        :param data: Dictionary of key/value pairs for MongoDB document. 
        :return: True if successful, False otherwise. 
        """ 
        if data: 
            try: 
                result = self.collection.insert_one(data) 
                return result.acknowledged 
            except PyMongoError as e: 
                print("Create Error:", e) 
                return False 
        else: 
            print("No data provided for insertion.") 
            return False 
 
    def read(self, query): 
        """ 
        Queries for documents matching the query. 
        :param query: Dictionary of key/value pairs to search for. 
        :return: List of documents found, or empty list if none. 
        """ 
        try: 
            results = list(self.collection.find(query)) 
            return results 
        except PyMongoError as e: 
            print("Read Error:", e) 
            return [] 
 
    def update(self, query, new_data): 
        """ 
        Updates documents matching a query. 
        :param query: Dictionary to find the document(s) to update. 
        :param new_data: Dictionary with the fields to update. 
        :return: The number of documents modified as an integer. 
        """ 
        if query and new_data: 
            try: 
                result = self.collection.update_many(query, {"$set": new_data}) 
                return result.modified_count 
            except PyMongoError as e: 
                print("Update Error:", e) 
                return 0 
        else: 
            print("Query and new_data must be provided for update.") 
            return 0 
             
    def delete(self, query): 
        """ 
        Deletes documents matching a query. 
        :param query: Dictionary to find the document(s) to delete. 
        :return: The number of documents deleted as an integer. 
        """ 
        if query: 
            try: 
                result = self.collection.delete_many(query) 
                return result.deleted_count 
            except PyMongoError as e: 
                print("Delete Error:", e) 
                return 0 
        else: 
            print("A query must be provided to delete documents.") 
            return 0 