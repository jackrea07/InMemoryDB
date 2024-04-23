class InMemoryDB:
    main_db = dict()
    temp_db = dict()
    transaction = False
    
    def get(self, key):
        return self.main_db.get(key, None)
    
    def put(self, key, val):
        if self.transaction == False:
            raise Exception("Cannot PUT without an ongoing transaction")
        else:
            self.temp_db.update({key : val})

    def begin_transaction(self):
        self.transaction = True

    def commit(self):
        if self.transaction == False:
            raise Exception("Cannot COMMIT without an ongoing transaction")
        else:
            self.main_db = self.temp_db.copy()
            self.transaction = False

    def rollback(self):
        if self.transaction == False:
            raise Exception("Cannot ROLLBACK without an ongoing transaction")
        else:
            self.temp_db = self.main_db.copy()
            self.transaction = False


if __name__ == '__main__':
    db = InMemoryDB()
    
    db.begin_transaction()
    print("Transaction begins")

    db.put("A", 5)
    print("A = 5")

    print(db.get("A"))

    db.put("A", 6)
    print("A = 6")

    db.commit()
    print("committed")

    print(db.get("A"))

    print(db.get("B"))

    db.begin_transaction()

    db.put("B", 10)
    print(db.temp_db)
    print(db.main_db)

    db.rollback()

    print(db.get("B"))


