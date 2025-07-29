import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/digital-insights-digital-insights-default/api/property-records-search'

mcp = FastMCP('property-records-search')

@mcp.tool()
def search_by_name(FirstName: Annotated[str, Field(description='')],
                   LastName: Annotated[str, Field(description='')],
                   State: Annotated[Union[str, None], Field(description='')] = None,
                   Page: Annotated[Union[int, float, None], Field(description='Default: 1')] = None) -> dict: 
    '''Search property records by name'''
    url = 'https://property-records-search.p.rapidapi.com/SearchPeople'
    headers = {'x-rapidapi-host': 'property-records-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'FirstName': FirstName,
        'LastName': LastName,
        'State': State,
        'Page': Page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
