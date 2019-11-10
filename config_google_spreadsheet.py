# import gspread
#
# # Подключение Google drive
# from oauth2client.service_account import ServiceAccountCredentials
#
# try:
#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#     client = gspread.authorize(credentials=creds)
#     sheet = client.open('Mastermind_data')
#     sheet_list = sheet.sheet1.get_all_values()
#     print(sheet_list)
# except:
#     print("No internet, can't load Google Spreadsheet")
#
#
# # def get_list_of_values(user_id: int):
# #     print('Got')
# #     return sheet.sheet1.row_values(get_user_row(user_id))
#
# # ----------
#
# # STATE_COL = sheet.sheet1.find("State").col
# # LANGUAGE_COL = sheet.sheet1.find("Language").col
# # GAME_COL = sheet.sheet1.find("Game_status").col
# # GAME_COMBINATION_COL = sheet.sheet1.find("Game_comb").col
# # GAME_STEPS_COL = sheet.sheet1.find("Steps").col
# # BEST_SCORE = sheet.sheet1.find("Best_score").col
#
# NUMBER_COL = sheet_list[0].index('#')
# ID_COL = sheet_list[0].index('id')
# FIRST_NAME_COL = sheet_list[0].index('First Name')
# LAST_NAME_COL = sheet_list[0].index('Last Name')
# LOGIN_COL = sheet_list[0].index('Login')
# STATE_COL = sheet_list[0].index('State')
# LANGUAGE_COL = sheet_list[0].index('Language')
# GAME_STATE_COL = sheet_list[0].index('Game_status')
# GAME_COMBINATION_COL = sheet_list[0].index('Game_comb')
# GAME_STEPS_COL = sheet_list[0].index('Steps')
# BEST_SCORE_COL = sheet_list[0].index('Best_score')
#
#
# # --------
#
# def upgrade_row(user_id : int, row : list):
#     user_row = get_user_row(user_id=user_id)
#     cell_list = sheet.sheet1.range('A5:K5')
#
#     for i, val in enumerate(row):
#         cell_list[i].value = str(val)
#
#     sheet.sheet1.update_cells(cell_list)
#
# # --------
#
# # def get_number_of_rows(x: sheet) -> int:
# #     return x.sheet1.get_all_values().__len__()
#
# def get_user_row(user_id: int) -> int:
#     index = 0
#     for list in sheet_list:
#         if list[ID_COL] == str(user_id):
#             return index
#         index += 1
#
#
# def get_number_of_rows() -> int:
#     return len(sheet_list)-1
#
#
# def get_user_state(user_id: int) -> str:
#     return str(sheet_list[get_user_row(user_id)][STATE_COL])
#
#
# def get_user_language(user_id: int) -> str:
#     return str(sheet_list[get_user_row(user_id)][LANGUAGE_COL])
#
#
# def get_user_game_state(user_id: int) -> str:
#     return str(sheet_list[get_user_row(user_id)][GAME_STATE_COL])
#
#
# def get_user_game_combination(user_id: int) -> str:
#     return str(sheet_list[get_user_row(user_id)][GAME_COMBINATION_COL])
#
#
# def get_user_game_steps(user_id: int) -> int:
#     return int(sheet_list[get_user_row(user_id)][GAME_STEPS_COL])
#
#
# def get_user_best_score(user_id: int) -> int:
#     return int(sheet_list[get_user_row(user_id)][BEST_SCORE_COL])
#
#
# # def get_user_row(user_id: int) -> int:
# #     return sheet.sheet1.find(str(user_id)).row
#
#
# # def get_user_state(user_id: int) -> str:
# #     return sheet.sheet1.cell(get_user_row(user_id), STATE_COL).value
#
#
# # def get_user_language(user_id: int) -> str:
# #     return sheet.sheet1.cell(get_user_row(user_id), LANGUAGE_COL).value
#
#
# # def get_user_game_state(user_id: int) -> str:
# #     return sheet.sheet1.cell(get_user_row(user_id), GAME_COL).value
#
#
# # def get_user_game_combination(user_id: int) -> str:
# #     return sheet.sheet1.cell(get_user_row(user_id), GAME_COMBINATION_COL).value
#
#
# # def get_user_game_steps(user_id: int) -> int:
# #     return int(sheet.sheet1.cell(get_user_row(user_id), GAME_STEPS_COL).value)
#
#
# # def get_user_best_score(user_id: int) -> int:
# #     return sheet.sheet1.cell(get_user_row(user_id), BEST_SCORE_COL).value
