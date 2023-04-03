from flask_app import db, app

app.app_context().push()
db.create_all()

# jonas = Message('Jonas', 'jonas@mail.com', 'Kažkoks labai rimtas atsiliepimas.')
# antanas = Message('Antanas', 'antanas@mail.lt', 'Antano nuomonė labai svarbi.')
# juozas = Message('Juozas', 'juozukas@friends.lt', 'Aš labai piktas, nes blogai.')
# bronius = Message('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.')

# db.session.add_all([jonas, antanas, juozas, bronius])
#
# db.session.commit()
#
# print(jonas.message)
# print(antanas.message)
# print(juozas.message)
# print(bronius.message)
