from sqlalchemy import text

from app.db.session import engine


def main() -> None:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user")
        )
        database, user = result.one()

        print(f"Connected to database: {database}")
        print(f"Connected as user: {user}")


if __name__ == "__main__":
    main()