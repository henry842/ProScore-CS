# ------------------------- 
# Importações e app
# -------------------------
from flask import Flask, request, render_template_string

import pandas as pd

app = Flask(__name__)

# -------------------------
# Dados de todos os times
# -------------------------

# Para simplificação, usaremos os mesmos dados de exemplo do seu código original
# Só atualizei os nomes dos times para o dicionário final

time_data = {
    "Vitality": {
        "map_stats": pd.DataFrame({
            "Mapa": ["Dust II", "Inferno", "Train", "Nuke", "Mirage", "Overpass", "Ancient"],
            "Taxa de Vitória (%)": [86, 82, 79, 76, 65, 50, 0],
            "Últimos 5 Mapas": ["V V V V L", "V L V V V", "L V L V L", "V L L V V", "V L L V V", "V L V", "FB FB FB FB FB"],
            "Partidas Jogadas": [21, 28, 13, 21, 26, 3, 0],
            "Vitórias CT (E)": [15, 15, 6, 10, 0, 1, 0],
            "Vitórias T (B)": [5, 5, 4, 6, 11, 2, 0],
            "CT % de Êxito": [57, 62, 65, 61, 58, 33, 0],
            "T % de Êxito": [64, 62, 48, 50, 49, 67, 0]
        }),
        "general_stats": {
            "torneios": {"contagem": 10, "taxa_ganho": 30},
            "partidas": {"contagem": 39, "taxa_ganho": 77},
            "mapas": {"contagem": 93, "taxa_ganho": 73},
            "rodadas": {"contagem": 2068, "taxa_ganho": 57}
        },
        "round_stats": {
            "5v4": {"valor": 0.55, "taxa": 75},
            "4v5": {"valor": 0.44, "taxa": 34},
            "bombas_plantadas": {"valor": 0.30, "taxa": 80},
            "bombas_desarmadas": {"valor": 0.79, "taxa": 100},
            "tempo_extra": {"valor": 0.06, "taxa": 53},
            "pistol": {"valor": 0.09, "taxa": 52},
            "eco": {"valor": 0.04, "taxa": 8},
            "force": {"valor": 0.21, "taxa": 48},
            "full_buy": {"valor": 0.67, "taxa": 63}
        }
    },

    "SPIRIT": {
        "map_stats": pd.DataFrame({
            "Mapa": ["Overpass", "Train", "Dust II", "Mirage", "Ancient", "Nuke", "Inferno"],
            "Taxa de Vitória (%)": [100, 83, 81, 71, 69, 63, 0],
            "Últimos 5 Mapas": ["V V ", "V V L V V", "L V V V L", "L V L V V", "V V V V L ", "L V V L L", "FB FB FB FB FB"],
            "Partidas Jogadas": [2, 5, 20, 21, 16, 18, 0],
            "Vitórias CT (E)": [1, 0, 14, 3, 6, 10, 0],
            "Vitórias T (B)": [1, 5, 6, 4, 2, 3, 0],
            "CT % de Êxito": [75, 57, 57, 61, 58, 56, 0],
            "T % de Êxito": [73, 58, 66, 51, 49, 50, 0]
        }),
        "general_stats": {
            "torneios": {"contagem": 10, "taxa_ganho": 30},
            "partidas": {"contagem": 39, "taxa_ganho": 77},
            "mapas": {"contagem": 93, "taxa_ganho": 73},
            "rodadas": {"contagem": 2068, "taxa_ganho": 57}
        },
        "round_stats": {
            "5v4": {"valor": 0.55, "taxa": 75},
            "4v5": {"valor": 0.44, "taxa": 34},
            "bombas_plantadas": {"valor": 0.30, "taxa": 80},
            "bombas_desarmadas": {"valor": 0.79, "taxa": 100},
            "tempo_extra": {"valor": 0.06, "taxa": 53},
            "pistol": {"valor": 0.09, "taxa": 52},
            "eco": {"valor": 0.04, "taxa": 8},
            "force": {"valor": 0.21, "taxa": 48},
            "full_buy": {"valor": 0.67, "taxa": 63}
        }
    },

    "THE_MONGOLZ": {
        "map_stats": pd.DataFrame({
            "Mapa": ["Overpass", "Mirage", "Nuke", "Dust II", "Ancient", "Inferno", "Train"],
            "Taxa de Vitória (%)": [100, 74, 64, 61, 60, 53, 0],
            "Últimos 5 Mapas": ["V - - - -", "V V L V V", "V V V V L", "V V L L V", "V L L V V", "L L V V L", "FB FB FB FB FB"],
            "Partidas Jogadas": [1, 25, 14, 17, 19, 18, 0],
            "Vitórias CT (E)": [0, 20, 0, 1, 13, 4, 0],
            "Vitórias T (B)": [1, 5, 14, 16, 6, 14, 0],
            "CT % de Êxito": [58, 57, 60, 50, 57, 54, 0],
            "T % de Êxito": [75, 53, 47, 51, 49, 51, 0]
        }),
        "general_stats": {
            "torneios": {"contagem": 11, "taxa_ganho": 9},
            "partidas": {"contagem": 49, "taxa_ganho": 63},
            "mapas": {"contagem": 111, "taxa_ganho": 59},
            "rodadas": {"contagem": 2401, "taxa_ganho": 52}
        },
        "round_stats": {
            "rodadas": {"valor": 1.0, "taxa": 52},
            "5v4": {"valor": 0.50, "taxa": 74},
            "4v5": {"valor": 0.49, "taxa": 31},
            "bombas_plantadas": {"valor": 0.29, "taxa": 78},
            "bombas_desarmadas": {"valor": 0.77, "taxa": 100},
            "tempo_extra": {"valor": 0.04, "taxa": 53},
            "pistol": {"valor": 0.09, "taxa": 46},
            "eco": {"valor": 0.06, "taxa": 4},
            "force": {"valor": 0.21, "taxa": 45},
            "full_buy": {"valor": 0.64, "taxa": 60}
        }
    },

    "MOUZ": {
        "map_stats": pd.DataFrame({
            "Mapa": ["Train", "Nuke", "Mirage", "Ancient", "Dust II", "Inferno", "Overpass"],
            "Taxa de Vitória (%)": [75, 68, 61, 60, 50, 46, 33],
            "Últimos 5 Mapas": ["L V V V V", "L V L V L", "V V L L L", "FB V L V L", "FB FB FB FB FB", "L V V L L", "L V L - -"],
            "Partidas Jogadas": [10, 23, 28, 15, 16, 16, 3],
            "Vitórias CT (E)": [3, 17, 20, 1, 0, 5, 0],
            "Vitórias T (B)": [6, 6, 6, 14, 16, 11, 3],
            "CT % de Êxito": [59, 60, 60, 54, 43, 51, 32],
            "T % de Êxito": [50, 46, 47, 49, 58, 48, 42]
        }),
        "general_stats": {
            "torneios": {"contagem": 12, "taxa_ganho": 0},
            "partidas": {"contagem": 49, "taxa_ganho": 65},
            "mapas": {"contagem": 120, "taxa_ganho": 58},
            "rodadas": {"contagem": 2628, "taxa_ganho": 51}
        },
        "round_stats": {
            "rodadas": {"valor": 1.0, "taxa": 51},
            "5v4": {"valor": 0.50, "taxa": 73},
            "4v5": {"valor": 0.50, "taxa": 30},
            "bombas_plantadas": {"valor": 0.26, "taxa": 79},
            "bombas_desarmadas": {"valor": 0.53, "taxa": 100},
            "tempo_extra": {"valor": 0.05, "taxa": 54},
            "pistol": {"valor": 0.09, "taxa": 56},
            "eco": {"valor": 0.05, "taxa": 3},
            "force": {"valor": 0.21, "taxa": 38},
            "full_buy": {"valor": 0.65, "taxa": 59}
        }
    },

    "FURIA": {
        "map_stats": pd.DataFrame({
            "Mapa": ["Dust II", "Train", "Inferno", "Nuke", "Mirage", "Overpass", "Ancient"],
            "Taxa de Vitória (%)": [57, 56, 55, 55, 50, 0, 0],
            "Últimos 5 Mapas": ["V V V L L", "V V L L L", "L V V V L", "FB V V L V", "V V V V L", "- - - - -", "FB FB FB FB FB"],
            "Partidas Jogadas": [20, 15, 19, 10, 20, 0, 0],
            "Vitórias CT (E)": [9, 10, 2, 2, 3, 0, 0],
            "Vitórias T (B)": [6, 3, 10, 8, 6, 0, 0],
            "CT % de Êxito": [50, 55, 51, 54, 50, 0, 0],
            "T % de Êxito": [56, 54, 56, 48, 47, 0, 0]
        }),
        "general_stats": {
            "torneios": {"contagem": 14, "taxa_ganho": 0},
            "partidas": {"contagem": 44, "taxa_ganho": 52},
            "mapas": {"contagem": 101, "taxa_ganho": 52},
            "rodadas": {"contagem": 2162, "taxa_ganho": 52}
        },
        "round_stats": {
            "rodadas": {"valor": 1.0, "taxa": 52},
            "5v4": {"valor": 0.53, "taxa": 73},
            "4v5": {"valor": 0.46, "taxa": 29},
            "bombas_plantadas": {"valor": 0.30, "taxa": 79},
            "bombas_desarmadas": {"valor": 0.55, "taxa": 100},
            "tempo_extra": {"valor": 0.05, "taxa": 44},
            "pistol": {"valor": 0.09, "taxa": 57},
            "eco": {"valor": 0.04, "taxa": 5},
            "force": {"valor": 0.24, "taxa": 47},
            "full_buy": {"valor": 0.64, "taxa": 57}
        }
    },



"TNL": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Ancient", "Train", "Mirage", "Dust II", "Nuke", "Inferno", "Overpass"],
        "Taxa de Vitória (%)": [76, 64, 63, 62, 57, 0, 0],
        "Últimos 5 Mapas": ["V V L V V", "L FB V L V", "L L V V L", "V V L V V", "V L L V L", "FB FB FB FB", "L L FB"],
        "Partidas Jogadas": [42, 25, 30, 34, 42, 0, 2],
        "Vitórias CT (E)": [23, 6, 8, 6, 5, 0, 0],
        "Vitórias T (B)": [19, 16, 22, 18, 23, 0, 0],
        "CT % de Êxito": [52, 51, 58, 53, 54, 0, 0],
        "T % de Êxito": [59, 50, 55, 56, 49, 0, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 18, "taxa_ganho": 17},
        "partidas": {"contagem": 65, "taxa_ganho": 69},
        "mapas": {"contagem": 162, "taxa_ganho": 61},
        "rodadas": {"contagem": 3439, "taxa_ganho": 54}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 54},
        "5v4": {"valor": 0.51, "taxa": 75},
        "4v5": {"valor": 0.49, "taxa": 32},
        "bombas_plantadas": {"valor": 0.30, "taxa": 78},
        "bombas_desarmadas": {"valor": 0.66, "taxa": 100},
        "tempo_extra": {"valor": 0.04, "taxa": 60},
        "pistol": {"valor": 0.09, "taxa": 58},
        "eco": {"valor": 0.05, "taxa": 7},
        "force": {"valor": 0.23, "taxa": 44},
        "full_buy": {"valor": 0.63, "taxa": 61}
    }
},

