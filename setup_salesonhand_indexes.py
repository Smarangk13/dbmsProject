import sqlite3

def setup_salesonhand_indexes():
    conn = sqlite3.connect("CS579.db")

    cursor = conn.cursor()

    indexes = []

    # b tree / ordered index to optimize price range queries
    priceIndex = 'CREATE INDEX price_index ON Sales(SalePrice)'

    indexes.append(priceIndex)

    for index in indexes:
        cursor.execute(index)

    conn.commit()
    conn.close()
