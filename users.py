import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы,
    если их еще нет и возвращает объект сессии
    """
    engine = sa.create_engine(DB_PATH)  # создаем соединение к базе данных
    Base.metadata.create_all(engine)  # создаем описанные таблицы
    session = sessionmaker(engine)  # создаем фабрику сессию
    return session()  # возвращаем сессию


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Ввод данных нового пользователя")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    gender = input("Введите пол (Male/Female): ")
    email = input("Введите адрес электронной почты: ")
    birthdate = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
    height = float(input("Введите рост, м: "))

    # создаем нового пользователя
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    # возвращаем созданного пользователя
    return user


def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Данные сохранены!")


if __name__ == "__main__":
    main()
