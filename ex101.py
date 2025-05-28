def vote(year):
    from datetime import date
    current_year = date.today().year
    person_year_born = current_year - year
    if 18 <= person_year_born < 65 :
        return f"Com {person_year_born} anos: VOTO OBRIGATORIO"
    elif 16 <= person_year_born < 18 or person_year_born >= 65:
        return f"Com {person_year_born} anos: VOTO OPCIONAL"
    else:
        return f"Com {person_year_born} anos: NAO VOTA"

age = int(input("Digite seu ano de nascimento: "))
print(vote(age))