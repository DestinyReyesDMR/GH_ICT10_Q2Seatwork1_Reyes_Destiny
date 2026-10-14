from pyscript import document

def verify_candidate(event):
    club_members = [
        "Vita De Guzman", 
        "Franchesca Dela Rosa", 
        "MJ Madrelejos", 
        "Raver Estacio", 
        "Chalanie Lumbang", 
        "Santiago Valdez", 
        "Gurleen Kaur", 
        "Kenneth Concepcion", 
        "JJ Villante", 
        "Jia Hadjigapor", 
        "Miguel Jimenez"
    ]

    first_el = document.getElementById("first-name")
    last_el = document.getElementById("last-name")
    
    first_value = first_el.value.strip() if first_el else ""
    last_value = last_el.value.strip() if last_el else ""
    
    full_name = f"{first_value} {last_value}"

    is_member = full_name in club_members

    messages = [
        f"Sorry {full_name}, your name is not on the list awwh okay lang yan.",
        f"Congratulations {full_name}! You are now part of the Commarts club! YAY"
    ]
    

    result_text = messages[int(is_member)]


    result_area = document.getElementById("result-area")
    if result_area:
        result_area.innerText = result_text