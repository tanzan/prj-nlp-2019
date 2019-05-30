import random
import pickle
from dataclasses import dataclass


@dataclass
class Document:
    __slots__ = ['id_', 'text', 'text_lem', 'label']
    
    id_: int
    text: str
    text_lem: str
    label: str
        
        
class Repository1551:
    
    def __init__(self, *docs: Document):
        self.docs = list(docs)
        
    def __iter__(self):
        for doc in self.docs:
            yield doc
            
    def __len__(self):
        return len(self.docs)
        
    def add(self, doc: Document):
        self.docs.append(doc)
        
    def extend(self, *docs: Document):
        self.docs.extend(list(docs))
        
    def shuffle(self):
        random.shuffle(self.docs)
        
    def __get_field_list(self, field):
        return [getattr(d, field) for d in self.docs]
        
    @property
    def labels(self):
        return self.__get_field_list('label')
    
    @property
    def texts(self):
        return self.__get_field_list('text')
    
    @property
    def lems(self):
        return self.__get_field_list('text_lem')

    def save(self, fname):
        with open(fname, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, fname):
        with open(fname, 'rb') as f:
            rep = pickle.load(f)
        return rep
