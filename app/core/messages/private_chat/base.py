from aiogram.utils.markdown import hbold as bold


def welcome(user_firstname: str) -> str:
    """
    :param user_firstname:
    :return: welcome message to user
    """

    return bold(f'Привет, {user_firstname}!') + \
        f"\n\n<b><i>Hideline</i></b> — полностью автоматизированный VPN-менеджер. Построен на технологии Outline, " \
        f"созданной инициативными разработчиками из Google.\n\n" \
        f"\nАвтор проекта: @Karych."


instruction = """<b>1.</b> Скачай и установи на устройство приложение Outline:

<b>iOS:</b> https://itunes.apple.com/app/outline-app/id1356177741
<b>macOS:</b> https://itunes.apple.com/app/outline-app/id1356178125
<b>Windows:</b> https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe
<b>Linux:</b> https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage
<b>Android:</b> https://play.google.com/store/apps/details?id=org.outline.android.client
<b>Дополнительная ссылка для Android:</b> https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk

<b>2.</b> Скопируй купленный ключ. Если не купил, нажми на кнопку "Создать Ключ."

<b>3.</b> Открой клиент Outline. Если твой ключ доступа определился автоматически, нажми "Подключиться". Если этого не произошло, вставь ключ в поле и нажмите "Подключиться".

Теперь у тебя есть доступ к свободному интернету. Чтобы убедиться, что ты подключился к серверу, введи в Google Поиске фразу "Какой у меня IP-адрес". IP-адрес, указанный в Google, должен совпадать с IP-адресом в клиенте Outline.

Дополнительные сведения можно найти на странице https://getoutline.org/."""

keys_description = "<b>Ключи</b>\n\nКлюч — один коннекшен к ВПН.\nТы можешь использовать его на разных " \
                   "устройствах, но не одновременно. <i>То есть на одном устройстве включил VPN, на другом выключил.</i>\n\n" \
                   "\nПокупается ключ навсегда (пока живет проект). Гарантирую работоспособность до 01.03.2023.\n" \
                   "Ограничение на ключ: 30гб трафика в месяц. Каждый месяц трафик обнуляется.\n" \
                   "Покупать ключи ты можешь любое количество раз.\n\nОплата через сервис Яндекса Yoomoney."
keys_description_2 = "Выбери количество ключей и оплати.\nВ течение 30 секунд после оплаты ключ будет сгенерирован и отправлен.\n\n" \
                     "В случае непредвиденной ошибки пиши в ЛС: @Karych. Я помогу решить все проблемы. " \
                     "Если ключ не придет — создам вручную или верну деньги. На твоё усмотрение.\n\nВыбери количество ключей:"
