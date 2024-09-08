from pytimeparse import parse
import ptbot
import os
import random


TG_TOKEN = os.getenv('TG_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')


def notify_progress(secs_left, id, forward_id, val_bar):
    val_progressbar = render_progressbar(val_bar, val_bar-secs_left)
    new_message = "Осталось {} сек\n".format(secs_left) + val_progressbar
    bot.update_message(forward_id, id, new_message)


def choose(forward_id, forward_answer):
    final_message = "Время вышло!"
    bot.send_message(forward_id, final_message)


def wait(chat_id, question):
    message_id = bot.send_message(chat_id, "Запускаю таймер")
    bot.create_countdown(parse(question), notify_progress, val_bar=parse(question), id=message_id, forward_id=chat_id)
    bot.create_timer(parse(question), choose, forward_id=chat_id, forward_answer=question)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    bot = ptbot.Bot(TG_TOKEN)
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(wait)
    bot.run_bot()