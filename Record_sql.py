import sqlite3

def record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras):
    connection = sqlite3.connect("entrainements.db")
    cursor = connection.cursor()
    new_record = (cursor.lastrowid, participant, d1, entrainement, serie, tps_rope, level, poids, gras)
    cursor.execute('INSERT INTO training VALUES(?,?,?,?,?,?,?,?,?)', new_record)
    connection.commit()
    connection.close()