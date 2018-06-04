from behave import given
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

@given('an empty card broker database')
def clear_card_broker_db(context):
    """
    truncate existing table data for clean run
    """

    engine = create_engine(context.urls.card_broker_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()

    session.execute('TRUNCATE TABLE gamestate')
    session.execute('TRUNCATE TABLE playerstate')

    session.commit()
    session.close()
