from django.core.mail import send_mail
from django.db import models
import telepot


class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 8 :
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, ' Attention, quelque chose ne va pas bien dans votre machine. Veuillez la réparer immédiatement. Température =  ' + str(self.temp))
            print(bot.sendMessage(rece_id, ' Attention, quelque chose ne va pas bien dans votre machine. Veuillez la réparer immédiatement. Température = ' + str(self.temp)))
            send_mail(
                'Temperature sévère !!',
                'Attention, quelque chose ne va pas bien dans votre machine. Veuillez la réparer immédiatement. Température = ' + str(self.temp),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        elif self.temp < 2 :
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, ' depassement de la temperature : ' + str(self.temp))
            print(bot.sendMessage(rece_id,' Attention, quelque chose ne va pas bien dans votre machine. Veuillez la réparer immédiatement. Température crtique = ' + str(self.temp)))
            send_mail(
                'Temperature critique !!',
                'Attention, quelque chose ne va pas bien dans votre machine. Veuillez la réparer immédiatement. Température critique = ' + str(self.temp),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)
