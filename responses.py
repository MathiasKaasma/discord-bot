import aiohttp  # vajalik hilisemaks


# Funktsioon, mis hakkab kasutajate sõnumeid käsitlema
async def handle_response(message) -> str:
    # Teeme iga sõnumi väiketäheliseks, et endal oleks kergem
    message = message.lower()

    # Kui sõnum oli !abi, saadame kasutajale vastuse
    if message == "abi":
        return "Vastus, mille bot discordi saadab"
