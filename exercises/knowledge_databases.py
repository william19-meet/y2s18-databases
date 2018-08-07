from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_subject(subject, wiki_name, rating):
	Knowledge_object = Knowledge(
		subject = subject,
		wiki_name = wiki_name,
		rating = rating,)
	session.add(Knowledge_object)
	session.commit()

def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return knowledge


def query_article_by_topic(their_name):
	knowledge = session.query(Knowledge).filter_by(subject=their_name).first()
	return knowledge

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass


add_subject("cyber", "cyber", 10)
#print(query_all_articles())
print(query_article_by_topic("cyber"))