"IMPERIAL": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Dust II", "Overpass", "Nuke", "Mirage", "Inferno", "Train", "Ancient"],
        "Taxa de Vitória (%)": [67, 67, 67, 65, 56, 50, 0],
        "Últimos 5 Mapas": ["V V V V L", "V L V ", "L L V L L", "V V L V L", "V V L V V", "V L L V V", "FB FB FB FB"],
        "Partidas Jogadas": [24, 3, 21, 17, 18, 8, 0],
        "Vitórias CT (E)": [12, 2, 2, 2, 4, 1, 0],
        "Vitórias T (B)": [12, 1, 12, 11, 6, 7, 0],
        "CT % de Êxito": [53, 59, 62, 47, 49, 56, 0],
        "T % de Êxito": [56, 58, 45, 61, 54, 47, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 13, "taxa_ganho": 23},
        "partidas": {"contagem": 37, "taxa_ganho": 68},
        "mapas": {"contagem": 85, "taxa_ganho": 61},
        "rodadas": {"contagem": 1768, "taxa_ganho": 54}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 53},
        "5v4": {"valor": 0.50, "taxa": 75},
        "4v5": {"valor": 0.49, "taxa": 33},
        "bombas_plantadas": {"valor": 0.28, "taxa": 80},
        "bombas_desarmadas": {"valor": 0.52, "taxa": 100},
        "tempo_extra": {"valor": 0.03, "taxa": 51},
        "pistol": {"valor": 0.09, "taxa": 54},
        "eco": {"valor": 0.06, "taxa": 9},
        "force": {"valor": 0.22, "taxa": 49},
        "full_buy": {"valor": 0.63, "taxa": 59}
    }
},

