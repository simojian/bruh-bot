# bruh-bot
This a very simple discord bot that has the ability to ***curse*** somebody by joining their voice chat in random intervals joins their voice channel, says "bruh" and leaves.
### Requirements:
Because of how i'm handling the playing of the "bruh" it requires FFmpeg for it to run.
### The Commands:
1. `&curse <@Member>` -
The very base of this bot, requires a member as an argument and *marks* them causing the bot to join the voice channel where the member is currently and says loudly "bruh" after which it leaves, this process is repeated in random intervals from 5 seconds to 15 minutes untill someone else has been cursed or the `&cleanse` command is used.
2. `&curseEvil <@Member>` -
Just the same as `&curse` however the interval is reduced to 5 to 15 seconnds for added cruelty. This is a bot owner only command. Please note your friends will hate you if you use it.
3. `&cleanse` -
Removes the *curse* from the currently afflicted member, meaning that the bot will stop joining their voice channels. This command is only usable by members with Administrator permissions.
4. `&ayy` -
Simple "ping" command used for making sure that the bot is online by responding with `@commandAuthor lmao`.
5. `&kill` -
Shuts down the bot. Bot owner only.
6. `&testBruh` -
Old command that was used for debugging and testing. Can be used to test if the bot can connect to a voice channel. Bot owner only.
7. `&forceLeave` -
Causes the bot to leave the current voice channel, meant for use in case it for whatever reason doesn't leave a voice channel after a "bruh". Bot owner only.

This bot doesn't have a lot of functionallity however, it can be fun (for the user maybe not so much for the cursed)
Feel free to use and edit to your hearts content!

Made by: Simojian
