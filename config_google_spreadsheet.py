import gspread

# Подключение Google drive
from oauth2client.service_account import ServiceAccountCredentials

try:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Mastermind_data')
except:
    print("No internet, can't load Google Spreadsheet")

# ----------

STATE_COL = sheet.sheet1.find("State").col
LANGUAGE_COL = sheet.sheet1.find("Language").col
GAME_COL = sheet.sheet1.find("Game_status").col
GAME_COMBINATION_COL = sheet.sheet1.find("Game_comb").col
GAME_STEPS_COL = sheet.sheet1.find("Steps").col
BEST_SCORE = sheet.sheet1.find("Best_score").col


# --------

def get_number_of_rows(x: sheet) -> int:
    return x.sheet1.get_all_values().__len__()


def get_user_row(user_id: int) -> int:
    return sheet.sheet1.find(str(user_id)).row


def get_user_state(user_id: int) -> str:
    return sheet.sheet1.cell(get_user_row(user_id), STATE_COL).value


def get_user_language(user_id: int) -> str:
    return sheet.sheet1.cell(get_user_row(user_id), LANGUAGE_COL).value


def get_user_game_state(user_id: int) -> str:
    return sheet.sheet1.cell(get_user_row(user_id), GAME_COL).value


def get_user_game_combination(user_id: int) -> str:
    return sheet.sheet1.cell(get_user_row(user_id), GAME_COMBINATION_COL).value


def get_user_game_steps(user_id: int) -> int:
    return int(sheet.sheet1.cell(get_user_row(user_id), GAME_STEPS_COL).value)


def get_user_best_score(user_id: int) -> str:
    return sheet.sheet1.cell(get_user_row(user_id), BEST_SCORE).value