"FaZe_Clan": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Ancient", "Dust II", "Inferno", "Nuke", "Train", "Mirage", "Overpass"],
        "Taxa de Vitória (%)": [67, 56, 50, 50, 50, 47, 0],
        "Últimos 5 Mapas": ["V V L V V", "V L V V L", "L V V L L", "FB V L V L", "FB FB FB FB FB", "V V L V V", "L L L"],
        "Partidas Jogadas": [18, 16, 12, 12, 2, 15, 3],
        "Vitórias CT (E)": [8, 10, 3, 8, 0, 2, 0],
        "Vitórias T (B)": [10, 6, 9, 4, 2, 8, 0],
        "CT % de Êxito": [49, 52, 45, 45, 71, 49, 58],
        "T % de Êxito": [56, 57, 53, 57, 24, 50, 20]
    }),
    "general_stats": {
        "torneios": {"contagem": 13, "taxa_ganho": 0},
        "partidas": {"contagem": 44, "taxa_ganho": 52},
        "mapas": {"contagem": 93, "taxa_ganho": 54},
        "rodadas": {"contagem": 1994, "taxa_ganho": 52}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 52},
        "5v4": {"valor": 0.52, "taxa": 73},
        "4v5": {"valor": 0.48, "taxa": 28},
        "bombas_plantadas": {"valor": 0.29, "taxa": 78},
        "bombas_desarmadas": {"valor": 0.66, "taxa": 100},
        "tempo_extra": {"valor": 0.05, "taxa": 52},
        "pistol": {"valor": 0.09, "taxa": 55},
        "eco": {"valor": 0.06, "taxa": 7},
        "force": {"valor": 0.20, "taxa": 38},
        "full_buy": {"valor": 0.65, "taxa": 59}
    }
},

"3DMAX": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Train", "Dust II", "Inferno", "Nuke", "Ancient", "Overpass", "Mirage"],
        "Taxa de Vitória (%)": [67, 60, 60, 44, 35, 0, 0],
        "Últimos 5 Mapas": ["FB V V", "L V L V V", "V L V V V", "V L V V V", "V L L L L", "L L", "FB FB FB FB FB"],
        "Partidas Jogadas": [4, 14, 19, 16, 17, 2, 5],
        "Vitórias CT (E)": [1, 6, 8, 4, 7, 0, 0],
        "Vitórias T (B)": [2, 8, 11, 3, 6, 0, 0],
        "CT % de Êxito": [50, 42, 47, 54, 53, 63, 0],
        "T % de Êxito": [42, 56, 54, 39, 43, 14, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 11, "taxa_ganho": 9},
        "partidas": {"contagem": 37, "taxa_ganho": 51},
        "mapas": {"contagem": 80, "taxa_ganho": 49},
        "rodadas": {"contagem": 1755, "taxa_ganho": 48}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 48},
        "5v4": {"valor": 0.47, "taxa": 73},
        "4v5": {"valor": 0.53, "taxa": 26},
        "bombas_plantadas": {"valor": 0.26, "taxa": 80},
        "bombas_desarmadas": {"valor": 0.59, "taxa": 100},
        "tempo_extra": {"valor": 0.06, "taxa": 57},
        "pistol": {"valor": 0.09, "taxa": 51},
        "eco": {"valor": 0.06, "taxa": 5},
        "force": {"valor": 0.21, "taxa": 36},
        "full_buy": {"valor": 0.64, "taxa": 55}
    }
},

"paiN_Gaming": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Nuke", "Dust II", "Inferno", "Mirage", "Ancient", "Overpass", "Train"],
        "Taxa de Vitória (%)": [47, 38, 38, 38, 33, 0, 0],
        "Últimos 5 Mapas": ["L V V V L", "V L L L L", "L V V V L", "FB L L V FB", "FB L L V V", " - - - - -", "FB FB FB FB FB"],
        "Partidas Jogadas": [15, 14, 16, 7, 6, 0, 4],
        "Vitórias CT (E)": [8, 3, 6, 2, 3, 0, 0],
        "Vitórias T (B)": [7, 4, 6, 5, 3, 0, 2],
        "CT % de Êxito": [53, 44, 44, 44, 61, 0, 35],
        "T % de Êxito": [48, 49, 53, 49, 27, 0, 37]
    }),
    "general_stats": {
        "torneios": {"contagem": 10, "taxa_ganho": 0},
        "partidas": {"contagem": 33, "taxa_ganho": 36},
        "mapas": {"contagem": 73, "taxa_ganho": 37},
        "rodadas": {"contagem": 1560, "taxa_ganho": 47}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 47},
        "5v4": {"valor": 0.51, "taxa": 67},
        "4v5": {"valor": 0.49, "taxa": 26},
        "bombas_plantadas": {"valor": 0.27, "taxa": 80},
        "bombas_desarmadas": {"valor": 0.55, "taxa": 100},
        "tempo_extra": {"valor": 0.03, "taxa": 48},
        "pistol": {"valor": 0.09, "taxa": 50},
        "eco": {"valor": 0.05, "taxa": 0},
        "force": {"valor": 0.23, "taxa": 38},
        "full_buy": {"valor": 0.63, "taxa": 54}
    }
},

"G2_Esports": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Inferno", "Dust II", "Ancient", "Mirage", "Nuke", "Train", "Overpass"],
        "Taxa de Vitória (%)": [71, 67, 58, 50, 38, 33, 0],
        "Últimos 5 Mapas": ["V L V V V", "L L V V V", "V L L V V", "L L V V L", "FB FB FB FB FB", "FB L V V V", "FB L"],
        "Partidas Jogadas": [21, 20, 18, 15, 12, 4, 0],
        "Vitórias CT (E)": [15, 11, 4, 6, 1, 0, 0],
        "Vitórias T (B)": [6, 9, 10, 5, 8, 4, 0],
        "CT % de Êxito": [56, 48, 54, 44, 57, 44, 0],
        "T % de Êxito": [55, 59, 51, 64, 37, 32, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 11, "taxa_ganho": 9},
        "partidas": {"contagem": 44, "taxa_ganho": 57},
        "mapas": {"contagem": 100, "taxa_ganho": 55},
        "rodadas": {"contagem": 2183, "taxa_ganho": 52}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 52},
        "5v4": {"valor": 0.49, "taxa": 73},
        "4v5": {"valor": 0.50, "taxa": 32},
        "bombas_plantadas": {"valor": 0.29, "taxa": 80},
        "bombas_desarmadas": {"valor": 0.65, "taxa": 100},
        "tempo_extra": {"valor": 0.04, "taxa": 55},
        "pistol": {"valor": 0.09, "taxa": 57},
        "eco": {"valor": 0.05, "taxa": 7},
        "force": {"valor": 0.23, "taxa": 43},
        "full_buy": {"valor": 0.64, "taxa": 58}
    }
},

