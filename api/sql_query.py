from config import SqlConnection, logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def question_1():
    conn = SqlConnection(logging)
    mydb = conn.connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        """
            SELECT priority_level, target_name,entity_id, movement_distance_km
            FROM `targets`
            WHERE priority_level = 1 or priority_level = 2
            and movement_distance_km > 5
        """
    )

    myresult = mycursor.fetchall()
    
    result = []
    
    for x in myresult:
        result.append(x)
    return result


question_1()


def question_2():
    conn = SqlConnection(logging)
    mydb = conn.connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        """
            SELECT signal_type, COUNT(signal_type)as counting
            FROM `intel_signals` 
            GROUP by signal_type 
            ORDER by counting DESC
        """
    )

    myresult = mycursor.fetchall()

    result = []
    
    for x in myresult:
        result.append(x)
    return result


question_2()


def question_3():
    conn = SqlConnection(logging)
    mydb = conn.connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        """
            SELECT entity_id, COUNT(reported_lat) as for_lat, COUNT(reported_lon) as for_lon
            FROM `intel_signals` 
            WHERE entity_id LIKE "%UNKNOWN%" or priority_level = 99
            GROUP by entity_id DESC LIMIT 3

        """
    )

    myresult = mycursor.fetchall()

    result = []
    
    for x in myresult:
        result.append(x)
    return result


question_3()


def question_4():
    conn = SqlConnection(logging)
    mydb = conn.connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        """
            WITH morning_to_evning AS (
            SELECT *
            FROM `intel_signals`
            WHERE timestamp BETWEEN "2026-03-15 08:00.00" and "2026-04-15 20:00.00"
            and distance_from_last = 0
            ),

            evning_to_morning AS (
                SELECT *
            FROM `intel_signals`
            WHERE timestamp BETWEEN "2026-03-15 20:00.00" and "2026-04-15 08:00.00"
            and distance_from_last > 10
            )

            SELECT * FROM morning_to_evning 
            UNION ALL
            SELECT * from evning_to_morning 

        """
    )

    myresult = mycursor.fetchall()

    result = []
    
    for x in myresult:
        result.append(x)
    return result


question_4()


def question_5():
    conn = SqlConnection(logging)
    mydb = conn.connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        """
            SELECT `reported_lat`,`reported_lon`
            FROM `intel_signals`
        """
    )

    myresult = mycursor.fetchall()

    result = []
    
    for x in myresult:
        result.append(x)
    return result


question_5()
