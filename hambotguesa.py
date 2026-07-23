import discord
from discord.ext import commands

intents = discord.Intents.default
intents.message_content = True

hambotguesa = commands.Bot(command_prefix="_", intents=intents)

#eventos
@hambotguesa.event
async def on_ready():
    print(f"Bot en linea ve a discordias")

#comandos
@hambotguesa.event
async def check(ctx):
    await ctx.send("por favor manda una imagen para analizar")

    def verificar(mensaje):
        return mensaje.author == ctx.author and len(mensaje.attachments) > 0
    
    try:
        mensaje = await hambotguesa.wait_for("message", check=verificar, timeout=60)
        imagen = mensaje.attachments[0]
        await imagen.save(f"img/{imagen.filename}")
        await ctx.send("imagen recibida y guardada para ser analizada")
    except:
         await ctx.send("Por favor enviar mensaje con una imagen para analizar, recuerda que tienes 60 segundos.")

hambotguesa.run("MTUyNzgwMzgyMzM0NTc2NjU5Mg.GabaYV.ikrBkbLoITj2N4YbA4MBiUGBVuZkd6Gnu11H2EMTUyNzgwMzgyMzM0NTc2NjU5Mg.GabaYV.ikrBkbLoITj2N4YbA4MBiUGBVuZkd6Gnu11H2E")

    