"NIP": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Nuke", "Inferno", "Train", "Ancient", "Overpass", "Dust II", "Mirage"],
        "Taxa de Vitória (%)": [79, 62, 57, 54, 50, 48, 20],
        "Últimos 5 Mapas": ["V V V V", "FB FB FB V", "L L V L", "L L V L", "V L L V", "FB FB FB FB", "L L FB L"],
        "Partidas Jogadas": [34, 13, 23, 26, 4, 21, 5],
        "Vitórias CT (E)": [20, 0, 9, 1, 0, 0, 1],
        "Vitórias T (B)": [14, 11, 14, 13, 2, 10, 3],
        "CT % de Êxito": [64, 55, 60, 52, 62, 49, 35],
        "T % de Êxito": [60, 49, 45, 50, 33, 42, 12]
    }),
    "general_stats": {
        "torneios": {"contagem": 14, "taxa_ganho": 7},
        "partidas": {"contagem": 40, "taxa_ganho": 53},
        "mapas": {"contagem": 98, "taxa_ganho": 56},
        "rodadas": {"contagem": 2022, "taxa_ganho": 52}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 53},
        "5v4": {"valor": 0.52, "taxa": 74},
        "4v5": {"valor": 0.47, "taxa": 29},
        "bombas_plantadas": {"valor": 0.28, "taxa": 76},
        "bombas_desarmadas": {"valor": 0.60, "taxa": 100},
        "tempo_extra": {"valor": 0.03, "taxa": 43},
        "pistol": {"valor": 0.10, "taxa": 48},
        "eco": {"valor": 0.03, "taxa": 5},
        "force": {"valor": 0.25, "taxa": 44},
        "full_buy": {"valor": 0.62, "taxa": 60}
    }
},

"JiJieHao": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Train", "Dust II", "Nuke", "Inferno", "Mirage", "Ancient", "Overpass"],
        "Taxa de Vitória (%)": [100, 68, 63, 36, 33, 22, 0],
        "Últimos 5 Mapas": ["V V", "V V L V", "V V V L L", "L L L L V", "L L V L", "L L L", "FB FB FB FB"],
        "Partidas Jogadas": [5, 14, 5, 6, 7, 5, 4],
        "Vitórias CT (E)": [3, 7, 2, 2, 2, 1, 0],
        "Vitórias T (B)": [2, 2, 1, 2, 3, 0, 0],
        "CT % de Êxito": [63, 56, 59, 43, 43, 39, 0],
        "T % de Êxito": [55, 52, 42, 33, 38, 49, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 8, "taxa_ganho": 0},
        "partidas": {"contagem": 21, "taxa_ganho": 38},
        "mapas": {"contagem": 47, "taxa_ganho": 40},
        "rodadas": {"contagem": 1006, "taxa_ganho": 48}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 48},
        "5v4": {"valor": 0.50, "taxa": 68},
        "4v5": {"valor": 0.47, "taxa": 26},
        "bombas_plantadas": {"valor": 0.22, "taxa": 81},
        "bombas_desarmadas": {"valor": 0.50, "taxa": 100},
        "tempo_extra": {"valor": 0.06, "taxa": 53},
        "pistol": {"valor": 0.09, "taxa": 47},
        "eco": {"valor": 0.05, "taxa": 6},
        "force": {"valor": 0.22, "taxa": 37},
        "full_buy": {"valor": 0.65, "taxa": 55}
    }
},

"M80": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Overpass", "Ancient", "Mirage", "Train", "Inferno", "Dust II", "Nuke"],
        "Taxa de Vitória (%)": [88, 83, 72, 64, 60, 48, 0],
        "Últimos 5 Mapas": ["V V V L", "V V V V L", "V V L V V", "V V V L V", "V V L L V", "V L L L V", "FB FB FB FB"],
        "Partidas Jogadas": [17, 24, 18, 11, 15, 23, 4],
        "Vitórias CT (E)": [13, 9, 1, 0, 2, 4, 0],
        "Vitórias T (B)": [14, 18, 13, 11, 9, 7, 0],
        "CT % de Êxito": [66, 62, 60, 60, 61, 54, 0],
        "T % de Êxito": [65, 60, 53, 43, 44, 44, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 13, "taxa_ganho": 38},
        "partidas": {"contagem": 43, "taxa_ganho": 70},
        "mapas": {"contagem": 98, "taxa_ganho": 66},
        "rodadas": {"contagem": 1933, "taxa_ganho": 57}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 57},
        "5v4": {"valor": 0.53, "taxa": 78},
        "4v5": {"valor": 0.46, "taxa": 32},
        "bombas_plantadas": {"valor": 0.31, "taxa": 79},
        "bombas_desarmadas": {"valor": 0.60, "taxa": 100},
        "tempo_extra": {"valor": 0.02, "taxa": 67},
        "pistol": {"valor": 0.10, "taxa": 53},
        "eco": {"valor": 0.04, "taxa": 6},
        "force": {"valor": 0.20, "taxa": 45},
        "full_buy": {"valor": 0.66, "taxa": 64}
    }
},

"Nemiga": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Train", "Inferno", "Mirage", "Ancient", "Dust II", "Overpass", "Nuke"],
        "Taxa de Vitória (%)": [55, 50, 50, 50, 48, 0, 0],
        "Últimos 5 Mapas": ["L V L L", "FB FB L", "L L V L", "V L L", "V L L", "L", "L"],
        "Partidas Jogadas": [11, 8, 20, 24, 27, 1, 4],
        "Vitórias CT (E)": [3, 0, 1, 4, 9, 0, 0],
        "Vitórias T (B)": [5, 4, 9, 8, 4, 0, 0],
        "CT % de Êxito": [59, 46, 48, 44, 48, 50, 0],
        "T % de Êxito": [49, 45, 54, 55, 50, 40, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 15, "taxa_ganho": 0},
        "partidas": {"contagem": 47, "taxa_ganho": 45},
        "mapas": {"contagem": 84, "taxa_ganho": 48},
        "rodadas": {"contagem": 1805, "taxa_ganho": 50}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 50},
        "5v4": {"valor": 0.50, "taxa": 71},
        "4v5": {"valor": 0.50, "taxa": 28},
        "bombas_plantadas": {"valor": 0.31, "taxa": 76},
        "bombas_desarmadas": {"valor": 0.61, "taxa": 100},
        "tempo_extra": {"valor": 0.04, "taxa": 46},
        "pistol": {"valor": 0.09, "taxa": 52},
        "eco": {"valor": 0.06, "taxa": 5},
        "force": {"valor": 0.20, "taxa": 41},
        "full_buy": {"valor": 0.65, "taxa": 56}
    }
},

