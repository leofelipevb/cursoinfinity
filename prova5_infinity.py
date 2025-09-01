day = int(input("Digite o dia de nascimento (1-31): "))
month = input("Digite o mês de nascimento (nome ou número): ").strip().lower()

if month in ["1", "janeiro"]:
    astro_sign = "Capricórnio" if day < 20 else "Aquário"
elif month in ["2", "fevereiro"]:
    astro_sign = "Aquário" if day < 19 else "Peixes"
elif month in ["3", "março", "marco"]:
    astro_sign = "Peixes" if day < 21 else "Áries"
elif month in ["4", "abril"]:
    astro_sign = "Áries" if day < 20 else "Touro"
elif month in ["5", "maio"]:
    astro_sign = "Touro" if day < 21 else "Gêmeos"
elif month in ["6", "junho"]:
    astro_sign = "Gêmeos" if day < 21 else "Câncer"
elif month in ["7", "julho"]:
    astro_sign = "Câncer" if day < 23 else "Leão"
elif month in ["8", "agosto"]:
    astro_sign = "Leão" if day < 23 else "Virgem"
elif month in ["9", "setembro"]:
    astro_sign = "Virgem" if day < 23 else "Libra"
elif month in ["10", "outubro"]:
    astro_sign = "Libra" if day < 23 else "Escorpião"
elif month in ["11", "novembro"]:
    astro_sign = "Escorpião" if day < 22 else "Sagitário"
elif month in ["12", "dezembro"]:
    astro_sign = "Sagitário" if day < 22 else "Capricórnio"
else:
    astro_sign = None

if astro_sign:
    print(f"Seu signo é: {astro_sign}")
else:
    print("Entrada inválida. Verifique o dia ou mês.")
