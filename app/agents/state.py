
from typing import List
import operator
from typing import Annotated
from typing import TypedDict

class AgentState(TypedDict):
    messages: Annotated[List[dict], operator.add]
    current_query: str
    documents: List[str]
    plan: List[str]
    status: str
    final_answer: str
    
     