"Ence": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Overpass", "Dust II", "Train", "Mirage", "Ancient", "Nuke", "Inferno"],
        "Taxa de Vitória (%)": [75, 73, 56, 54, 53, 50, 0],
        "Últimos 5 Mapas": ["V V V V", "V V V L L", "L L L", "L V L V L", "L V V L V", "FB FB FB FB", "FB FB FB FB"],
        "Partidas Jogadas": [4, 37, 25, 35, 40, 28, 0],
        "Vitórias CT (E)": [2, 14, 5, 7, 11, 1, 0],
        "Vitórias T (B)": [2, 13, 10, 23, 9, 8, 0],
        "CT % de Êxito": [75, 51, 57, 54, 57, 52, 0],
        "T % de Êxito": [42, 64, 46, 51, 48, 48, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 25, "taxa_ganho": 12},
        "partidas": {"contagem": 81, "taxa_ganho": 62},
        "mapas": {"contagem": 180, "taxa_ganho": 59},
        "rodadas": {"contagem": 3755, "taxa_ganho": 53}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 54},
        "5v4": {"valor": 0.52, "taxa": 74},
        "4v5": {"valor": 0.47, "taxa": 32},
        "bombas_plantadas": {"valor": 0.28, "taxa": 77},
        "bombas_desarmadas": {"valor": 0.74, "taxa": 100},
        "tempo_extra": {"valor": 0.04, "taxa": 54},
        "pistol": {"valor": 0.09, "taxa": 51},
        "eco": {"valor": 0.05, "taxa": 2},
        "force": {"valor": 0.21, "taxa": 48},
        "full_buy": {"valor": 0.65, "taxa": 59}
    }
},




"Astralis": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Nuke", "Inferno", "Ancient", "Train", "Mirage", "Overpass", "Dust II"],
        "Taxa de Vitória (%)": [61, 60, 53, 43, 43, 33, 23],
        "Últimos 5 Mapas": ["V L V L L", "V V V V L", "V V L L V", "L FB FB FB L", "V L V FB L", "FB L V L", "L FB FB L L"],
        "Partidas Jogadas": [18, 15, 15, 7, 14, 3, 13],
        "Vitórias CT (E)": [11, 7, 8, 3, 7, 1, 5],
        "Vitórias T (B)": [7, 8, 7, 4, 6, 2, 3],
        "CT % de Êxito": [63, 54, 58, 61, 50, 33, 38],
        "T % de Êxito": [47, 47, 50, 42, 51, 58, 46]
    }),
    "general_stats": {
        "torneios": {"contagem": 10, "taxa_ganho": 0},
        "partidas": {"contagem": 35, "taxa_ganho": 51},
        "mapas": {"contagem": 84, "taxa_ganho": 49},
        "rodadas": {"contagem": 1759, "taxa_ganho": 51}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 51},
        "5v4": {"valor": 0.51, "taxa": 72},
        "4v5": {"valor": 0.49, "taxa": 30},
        "bombas_plantadas": {"valor": 0.25, "taxa": 78},
        "bombas_desarmadas": {"valor": 0.73, "taxa": 100},
        "tempo_extra": {"valor": 0.03, "taxa": 54},
        "pistol": {"valor": 0.09, "taxa": 50},
        "eco": {"valor": 0.04, "taxa": 3},
        "force": {"valor": 0.24, "taxa": 40},
        "full_buy": {"valor": 0.63, "taxa": 59}
    }
},

"TYLOO": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Dust II", "Ancient", "Overpass", "Nuke", "Inferno", "Train", "Mirage"],
        "Taxa de Vitória (%)": [80, 68, 50, 47, 44, 38, 27],
        "Últimos 5 Mapas": ["V V V L L", "V L V L L", "V L V L L", "V L L V L", "L L V L V", "V L V L L", "L L L L L"],
        "Partidas Jogadas": [25, 16, 6, 11, 19, 11, 18],
        "Vitórias CT (E)": [12, 12, 3, 5, 7, 2, 6],
        "Vitórias T (B)": [13, 4, 3, 6, 8, 9, 12],
        "CT % de Êxito": [49, 58, 60, 51, 46, 53, 44],
        "T % de Êxito": [69, 53, 42, 46, 51, 40, 46]
    }),
    "general_stats": {
        "torneios": {"contagem": 11, "taxa_ganho": 27},
        "partidas": {"contagem": 51, "taxa_ganho": 67},
        "mapas": {"contagem": 97, "taxa_ganho": 60},
        "rodadas": {"contagem": 2094, "taxa_ganho": 53}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 53},
        "5v4": {"valor": 0.50, "taxa": 72},
        "4v5": {"valor": 0.49, "taxa": 33},
        "bombas_plantadas": {"valor": 0.28, "taxa": 77},
        "bombas_desarmadas": {"valor": 0.67, "taxa": 100},
        "tempo_extra": {"valor": 0.06, "taxa": 54},
        "pistol": {"valor": 0.09, "taxa": 58},
        "eco": {"valor": 0.05, "taxa": 5},
        "force": {"valor": 0.22, "taxa": 45},
        "full_buy": {"valor": 0.64, "taxa": 58}
    }
},

"GamerLegion": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Inferno", "Train", "Mirage", "Ancient", "Overpass", "Nuke", "Dust II"],
        "Taxa de Vitória (%)": [67, 64, 63, 53, 50, 33, 0],
        "Últimos 5 Mapas": ["L L L V V", "V L V V V", "V L V V L", "V V V L L", "L V L V L", "L L L V V", "L L L L L"],
        "Partidas Jogadas": [16, 8, 13, 19, 2, 18, 5],
        "Vitórias CT (E)": [8, 4, 7, 9, 1, 6, 0],
        "Vitórias T (B)": [8, 4, 6, 10, 1, 6, 0],
        "CT % de Êxito": [49, 57, 60, 55, 56, 50, 0],
        "T % de Êxito": [59, 50, 50, 44, 45, 45, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 11, "taxa_ganho": 0},
        "partidas": {"contagem": 37, "taxa_ganho": 46},
        "mapas": {"contagem": 87, "taxa_ganho": 48},
        "rodadas": {"contagem": 1864, "taxa_ganho": 50}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 50},
        "5v4": {"valor": 0.50, "taxa": 70},
        "4v5": {"valor": 0.50, "taxa": 30},
        "bombas_plantadas": {"valor": 0.28, "taxa": 76},
        "bombas_desarmadas": {"valor": 0.59, "taxa": 100},
        "tempo_extra": {"valor": 0.04, "taxa": 49},
        "pistol": {"valor": 0.09, "taxa": 52},
        "eco": {"valor": 0.05, "taxa": 2},
        "force": {"valor": 0.23, "taxa": 41},
        "full_buy": {"valor": 0.63, "taxa": 56}
    }
},

