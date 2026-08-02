from database.database import get_connection


class HistoryService:

    @staticmethod
    def save(expression: str, result):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO history(expression,result)
            VALUES(?,?)
            """,
            (expression, str(result)),
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():

        conn = get_connection()

        rows = conn.execute(
            """
            SELECT expression,result,timestamp
            FROM history
            ORDER BY id DESC
            """
        ).fetchall()

        conn.close()

        return rows

    @staticmethod
    def clear():

        conn = get_connection()

        conn.execute("DELETE FROM history")

        conn.commit()

        conn.close()