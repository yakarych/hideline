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


instruction = """1. Скачай и установи на устройство приложение Outline:

<b>iOS:</b> https://itunes.apple.com/app/outline-app/id1356177741
<b>macOS:</b> https://itunes.apple.com/app/outline-app/id1356178125
<b>Windows:</b> https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe
<b>Linux:</b> https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage
<b>Android:</b> https://play.google.com/store/apps/details?id=org.outline.android.client
<b>Дополнительная ссылка для Android:</b> https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk

<b>2.</b> Скопируй купленный ключ. Никому его не сообщай (вообще никому).

<b>3.</b> Открой клиент Outline. Если твой ключ доступа определился автоматически, нажми "Подключиться". Если этого не произошло, вставь ключ в поле и нажмите "Подключиться".

Теперь у тебя есть доступ к свободному интернету. Чтобы убедиться, что ты подключился к серверу, введи в Google Поиске фразу "Какой у меня IP-адрес". IP-адрес, указанный в Google, должен совпадать с IP-адресом в клиенте Outline.

Дополнительные сведения можно найти на странице https://getoutline.org/."""
