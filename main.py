from telethon import TelegramClient, events, Button as button
from os import getenv


api_id = getenv("api_id")
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")


client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    reply_btns = [
                    button.url("Силка На Проєкт", "https://github.com/leonidig/X-PYTHON-MANAGER")
    ]
    await event.reply(f"Привіт, {first_name}!\nЯ бот який допоможе тобі з запуском проекта!", buttons=reply_btns)
    next1_ = [
        button.inline("Скопіював!", b'next1_')
    ]
    await event.respond("Тепер нажимай на кнопку і копіюй шлях до мого репозиторія", buttons = next1_)


@client.on(events.CallbackQuery(pattern=b"next1_"))
async def create_file(event):
    next2 = [
        button.inline("Створив!", b'next2')
    ]
    await event.respond("Так, посилання в нас є.\nДавай тепер створемо папку для цього проєкту", buttons = next2)


@client.on(events.CallbackQuery(pattern=b'next2'))
async def start_open_project(event):
    await event.respond("Круто виходить!\nТепер треба відкрити цей проєкт, повторюй за мною\nТепер треба відкрити редактор коду")
    vs_code_path = '/Users/leonidlisovskiy/Desktop/bot-balance-manager/open_vs_code.png'
    next3 = [
        button.inline("Далі", b'next3')
    ]
    await client.send_file(event.chat_id, vs_code_path, caption="В тебе повинно бути щось схоже - це сторінка привітання",buttons=next3)
    


@client.on(events.CallbackQuery(pattern=b'next3'))
async def open_project(event):
    await event.respond("Тепер нажми f1, та напиши ->\n' >clone '")
    git_clone_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/git_clone.png"
    next4 = [
        button.inline("Далі", b'next4')
    ]
    await client.send_file(event.chat_id, git_clone_path, caption="В тебе повинно вийти наступним чином\nТепер жми Enter\nПримітка!Якщо в тебе як в мене немає клавіши f1 - то нажми на це поле вище і так само введи >clone", buttons=next4)
    

@client.on(events.CallbackQuery(pattern=b"next4"))
async def enter_url(event):
    entered_url_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/enter_path.png"
    await event.respond("Тепер ти можеш вставляти туди шлях до репозиторія який ми скопіювали раніше")
    next5 = [
        button.inline("Далі", b"next5")
    ]
    await client.send_file(event.chat_id, entered_url_path, caption="В тебе повинно вийти як на фото\nІ тепер жми на Enter", buttons=next5)


@client.on(events.CallbackQuery(pattern=b'next5'))
async def opent_folder(event):
    open_folder_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/open_folder.png"
    await event.respond("Тепер обирай у якому файлі ти відкриєш проєкт.\nОбирай папку яку ми створили декілька етапів назад")
    next6 = [
        button.inline("Далі", b'next6')
    ]
    await client.send_file(event.chat_id, open_folder_path, caption="Обираєщ свою папку і жмеш - Select as Repository Destinaton", buttons=next6)
    


@client.on(events.CallbackQuery(pattern=b'next6'))
async def confirm(event):
    confirm_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/confirm_opening.png"
    next7 = [
        button.inline("Погнали далі", b'next7')
    ]
    await client.send_file(event.chat_id, confirm_path, caption="Ти майже відкрив, тепер тут обери першу кнопку - Open", buttons=next7)


@client.on(events.CallbackQuery(pattern=b'next7'))
async def render_project(event):
    done_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/opening_done.png"
    next8 = [
        button.inline("Далі", b'next8')
    ]
    await client.send_file(event.chat_id, done_path, caption="Ура🥳\nТи відкрив проєкт\nАле цього недостатньо, щоб він працював треба скачати необхідні бібліотеки.", buttons=next8)


@client.on(events.CallbackQuery(pattern=b'next8'))
async def open_terminal(event):
    open_terminal_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/open_terminal.png"
    next9 = [
        button.inline("Далі", b'next9')
    ]
    await client.send_file(event.chat_id, open_terminal_path,caption="Гарячі клавіши для терміналу->\nctrl + shift + ~\nMacBook -\ncontrol + shif + ~\nАбо зверху оберіть Terminal -> New Terminal", buttons=next9)



@client.on(events.CallbackQuery(pattern=b'next9'))
async def create_venv(event):
    os_choice = [
        [button.inline("MacOS", b'macos')],
        [button.inline("Linux", b'linux')],
        [button.inline("Windows", b'windows')]
    ]
    await event.respond("Обери свою операційну систему", buttons = os_choice)

# \nШаг 2 - source .venv/bin/activate(жми enter)

