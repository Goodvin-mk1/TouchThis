from pprint import pprint

from requests import Session


def krya():
    with Session() as session:
        response = session.get(
            url="http://localhost:8000/api/1/category/all",
            headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2NTkyNzA1OTF9.qGON6NQ4o-KIGNXZWPiJqE76Ik8x4A3ugwP9DrU0rKs"},
        )

        pprint(response.status_code)
        pprint(response.json())

krya()
