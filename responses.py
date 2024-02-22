# Funktsioon, mis hakkab kasutajate sõnumeid käsitlema
def handle_response(message) -> str:
    # Teeme iga sõnumi väiketäheliseks, et endal oleks kergem
    p_message = message.lower()

    # Kui sõnum oli !abi, saadame kasutajale vastuse
    if p_message == "abi":
        return "Vastus, mille bot discordi saadab"