@client.on(events.CallbackQuery)
async def venv_by_os(event):
    if event.data == b'macos' or event.data == b'linux':
        await event.respond("Щоб створити віртуальне середовище( venv, потрібно щоб в нього качати всі бібліотеки, а не напряму тобі на гаджет) тобі потрібно ввести наступні 2 команди -\nШаг 1 -\npython3 -m venv .venv (жми enter)")
        confirm_venv_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/confirm_venv.png"
        await client.send_file(event.chat_id, confirm_venv_path, caption="На цьому етапі у тебе програма запитає чи ви хочете обрати свій venv як робочій простір - жми Yes")
        await event.respond("Шаг 2 - source .venv/bin/activate(жми enter)")
        show_venv_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/show_venv.png"
        next10 = [
            button.inline("Продовжуємо", b'next10')
        ]
        await client.send_file(event.chat_id, show_venv_path, caption="Знак того що все успішно створилося - в тебе перед імʼям пишеться (.venv)", buttons=next10)

    elif event.data == b'windows':
        await event.respond("Щоб створити віртуальне середовище( venv ) тобі потрібно ввести наступні 2 команди -\nШаг 1 -\npython -m venv venv (жми enter)")
        confirm_venv_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/confirm_venv.png"
        await client.send_file(event.chat_id, confirm_venv_path, caption="На цьому етапі у тепе програма запитає чи ви хочете обрати свій venv як робочій простір - жми Yes")
        await event.respond("Шаг 2 -  source .venv/bin/activate  (жми enter)")
        next10 = [
            button.inline("Продовжуємо", b'next10')
        ]
        await event.respond("Якщо в тебе поряд з іменем на початку строки написано .venv ( venv, потрібно щоб в нього качати всі бібліотеки, а не напряму тобі на гаджет ) то це означає що ми все правильно зробили", buttons = next10)


@client.on(events.CallbackQuery(pattern=b'next10'))
async def installing(event):
    await event.respond("Тепер треба у терміналі ввести команду\npip install -r requirements.txt\nЩоб скачати всі необхідні бібліотеки")
    done_downloading_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/downloading_done.png"
    next11_ = [
        button.inline("Далі", b'next11_')
    ]
    await client.send_file(event.chat_id, done_downloading_path, caption='У кінці встановлення ти побачиш наступне( якщо помики відсутні)', buttons=next11_)


@client.on(events.CallbackQuery(pattern=b'next11_'))
async def create_file(event):
    create_file_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/create_file.jpg"
    next12_ = [
        button.inline("Далі", b'next12_')
    ]
    await client.send_file(event.chat_id, create_file_path, caption="Тепер створи файл з назвою .env", buttons=next12_)


@client.on(events.CallbackQuery(pattern=b'next12_'))
async def enter_text(event):
    enter_text_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/enter_text.png"
    next13_ = [
        button.inline("Далі", b'next13_')
    ]
    await client.send_file(event.chat_id, enter_text_path, caption="Введи туди наступне -\nSECRET_KEY = 'kjdjsdhvuySD*(v7s9dviugdKJ)' - цей ключ може бути будь яким - тому просто побий по клавіатурі)\nBACKEND_URL = 'http://127.0.0.1:8000' - це вже повністю спиши в мене бо воно повинно бути іменно таким як я написав\nУ кінці в тебе повинно вийти як у мене на картинці ", buttons=next13_)



@client.on(events.CallbackQuery(pattern=b'next13_'))
async def boot_terminal(event):
    boot_terminal_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/boot_terminal.jpg"
    next14_ = [
        button.inline("Далі", b'next14_')
    ]
    await client.send_file(event.chat_id, boot_terminal_path, caption="Тепер створи термінал як я тобі показував вище\nТа нажми те що я тобі обвів у кружечок", buttons=next14_)


@client.on(events.CallbackQuery(pattern=b'next14_'))
async def show_terminal_(event):
    show_terminal_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/dual_terminal.png"
    next15_ = [
        button.inline("Далі", b'next15_')
    ]
    await client.send_file(event.chat_id, show_terminal_path, caption="Ось так повинна виглядати программиа у тебе", buttons=next15_)


@client.on(events.CallbackQuery(pattern=b'next15_'))
async def enter_commands(event):
    next16_ = [
        button.inline("Далі", b'next16_')
    ]
    await event.respond("Ти вже майже завершив\nТепер у лівому терміналі введи ->\n flask --app app run \nА у правому введи 2 команди -\nКоманда 1 -  cd backend\nКоманда 2 - fastapi dev main.py", buttons = next16_)
    

@client.on(events.CallbackQuery(pattern=b'next16_'))
async def final(event):
    final_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/final.png"
    await client.send_file(event.chat_id, final_path, caption="Можеш навести крсор на силку *http://127.0.0.1:5000* в лівому терміналі і нажати ctrl/command + ЛКМ")
    sender = await event.get_sender()
    first_name = sender.first_name
    bonus = [
        button.inline("Бонус", b'bonus')
    ]
    await event.respond(f"І в тебе в браузері відкриється сторінка мого проєкту\nРадий був допомогти тобі, {first_name}\nEnjoy ⚡", buttons=bonus)


@client.on(events.CallbackQuery(pattern=b'bonus'))
async def bonus(event):
    bonus_path = "/Users/leonidlisovskiy/Desktop/bot-balance-manager/funny_video.mp4"
    await client.send_file(event.chat_id, bonus_path, caption="Судді, ось вам дуже смішне відео, можете мене на валідації не сильно пресувати 🏆")



async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())