"Team_Liquid": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Ancient", "Dust II", "Train", "Inferno", "Nuke", "Mirage", "Overpass"],
        "Taxa de Vitória (%)": [46, 41, 38, 33, 27, 23, 0],
        "Últimos 5 Mapas": ["V L L V V", "L V L V L", "V V L L L", "L V L L V", "L L V L L", "L L L V L", "FB FB FB FB FB"],
        "Partidas Jogadas": [12, 15, 8, 11, 11, 13, 5],
        "Vitórias CT (E)": [5, 3, 2, 4, 1, 9, 0],
        "Vitórias T (B)": [7, 5, 6, 7, 8, 4, 0],
        "CT % de Êxito": [44, 48, 56, 42, 44, 50, 0],
        "T % de Êxito": [48, 46, 38, 46, 44, 42, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 14, "taxa_ganho": 0},
        "partidas": {"contagem": 36, "taxa_ganho": 36},
        "mapas": {"contagem": 82, "taxa_ganho": 38},
        "rodadas": {"contagem": 1752, "taxa_ganho": 47}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 47},
        "5v4": {"valor": 0.48, "taxa": 71},
        "4v5": {"valor": 0.52, "taxa": 24},
        "bombas_plantadas": {"valor": 0.26, "taxa": 75},
        "bombas_desarmadas": {"valor": 0.59, "taxa": 100},
        "tempo_extra": {"valor": 0.05, "taxa": 43},
        "pistol": {"valor": 0.09, "taxa": 51},
        "eco": {"valor": 0.06, "taxa": 1},
        "force": {"valor": 0.22, "taxa": 39},
        "full_buy": {"valor": 0.63, "taxa": 53}
    }
},

"betbom": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Inferno", "Nuke", "Overpass", "Train", "Dust II", "Ancient", "Mirage"],
        "Taxa de Vitória (%)": [100, 65, 60, 59, 56, 55, 45],
        "Últimos 5 Mapas": ["V V V V V", "V V L L V", "V V L V", "L L L V", "L L V FB", "V L FB FB", "V L L L V"],
        "Partidas Jogadas": [15, 14, 16, 7, 6, 19, 4],
        "Vitórias CT (E)": [5, 10, 6, 2, 3, 10, 2],
        "Vitórias T (B)": [10, 4, 4, 5, 3, 10, 2],
        "CT % de Êxito": [55, 64, 41, 68, 51, 51, 47],
        "T % de Êxito": [58, 48, 49, 35, 53, 45, 51]
    }),
    "general_stats": {
        "torneios": {"contagem": 17, "taxa_ganho": 12},
        "partidas": {"contagem": 53, "taxa_ganho": 64},
        "mapas": {"contagem": 109, "taxa_ganho": 59},
        "rodadas": {"contagem": 2369, "taxa_ganho": 52}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 52},
        "5v4": {"valor": 0.51, "taxa": 74},
        "4v5": {"valor": 0.48, "taxa": 28},
        "bombas_plantadas": {"valor": 0.26, "taxa": 77},
        "bombas_desarmadas": {"valor": 0.85, "taxa": 100},
        "tempo_extra": {"valor": 0.06, "taxa": 56},
        "pistol": {"valor": 0.09, "taxa": 50},
        "eco": {"valor": 0.06, "taxa": 3},
        "force": {"valor": 0.20, "taxa": 43},
        "full_buy": {"valor": 0.65, "taxa": 59}
    }
},

"Legacy": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Overpass", "Ancient", "Mirage", "Nuke", "Inferno", "Train", "Dust II"],
        "Taxa de Vitória (%)": [100, 69, 67, 65, 59, 50, 36],
        "Últimos 5 Mapas": ["V V V V V", "L V V V V", "V V V L L", "L V L V V", "V V V L L", "V L FB FB FB", "V FB L FB FB"],
        "Partidas Jogadas": [1, 16, 25, 23, 23, 2, 14],
        "Vitórias CT (E)": [0, 0, 8, 2, 14, 0, 1],
        "Vitórias T (B)": [1, 7, 2, 7, 0, 2, 9],
        "CT % de Êxito": [67, 58, 55, 63, 57, 58, 42],
        "T % de Êxito": [71, 59, 56, 49, 56, 37, 54]
    }),
    "general_stats": {
        "torneios": {"contagem": 12, "taxa_ganho": 25},
        "partidas": {"contagem": 56, "taxa_ganho": 64},
        "mapas": {"contagem": 106, "taxa_ganho": 58},
        "rodadas": {"contagem": 2093, "taxa_ganho": 55}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 55},
        "5v4": {"valor": 0.56, "taxa": 73},
        "4v5": {"valor": 0.43, "taxa": 32},
        "bombas_plantadas": {"valor": 0.28, "taxa": 82},
        "bombas_desarmadas": {"valor": 0.58, "taxa": 100},
        "tempo_extra": {"valor": 0.03, "taxa": 49},
        "pistol": {"valor": 0.10, "taxa": 54},
        "eco": {"valor": 0.05, "taxa": 4},
        "force": {"valor": 0.21, "taxa": 48},
        "full_buy": {"valor": 0.66, "taxa": 61}
    }
},

"OG": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Overpass", "Nuke", "Ancient", "Mirage", "Dust II", "Inferno", "Train"],
        "Taxa de Vitória (%)": [100, 77, 68, 46, 45, 43, 38],
        "Últimos 5 Mapas": ["V V", "V L V V L", "L V V V V", "V L L V L", "FB FB FB FB FB", "V L V V V", "V V V L L"],
        "Partidas Jogadas": [2, 29, 35, 26, 11, 21, 8],
        "Vitórias CT (E)": [0, 7, 19, 1, 0, 1, 2],
        "Vitórias T (B)": [2, 1, 2, 13, 11, 14, 6],
        "CT % de Êxito": [79, 57, 58, 54, 42, 48, 48],
        "T % de Êxito": [54, 55, 52, 44, 52, 42, 42]
    }),
    "general_stats": {
        "torneios": {"contagem": 17, "taxa_ganho": 12},
        "partidas": {"contagem": 56, "taxa_ganho": 64},
        "mapas": {"contagem": 123, "taxa_ganho": 60},
        "rodadas": {"contagem": 2684, "taxa_ganho": 52}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 52},
        "5v4": {"valor": 0.52, "taxa": 73},
        "4v5": {"valor": 0.47, "taxa": 30},
        "bombas_plantadas": {"valor": 0.27, "taxa": 79},
        "bombas_desarmadas": {"valor": 0.83, "taxa": 100},
        "tempo_extra": {"valor": 0.05, "taxa": 47},
        "pistol": {"valor": 0.09, "taxa": 60},
        "eco": {"valor": 0.05, "taxa": 6},
        "force": {"valor": 0.21, "taxa": 44},
        "full_buy": {"valor": 0.65, "taxa": 58}
    }
},

