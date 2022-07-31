from requests import Session


def krya():
    with Session() as session:
        response = session.delete(
            url="http://localhost:8000/api/1/invoice/del",
            headers={"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2NTkyNzA1OTF9.qGON6NQ4o-KIGNXZWPiJqE76Ik8x4A3ugwP9DrU0rKs"},
            params={"invoice_id": 3}
        )

        print(response.status_code)
        print(response.json())

krya()
