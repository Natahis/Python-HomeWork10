from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import MessageHandler,filters
key_bot="5614665038:AAGSzdum2vXAf-VYyEcpwUs4zaeUh4kR0Jo"
help_info="/hello\n"

def hello(update, context ) :
  return f"Hello {update.effective_user.first_name}"

async def filters_handler(update, context):
    x=update.message
    if x==None:
        x=update.edited_message#print("==========изменение\n") 

    if x.entities==[] or (not x.text[0]=='/'):# текст не содержащий команду
        print(" выводится введенный обычный текст,\nкоторый можно использовать в своих целях",x.text)

    else:# содержит символ /, т.е. команду или набор
        com=list(map(str, x.text.split('\n')))
        if len(com)>1:# если вдруг больше
            await context.bot.send_message(
                            chat_id=update.effective_chat.id, 
                            text="одна команда расположена более чем на одной строке?!!\n\n"+help_info)
            return

        com=list(map(str, com[0].split(' ')))# разбор предложения после команды
 
        if com[0] in help_info:#основной набор команд!!!!
            print(com[0])
            
            # обработка команды /hello
            if com[0]=="/hello":
                t=hello(update, context)
                await context.bot.send_message(chat_id=update.effective_chat.id, 
                            text=t)
            return
                
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Извините!Не понимаю команду! "+com[0]+"\n набор правильных команд бла бла\n\n"+help_info)

app = ApplicationBuilder().token(key_bot).build()
app.add_handler(MessageHandler(filters.TEXT, filters_handler))
app.run_polling()