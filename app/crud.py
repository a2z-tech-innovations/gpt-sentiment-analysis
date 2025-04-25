from sqlalchemy.orm import Session
# import app.models as models
from app.models import SearchTerm, GeneratedContent, SentimentAnalysis
import app.schemas as schemas

def create_search_term(db: Session, term: str):
    db_search_term = SearchTerm(term=term)
    
    db.add(db_search_term)
    db.commit()
    db.refresh(db_search_term)
    
    return db_search_term
    
def create_generated_content(db: Session, content: str, search_term_id: int):
    db_generated_content = GeneratedContent(content=content, search_term_id=search_term_id)
    db.add(db_generated_content)
    db.commit()
    db.refresh(db_generated_content)
    
    return db_generated_content

def get_search_term(db: Session, term: str):
    return db.query(SearchTerm).filter(SearchTerm.term == term).first()
    
def create_sentiment_analysis(db: Session, readability: str, sentiment: str, search_term_id: int):
    db_sentiment_analysis = SentimentAnalysis(readability=readability, sentiment=sentiment, search_term_id=search_term_id)
    db.add(db_sentiment_analysis)
    db.commit()
    db.refresh(db_sentiment_analysis)
    
    return db_sentiment_analysis

def get_sentiment_analysis(db: Session, search_term_id: int):
    return db.query(SentimentAnalysis).filter(SentimentAnalysis.search_term_id == search_term_id).first()