from geopy.geocoders import Nominatim
from geopy.distance import distance


def calc_dist(input_city, input_state):

    parceiros = [
      ['TRÍADE', 'manaus, amazonas', -3.1316333, -59.9825041],
      ['XAVIER PAIM', 'salvador, bahia', -12.9822499, -38.4812772],
      ['CONTAS energy', 'feira de santana, bahia', -12.2578934, -38.9598047],
      ['SUNLINKS REPRESENTACOES_01', 'fortaleza, ceara, brasil', -3.7304512, -38.5217989],
      ['SUNLINKS REPRESENTACOES_02', 'teresina, piaui, brasil', -5.0874608, -42.8049571],
      ['SUNLINKS REPRESENTACOES_03', 'belem, para, brasil', -1.45056, -48.4682453],
      ['SUNLINKS REPRESENTACOES_04', 'manaus, amazonas, brasil', -3.1316333, -59.9825041],
      ['ADORNO ENERGIA LTDA_01', 'goiania, goias, brasil', -16.680882, -49.2532691],
      ['ADORNO ENERGIA LTDA_02', 'distrito federal, brasil', -15.7754462, -47.7970891],
      ['Diego Garcia_01', 'uberlandia, minas gerais, brasil', -18.9188041, -48.2767837],
      ['Diego Garcia_02', 'cuiaba, mato grosso, brasil', -15.5986686, -56.0991301],
      ['BIASI TECH', 'uberlandia, minas gerais, brasil', -18.9188041, -48.2767837],
      ['RDL SOLUÇÕES_01', 'joao pessoa, paraiba, brasil', -7.1215981, -34.882028],
      ['RDL SOLUÇÕES_02', 'maceio, alagoas, brasil', -9.6476843, -35.7339264],
      ['RDL SOLUÇÕES_03', 'palmas, tocantins, brasil', -10.1837852, -48.3336423],
      ['RDL SOLUÇÕES_04', 'recife, pernambuco, brasil', -8.0584933, -34.8848193],
      ['RDL SOLUÇÕES_05', 'natal, rio grande do norte, brasil', -5.805398, -35.2080905],
      ['CIMUS Energia_01', 'Curitiba, parana, brasil', -25.4295963, -49.2712724],
      ['CIMUS Energia_02', 'São José do Rio Preto, sao paulo, brasil', -20.8125851, -49.3804212],
      ['ENERGY PARTNERS SOLUCOES@Manoela Rech', 'vitoria, espirito santo, brasil', -20.3200917, -40.3376682],
      ['ENERGY PARTNERS SOLUCOES@Felipe Paim', 'porto alegre, rio grande do sul, brasil', -30.0324999, -51.2303767],
      ['ITA CAPITAL', 'rio de janeiro, rio de janeiro, brasil', -22.9110137, -43.2093727],
      ['FORTEM ENERGIA', 'campo belo, rio grande do sul, brasil', -29.9298237, -51.046010298562535],
      ['OMNI ENERGY_01', 'florianopolis, santa catarina, brasil', -27.5973002, -48.5496098],
      ['OMNI ENERGY_02', 'curitiba, parana, brasil', -25.4295963, -49.2712724],
      ['OMNI ENERGY_03', 'cuiaba, mato grosso, brasil', -15.5986686, -56.0991301],
      ['TIC SALES', 'chapeco,santa catarina, brasil', -27.0922364, -52.6166878],
      ['ALVO K', 'campinas, sao paulo, brasil', -22.9056391, -47.059564],
      ['FIX SOLUCOES', 'sao jose dos campos, sao paulo, brasil', -23.1867782, -45.8854538],
      ['GMX CAPITAL ASSESSORIA', 'sao paulo, sao paulo, brasil', -23.5506507, -46.6333824],
      ['ELOHIM ENERGIA', 'sorocaba, sao paulo, brasil', -23.5003451, -47.4582864]
    ]

    geolocator = Nominatim(user_agent="myapp", timeout=10)
    target_city = f'{input_city}, {input_state}, brasil'
    target_location = geolocator.geocode(target_city)

    result = []
    for parceiro, local, lat, lon in parceiros:
        # parceiro
        latitude = lat
        longitude = lon

        # lead
        target_latitude = target_location.latitude
        target_longitude = target_location.longitude

        distance_km = distance((latitude, longitude),
                               (target_latitude, target_longitude)).km

        result.append([parceiro, local, distance_km])

    result.sort(key=lambda x: int(x[2]))
    return result


if __name__ == "__main__":
    calc_dist()