"9z": {
    "map_stats": pd.DataFrame({
        "Mapa": ["Train", "Dust II", "Nuke", "Ancient", "Inferno", "Mirage", "Overpass"],
        "Taxa de Vitória (%)": [86, 67, 65, 62, 58, 33, 0],
        "Últimos 5 Mapas": ["V V V V V", "V V L V L", "L V L V L", "V L L V", "L L V L V", "V L V L V", "FB FB FB FB FB"],
        "Vitórias CT (E)": [0, 8, 10, 3, 2, 0, 0],
        "Vitórias T (B)": [6, 0, 1, 1, 6, 15, 9],
        "CT % de Êxito": [66, 63, 57, 51, 50, 60, 0],
        "T % de Êxito": [41, 55, 54, 51, 55, 45, 0]
    }),
    "general_stats": {
        "torneios": {"contagem": 12, "taxa_ganho": 8},
        "partidas": {"contagem": 36, "taxa_ganho": 69},
        "mapas": {"contagem": 83, "taxa_ganho": 59},
        "rodadas": {"contagem": 1642, "taxa_ganho": 54}
    },
    "round_stats": {
        "rodadas": {"valor": 1.0, "taxa": 54},
        "5v4": {"valor": 0.53, "taxa": 74},
        "4v5": {"valor": 0.46, "taxa": 32},
        "bombas_plantadas": {"valor": 0.28, "taxa": 81},
        "bombas_desarmadas": {"valor": 0.86, "taxa": 100},
        "tempo_extra": {"valor": 0.02, "taxa": 67},
        "pistol": {"valor": 0.10, "taxa": 54},
        "eco": {"valor": 0.05, "taxa": 2},
        "force": {"valor": 0.21, "taxa": 46},
        "full_buy": {"valor": 0.64, "taxa": 61}
    }
},
}

for team, data in time_data.items():
    try:
        df = data["map_stats"]
        # pega o tamanho de cada coluna
        lengths = {col: len(df[col].values) for col in df.columns}
        if len(set(lengths.values())) != 1:
            print(f"\n⚠️ Erro no time: {team}")
            print(lengths)
    except Exception as e:
        print(f"Erro ao verificar {team}: {e}")


import pandas as pd

mapas_disponiveis = ["Dust II", "Inferno", "Train", "Nuke", "Mirage", "Overpass", "Ancient"]

# -------------------------
# Função auxiliar para bolinhas
# -------------------------
def mostrar_bolinhas(ultimos_mapas):
    """
    Recebe uma string com os últimos resultados (ex: "V L V V L") 
    e retorna HTML com bolinhas coloridas.
    """
    if not ultimos_mapas or pd.isna(ultimos_mapas):
        return ""

    bolinhas = ""
    # Garante que seja string e separa por espaço
    resultados = str(ultimos_mapas).split()
    for resultado in resultados:
        if resultado == "V":
            bolinhas += '<span class="bolinha green-bubble">V</span>'
        elif resultado == "L":
            bolinhas += '<span class="bolinha red-bubble">L</span>'
        else:
            bolinhas += f'<span class="bolinha">{resultado}</span>'
    return bolinhas

def calcular_pontuacao_completa(time_stats, mapa):
    """
    Calcula a pontuação completa de um time em um mapa específico.
    Considera:
    - Estatísticas do mapa
    - Sequência de vitórias recentes
    - Estatísticas gerais (últimos 6 meses)
    - Estatísticas de rodadas
    - Quantidade de partidas jogadas no mapa (peso de confiança)
    """

    # --- Pesos do mapa ---
    pesos_mapas = {
        "Inferno": {"ct": 0.35, "t": 0.30},
        "Nuke": {"ct": 0.40, "t": 0.25},
        "Mirage": {"ct": 0.30, "t": 0.30},
        "Overpass": {"ct": 0.35, "t": 0.25},
        "Ancient": {"ct": 0.35, "t": 0.25},
        "Dust II": {"ct": 0.25, "t": 0.35},
        "Train": {"ct": 0.35, "t": 0.25},
    }

    peso_ct = pesos_mapas.get(mapa, {"ct": 0.3, "t": 0.3})["ct"]
    peso_t = pesos_mapas.get(mapa, {"ct": 0.3, "t": 0.3})["t"]

    # --- Pontuação do mapa ---
    df = time_stats["map_stats"]
    if mapa not in df['Mapa'].values:
        return 0  # Se o time não tiver estatísticas do mapa, retorna 0

    stats = df[df["Mapa"] == mapa].iloc[0]

    # Sequência de vitórias recentes
    ult_vitorias = str(stats.get("Últimos 5 Mapas", "")).count("V")
    sequencia = (ult_vitorias / 5) * 100  # normaliza 0-100

    # Usa "Partidas Jogadas" para dar mais peso em quem tem mais histórico no mapa
    partidas_jogadas = stats.get("Partidas Jogadas", 0)
    fator_amostra = 1 + min(partidas_jogadas, 30) / 20  # trava no máx. 2.5x

    mapa_score = (
        0.4 * stats.get("Taxa de Vitória (%)", 0) +
        peso_ct * stats.get("CT % de Êxito", 0) +
        peso_t * stats.get("T % de Êxito", 0) +
        2 * sequencia
    ) * fator_amostra

    # --- Estatísticas gerais ---
    general = time_stats.get("general_stats", {})
    geral_score = 0
    if general:
        geral_score = (
            0.3 * general.get("torneios", {}).get("taxa_ganho", 0) +
            0.3 * general.get("partidas", {}).get("taxa_ganho", 0) +
            0.2 * general.get("mapas", {}).get("taxa_ganho", 0) +
            0.2 * general.get("rodadas", {}).get("taxa_ganho", 0)
        )

    # --- Estatísticas de rodadas ---
    rounds = time_stats.get("round_stats", {})
    pesos_rounds = {
        "5v4": 0.15,
        "4v5": 0.15,
        "bombas_plantadas": 0.1,
        "bombas_desarmadas": 0.1,
        "tempo_extra": 0.05,
        "pistol": 0.15,
        "eco": 0.05,
        "force": 0.1,
        "full_buy": 0.15
    }
    rounds_score = 0
    for chave, peso in pesos_rounds.items():
        if chave in rounds:
            rounds_score += peso * rounds[chave].get("taxa", 0)

    # --- Pontuação final ---
    pontuacao_final = (mapa_score * 0.5) + (geral_score * 0.25) + (rounds_score * 0.25)
    return pontuacao_final


# Função para gerar opções de times
def gerar_opcoes_times(time_data, time1_name="", time2_name=""):
    opcoes = ""
    for time in sorted(time_data.keys()):
        selecionado1 = 'selected' if time.lower() == time1_name.lower() else ''
        selecionado2 = 'selected' if time.lower() == time2_name.lower() else ''
        opcoes += f'<option value="{time}" {selecionado1}{selecionado2}>{time}</option>'
    return opcoes

# Função para gerar opções de mapas
def gerar_opcoes_mapas(mapas_disponiveis, mapas_selecionados=[]):
    opcoes = ""
    for mapa in mapas_disponiveis:
        selecionado = 'selected' if mapa in mapas_selecionados else ''
        opcoes += f'<option value="{mapa}" {selecionado}>{mapa}</option>'
    return opcoes


