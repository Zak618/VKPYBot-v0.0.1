import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token='')
session_api = session.get_api()
longpoll = VkLongPoll(session)


hello_list = ('И тебе привет!',
              'Привет',
              'Доброго времени суток')



films_list = ('Человек-паук: Нет пути домой', 'Побег из Шоушенка', 'Крёстный отец', 'Тёмный рыцарь','12 разгневанных мужчин',
              'Криминальное чтиво', 'Властелин колец: Братство Кольца',
              'Хороший, плохой, злой', 'Бойцовский клуб', 'Матрица', 'Пролетая над гнездом кукушки',
              'Эта прекрасная жизнь', 'Спасти рядового Райана', 'Унесённые призраками', 'Американская история Икс',
              'Однажды на Диком Западе', 'Огни большого города', 'Джанго освобождённый', 'Бульвар Сансет')



photo_list = ('photo-173002735_457309202', 'photo-173002735_457309207', 'photo-173002735_457309213', 'photo-173002735_457309227',
              'photo-173002735_457292431', 'photo-173002735_457276112', 'photo-173002735_457274837', 'photo-74554829_457711115',
              'photo-74554829_457714169', 'photo-74554829_457714045', 'photo-74554829_457714053')


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ', event.datetime)
            print('Текст сообщения', event.text)
            response = event.text.lower()
            if event.from_user and not event.from_me:
                if response.find('привет') >= 0 or response.find('здравствуй') >= 0:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send', {'user_id':event.user_id,
                                                     'message':random.choice(hello_list),
                                                     'random_id':'0'})

                elif response.find('как дела') >= 0:
                    session.method('messages.send',
                                   {'user_id':event.user_id,
                                    'message':'',
                                    'random_id':'0',
                                    'sticker_id':'126'})

                
                elif response.find('фото') >= 0:
                    session.method('messages.send',
                                    {'user_id':event.user_id,
                                    'message':'',
                                    'random_id':'0',
                                    'attachment':'photo-213222031_457239034'})


                elif response.find('фильм') >= 0:
                    session.method('messages.send',
                                    {'user_id':event.user_id,
                                    'message':random.choice(films_list),
                                    'random_id':'0'})
                


                elif response.find('картин') >= 0:
                    session.method('messages.send',
                                    {'user_id':event.user_id,
                                    'message':'',
                                    'random_id':'0',
                                    'attachment':random.choice(photo_list)})
