from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
import pprint


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')

table = dynamodb.Table('Minimastergame_users')

table_user_games = dynamodb.Table('Minimastergame_users_games')


def get_item(user_id: int) -> dict:
    pprint.pprint(table.get_item(Key={'ID': user_id}))
    return table.get_item(Key={'ID': user_id})['Item']


def get_user_game_state(user_id: int) -> str:
    return get_item(user_id=user_id)['Game_status']
    # return str(sheet_list[get_user_row(user_id)][STATE_COL])


def get_user_language(user_id: int) -> str:
    return get_item(user_id=user_id)['User_language']


def get_user_game_combination(user_id: int) -> str:
    return get_item(user_id=user_id)['Game_comb']


def get_user_games_number(user_id: int) -> int:
    return get_item(user_id=user_id)['Games']


def get_user_game_steps(user_id: int) -> int:
    return get_item(user_id=user_id)['Steps']


def get_user_best_score(user_id: int) -> int:
    return get_item(user_id=user_id)['Best_score']


def update(user_id: int, item: str, new_value: str):
    table.update_item(
        Key={'ID': user_id},
        UpdateExpression=f'SET {item} = :val',
        ExpressionAttributeValues={
            ':val': new_value
        }
    )


def exists(value: str) -> bool:
    try:
        item = table.get_item(hash_key=value)
        return True
    except:
        return False
    # try:
    #     table.get_item(Key={'ID': value})
    #     print('Found item')
    #     return True
    # except Exception as e:
    #     print(e)
    #     return False


def append_in_table(ID: int, First_Name: str, User_language: str, Game_status: str,
                    Game_comb: str, Steps: str, Best_score: str, Games: int):
    response = table.put_item(
        Item={
            'ID': ID,
            'First Name': First_Name,
            # 'Last Name': Last_Name,
            # 'Login': Login,
            'User_language': User_language,
            'Game_status': Game_status,
            'Game_comb': Game_comb,
            'Steps': Steps,
            'Best_score': Best_score,
            'Games': Games
        }
    )
    print("PutItem succeeded:")
    pprint.pprint(response)


def append_game_in_table(ID: int, Game_number: int, Number_of_steps: int):
    response = table_user_games.put_item(
        Item={
            'ID': ID,
            'Game number': Game_number,
            'Number of steps': Number_of_steps
        }
    )
    print("PutItem succeeded:")
    pprint.pprint(response)

#
#
# print("Movies from 1985")
#
# response = table.query(
#     KeyConditionExpression=Key('year').eq(2019)
# )
#
# for i in response['Items']:
#     print(i['year'], ":", i['title'])
#
# def get_item_by_year(year : int):
#     response = table.query(KeyConditionExpression=Key('year').eq(1985))
#     answer = ''
#     for i in response['Items']:
#         answer += str(i['year']) + " :" + str(i['title'] + '\n')
#     return answer
