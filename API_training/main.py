from API_training.get_address_info import NominatimAPI


if __name__ == '__main__':
    import asyncio
street: str = input("Enter street: ")
city: str = input("Enter city: ")
country: str = input("Enter country: ")
asyncio.run(NominatimAPI.search_address(formate="json", city=city, street=street, country=country))