@app.route("/", methods=["GET", "POST"])
def index():
    comparacoes_html = ""
    time1_name = ""
    time2_name = ""
    mapas_selecionados = []

    if request.method == "POST":
        time1_name = request.form['time1']
        time2_name = request.form['time2']
        mapas_selecionados = request.form.getlist('mapas')

        if time1_name not in time_data or time2_name not in time_data:
            comparacoes_html += "<p class='error'>Um ou ambos os times não existem na base de dados.</p>"
        else:
            df_time1 = time_data[time1_name]["map_stats"]
            df_time2 = time_data[time2_name]["map_stats"]

            for mapa in mapas_selecionados:
                if mapa in df_time1['Mapa'].values and mapa in df_time2['Mapa'].values:
                    stats1 = df_time1[df_time1['Mapa'] == mapa].iloc[0]
                    stats2 = df_time2[df_time2['Mapa'] == mapa].iloc[0]

                    ult1 = str(stats1['Últimos 5 Mapas'])
                    ult2 = str(stats2['Últimos 5 Mapas'])

                    melhor_vitoria = time1_name if stats1['Taxa de Vitória (%)'] > stats2['Taxa de Vitória (%)'] else time2_name
                    melhor_ct = time1_name if stats1['CT % de Êxito'] > stats2['CT % de Êxito'] else time2_name
                    melhor_t = time1_name if stats1['T % de Êxito'] > stats2['T % de Êxito'] else time2_name
                    sequencia_vitoria = time1_name if ult1.count("V") > ult2.count("V") else time2_name

                    pont_time1 = calcular_pontuacao_completa(time_data[time1_name], mapa)
                    pont_time2 = calcular_pontuacao_completa(time_data[time2_name], mapa)

                    total = pont_time1 + pont_time2
                    if total == 0:
                        perc_time1 = perc_time2 = 50
                    else:
                        perc_time1 = round((pont_time1 / total) * 100)
                        perc_time2 = round((pont_time2 / total) * 100)

                    if perc_time1 > perc_time2:
                        mais_chance = f"{time1_name} {perc_time1}%"
                    elif perc_time2 > perc_time1:
                        mais_chance = f"{time2_name} {perc_time2}%"
                    else:
                        mais_chance = "Empate 50%"

                    general1 = time_data[time1_name]["general_stats"]
                    general2 = time_data[time2_name]["general_stats"]
                    general_comparacao = ""
                    for chave in general1:
                        taxa1 = general1[chave]["taxa_ganho"]
                        taxa2 = general2[chave]["taxa_ganho"]
                        vencedor = time1_name if taxa1 > taxa2 else (time2_name if taxa2 > taxa1 else "Empate")
                        general_comparacao += f"<tr><td>{chave.capitalize()}</td><td>{vencedor}</td></tr>"

                    round1 = time_data[time1_name]["round_stats"]
                    round2 = time_data[time2_name]["round_stats"]
                    rounds_comparacao = ""
                    for chave in round1:
                        taxa1 = round1[chave]["taxa"]
                        taxa2 = round2[chave]["taxa"]
                        vencedor = time1_name if taxa1 > taxa2 else (time2_name if taxa2 > taxa1 else "Empate")
                        rounds_comparacao += f"<tr><td>{chave}</td><td>{vencedor}</td></tr>"

                    comparacoes_html += f"""
                    <div class='comparacao'>
                        <h3>{mapa}</h3>
                        <div class="stats-grid">
                            <div class="stat-card victory"><p>Melhor média de vitória</p><span>{melhor_vitoria}</span></div>
                            <div class="stat-card ct"><p>Melhor média de CT</p><span>{melhor_ct}</span></div>
                            <div class="stat-card t"><p>Melhor média de T</p><span>{melhor_t}</span></div>
                            <div class="stat-card streak"><p>Sequência de vitórias</p><span>{sequencia_vitoria}</span></div>
                            <div class="stat-card chance"><p>Mais chance de vencer</p><span>{mais_chance}</span></div>
                        </div>
                        <div class="time">
                            <h4>{time1_name}</h4>
                            <table>
                                <tr><td>Taxa de Vitória:</td><td>{stats1['Taxa de Vitória (%)']}%</td></tr>
                                <tr><td>Últimos 5 Mapas:</td><td>{mostrar_bolinhas(stats1['Últimos 5 Mapas'])}</td></tr>
                            </table>
                        </div>
                        <div class="time">
                            <h4>{time2_name}</h4>
                            <table>
                                <tr><td>Taxa de Vitória:</td><td>{stats2['Taxa de Vitória (%)']}%</td></tr>
                                <tr><td>Últimos 5 Mapas:</td><td>{mostrar_bolinhas(stats2['Últimos 5 Mapas'])}</td></tr>
                            </table>
                        </div>
                        <div class='extra-comparacao'>
                            <h4>General Stats</h4>
                            <table>{general_comparacao}</table>
                            <h4>Round Stats</h4>
                            <table>{rounds_comparacao}</table>
                        </div>
                    </div>
                    """
                else:
                    comparacoes_html += f"<p class='error'>O mapa {mapa} não está disponível para comparação.</p>"

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Comparação de Times</title>
        <style>
            body { font-family: Arial, sans-serif; background: #1e272e; margin: 0; padding: 20px; }
            .container { max-width: 1100px; margin: auto; background: #2f3640; padding: 20px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.4); color: #ecf0f1; }
            h1 { text-align: center; color: #f39c12; }
            form { display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px; }
            select, button { padding: 10px; font-size: 16px; border-radius: 6px; border: 1px solid #444; background: #353b48; color: #fff; }
            button { background-color: #e67e22; color: #fff; border: none; cursor: pointer; font-weight: bold; }
            button:hover { background-color: #d35400; box-shadow: 0 4px 12px rgba(0,0,0,0.4); }
            .comparacao { background: #3d3d3d; border: 1px solid #555; border-radius: 8px; padding: 20px; margin-bottom: 20px; }
            .time h4 { color: #3498db; margin-bottom: 5px; }
            .bolinha { width: 25px; height: 25px; border-radius: 50%; display: inline-block; text-align: center; line-height: 25px; font-weight: bold; margin-right: 5px; }
            .green-bubble { background-color: #27ae60; color: white; }
            .red-bubble { background-color: #e74c3c; color: white; }
            .error { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Comparação de Times</h1>
            <form method="post">
                <label>Time 1:</label>
                <select name="time1">{{ opcoes_times|safe }}</select>
                <label>Time 2:</label>
                <select name="time2">{{ opcoes_times|safe }}</select>
                <label>Mapas:</label>
                <select name="mapas" multiple>{{ opcoes_mapas|safe }}</select>
                <button type="submit">Comparar</button>
            </form>
            <div>
                {{ comparacoes_html|safe }}
            </div>
        </div>
    </body>
    </html>
    """

    return render_template_string(
        html_template,
        opcoes_times=gerar_opcoes_times(time_data, time1_name, time2_name),
        opcoes_mapas=gerar_opcoes_mapas(mapas_disponiveis, mapas_selecionados),
        comparacoes_html=comparacoes_html
    )

# -------------------------
# Rodar o app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)