my_dict = {}

class MusicPlayer():
    def __init__(self):
        pass
    
    def welcome(self):
        print("Welcome to the music player")
       
    class Song():
        def __init__(self,name,artist,lyrics):
            self.name = name
            self.artist = artist
            self.lyrics = lyrics
            self.add_song()      

        # def show_lyrics(self):
        #     print(self.lyrics) 

        def __str__(self):
            return  f"{self.name} by {self.artist}"

        def add_song(self):
            if self.artist not in my_dict.keys():
                my_dict[self.artist] = {}
                my_dict[self.artist][self.name]=self.lyrics  
            else:
                my_dict[self.artist][self.name] = self.lyrics    

    first = Song("Levitating", "Dua Lipa", '''
[Verse 1]
If you wanna run away with me, I know a galaxy
And I can take you for a ride
I had a premonition that we fell into a rhythm
Where the music don't stop for life
Glitter in the sky, glitter in my eyes
Shining just the way I like
If you're feeling like you need a little bit of company
You met me at the perfect time

[Pre-Chorus]
You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
Yeah, yeah, yeah, yeah, yeah

[Chorus]
I got you, moonlight, you're my starlight
I need you all night, come on, dance with me
I'm levitating
You, moonlight, you're my starlight (You're the moonlight)
I need you all night, come on, dance with me
I'm levitating

[Verse 2]
I believe that you're for me, I feel it in our energy
I see us written in the stars
We can go wherever, so let's do it now or never
Baby, nothing's ever, ever too far
Glitter in the sky, glitter in our eyes
Shining just the way we are
I feel like we're forever every time we get together
But whatever, let's get lost on Mars
[Pre-Chorus]
You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
Yeah, yeah, yeah, yeah, yeah

[Chorus]
I got you, moonlight, you're my starlight
I need you all night, come on, dance with me
I'm levitating
You, moonlight, you're my starlight (You're the moonlight)
I need you all night, come on, dance with me
I'm levitating

[Post-Chorus]
You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
Yeah, yeah, yeah, yeah, yeah
I'm levitating (Woo)
You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
Yeah, yeah, yeah, yeah, yeah (Woo)

[Bridge]
My love is like a rocket, watch it blast off
And I'm feeling so electric, dance my ass off
And even if I wanted to, I can't stop
Yeah, yeah, yeah, yeah, yeah
My love is like a rocket, watch it blast off
And I'm feeling so electric, dance my ass off
And even if I wanted to, I can't stop
Yeah, yeah, yeah, yeah, yeah
[Pre-Chorus]
You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading

[Chorus]
I got you (Yeah), moonlight, you're my starlight
I need you all night (All night), come on, dance with me
I'm levitating (Woo)

[Post-Chorus]
You can fly away with me tonight (Tonight)
You can fly away with me tonight
Baby, let me take you for a ride
Yeah, yeah, yeah, yeah, yeah (Take you for a ride)
I'm levitating (Woo)
You can fly away with me tonight (Tonight)
You can fly away with me tonight
Baby, let me take you for a ride
Yeah, yeah, yeah, yeah, yeah (Let me take you for a ride)

[Chorus]
I got you, moonlight, you're my starlight (You are my starlight)
I need you all night, come on, dance with me (Come on, dance with me)
I'm levitating
You, moonlight, you're my starlight (You're the moonlight)
I need you all night, come on, dance with me
I'm levitating''')        

    second = Song("Save Your Tears", "The Weeknd", '''
[Intro: The Weeknd & Ariana Grande]
Ooh (Ooh)
Na-na, yeah

[Verse 1: The Weeknd]
I saw you dancing in a crowded room (Uh)
You look so happy when I'm not with you
But then you saw me, caught you by surprise
A single teardrop falling from your eye

[Refrain: The Weeknd & Ariana Grande]
I don't know why I run away (Oh)
I make you cry when I run away (Oh)

[Pre-Chorus: The Weeknd]
Take me back 'cause I wanna stay
Save your tears for another

[Chorus: The Weeknd & Ariana Grande]
Save your tears for another day (Oh)
Save your tears for another day (Mm)

[Verse 2: Ariana Grande]
Met you once under a Pisces moon
I kept my distance 'cause I know that you
Don't like when I'm with nobody else
I couldn't help it, I put you through hell
[Refrain: Ariana Grande]
I don't know why I run away, oh boy (Run away, oh yeah; oh)
I make you cry when I run away (Away, oh; oh)

[Pre-Chorus: Ariana Grande]
Boy, take me back 'cause I wanna stay
Save your tears for another
I realize that it's much too late
And you deserve someone better

[Chorus: Ariana Grande]
Save your tears for another day (Oh)
Save your tears for another day (Oh)

[Refrain: Both, Ariana Grande]
(Bum, bum, bum, bum, bum)
I don't know why I run away (Oh)
(Bum, bum, bum, bum, bum)
I make you cry when I run away (Save)

[Chorus: Both, Ariana Grande & The Weeknd]
Save your tears for another day (Ooh; oh)
Ooh, girl, I said (Okay)
Save (Save) your (Your) tears for another day (Oh yeah, yeah; oh)

[Outro: The Weeknd & Both]
Save your tears for another day (Oh)
Save your tears for another day (Oh)
Save your tears for another day''')        

    third = Song("Blinding Lights", "The Weeknd", '''
    [Intro]
Yeah

[Verse 1]
I've been tryna call
I've been on my own for long enough
Maybe you can show me how to love, maybe
I'm going through withdrawals
You don't even have to do too much
You can turn me on with just a touch, baby

[Pre-Chorus]
I look around and
Sin City's cold and empty (Oh)
No one's around to judge me (Oh)
I can't see clearly when you're gone

[Chorus]
I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch
I said, ooh, I'm drowning in the night
Oh, when I'm like this, you're the one I trust
Hey, hey, hey

[Verse 2]
I'm running out of time
'Cause I can see the sun light up the sky
So I hit the road in overdrive, baby, oh
[Pre-Chorus]
The city's cold and empty (Oh)
No one's around to judge me (Oh)
I can't see clearly when you're gone

[Chorus]
I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch
I said, ooh, I'm drowning in the night
Oh, when I'm like this, you're the one I trust

[Bridge]
I'm just calling back to let you know (Back to let you know)
I could never say it on the phone (Say it on the phone)
Will never let you go this time (Ooh)

[Chorus]
I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch
Hey, hey, hey
Hey, hey, hey

[Outro]
I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch''')   

    fourth = Song("Mood", "24kGoldn", '''
    [Intro: 24kGoldn]
Oh-oh-oh
Yeah, yeah, yeah, yeah (Yeah)

[Chorus: 24kGoldn]
Why you always in a mood? Fuckin' 'round, actin' brand new
I ain't tryna tell you what to do, but try to play it cool
Baby, I ain't playing by your rules
Everything look better with a view
Why you always in a mood? Fuckin' 'round, actin' brand new
I ain't tryna tell you what to do, but try to play it cool
Baby, I ain't playing by your rules
Everything look better with a view, yeah

[Verse 1: iann dior]
I could never get attached
When I start to feel, I unattach
Somehow I always end up feeling bad
Baby, I am not your dad, it's not all you want from me
I just want your company
Girl, it's obvious, elephant in the room
And we're a part of it, don't act so confused
And you love startin' it, now I'm in a mood
Now we arguin' in my bedroom

[Pre-Chorus: iann dior]
We play games of love to avoid the depression
We been here before and I won't be your victim
[Chorus: 24kGoldn]
Why you always in a mood? Fuckin' 'round, actin' brand new
I ain't tryna tell you what to do, but try to play it cool
Baby, I ain't playing by your rules
Everything look better with a view
Why you always in a mood? Fuckin' 'round, actin' brand new
I ain't tryna tell you what to do, but try to play it cool
Baby, I ain't playing by your rules
Everything look better with a view

[Verse 2: 24kGoldn]
So why you tryin' to fake your love on the regular
When you could be blowin' up just like my cellular?
I won't ever let a shorty go and set me up
Only thing I need to know is if you wet enough
I'm talking slick back, kick back, gang sippin' fourties
You keep playin', not another day with you, shorty
Mismatched fits, that was way before you know me
Got a lot of love, well, you better save it for me

[Pre-Chorus: iann dior, iann dior & 24kGoldn]
We play games of love to avoid the depression
We been here before and I won't be your victim

[Chorus: 24kGoldn]
Why you always in a mood? Fuckin' 'round, actin' brand new
I ain't tryna tell you what to do, but try to play it cool
Baby, I ain't playing by your rules
Everything look better with a view
Why you always in a mood? Fuckin' 'round, actin' brand new
I ain't tryna tell you what to do, but try to play it cool
Baby, I ain't playing by your rules
Everything look better with a view, yeah''') 

    fifth = Song("Good 4 U", "Olivia Rodrigo", '''
    [Intro]
(Ah)

[Verse 1]
Well, good for you, I guess you moved on really easily
You found a new girl and it only took a couple weeks
Remember when you said that you wanted to give me the world?
(World)
And good for you, I guess that you've been workin' on yourself
I guess that therapist I found for you, she really helped
Now you can be a better man for your brand new girl (Girl)

[Chorus]
Well, good for you
You look happy and healthy, not me
If you ever cared to ask
Good for you
You're doin' great out there without me, baby
God, I wish that I could do that
I've lost my mind, I've spent the night
Cryin' on the floor of my bathroom
But you're so unaffected, I really don't get it
But I guess good for you

[Verse 2]
Well, good for you, I guess you're gettin' everything you want (Ah)
You bought a new car and your career's really takin' off (Ah)
It's like we never even happened
Baby, what the fuck is up with that? (Ah)
And good for you, it's like you never even met me
Remember when you swore to God I was the only
Person who ever got you? Well, screw that, and screw you
You will never have to hurt the way you know that I do
[Chorus]
Well, good for you
You look happy and healthy, not me
If you ever cared to ask
Good for you
You're doin' great out there without me, baby
God, I wish that I could do that
I've lost my mind, I've spent the night
Cryin' on the floor of my bathroom
But you're so unaffected, I really don't get it
But I guess good for you

[Break]
(Ah-ah-ah-ah)
(Ah-ah-ah-ah)

[Bridge]
Maybe I'm too emotional
But your apathy's like a wound in salt
Maybe I'm too emotional
Or maybe you never cared at all
Maybe I'm too emotional
Your apathy is like a wound in salt
Maybe I'm too emotional
Or maybe you never cared at all
[Chorus]
Well, good for you
You look happy and healthy, not me
If you ever cared to ask
Good for you
You're doin' great out there without me, baby
Like a damn sociopath
I've lost my mind, I've spent the night
Cryin' on the floor of my bathroom
But you're so unaffected, I really don't get it
But I guess good for you

[Outro]
Well, good for you, I guess you moved on really easily''')   

    sixth = Song("Kiss Me More", "Doja Cat", '''
    [Verse 1: Doja Cat]
We hug and, yes, we make love
And always just say goodnight (La-la-la-la-la-la)
And we cuddle, sure, I do love it
But I need your lips on mine

[Chorus: Doja Cat]
Can you kiss me more?
We're so young, boy, we ain't got nothin' to lose, uh-oh
It's just principle
Baby, hold me 'cause I like the way you groove, uh-oh

[Post-Chorus: Doja Cat]
Boy, you write your name, I can do the same
Oh, I love the taste, la-la-la-la-la-la
All on my tongue, I want it (La-la-la-la-la-la)
Boy, you write your name, I can do the same
Oh, I love the taste, la-la-la-la-la-la
All on my tongue, I want it (La-la-la-la-la-la)

[Verse 2: Doja Cat]
I, I feel like fuckin' somethin'
But we could be corny, fuck it
Sugar, I ain't no dummy, dummy
I likе to say, "What if?", but if
We could kiss and just cut the rubbish
Then I might bе onto somethin'
I ain't givin' you one in public
I'm givin' you hundreds, fuck it
Somethin' we just gotta get into
Sign first, middle, last on the wisdom tooth
Niggas wishin' that the pussy was a kissin' booth
Taste breakfast, lunch, and gin and juice
And that dinner just like dessert too
And when we French, refresh, gimme two
When I bite that lip, come get me too
He want lipstick, lip gloss, hickeys too, huh
[Chorus: Doja Cat]
Can you kiss me more?
We're so young, boy, we ain't got nothin' to lose, uh-oh
It's just principle
Baby, hold me 'cause I like the way you groove, uh-oh

[Post-Chorus: Doja Cat]
Boy, you write your name, I can do the same
Oh, I love the taste, la-la-la-la-la-la
All on my tongue, I want it (La-la-la-la-la-la)
Boy, you write your name, I can do the same
Oh, I love the taste, la-la-la-la-la-la
All on my tongue, I want it

[Verse 3: SZA]
Say give me a buck, need that gushy stuff
Push the limit, no, you ain't good enough
All your niggas say that you lost without me
All my bitches feel like I dodged the county
Fuckin' with you feel like jail, nigga (Feel like jail)
I can't even exhale, nigga (Exhale)
Pussy like holy grail, you know that
You gon' make me need bail, you know that
Caught dippin' with your friend
You ain't even half man, lyin' on your—, you know that
Got me a bag full of brick, you know that
Control, don't slow the pace if I throw back
All this ass for real (All this ass)
Drama make you feel (Make you feel)
Fantasy and whip appeal is all I can give you
[Chorus: Doja Cat, SZA & Both]
Can you kiss me more?
We're so young, boy, we ain't got nothin' to lose, uh-oh
It's just principle
Baby, hold me 'cause I like the way you groove, uh-oh
Oh, darlin'

[Post-Chorus: SZA & Doja Cat]
Boy, you write your name, I can do the same
Ooh, I love the taste, oh-la-la-la-la-la
All on my tongue, I want it
Boy, you write your name, I can do the same
Ooh, I love the taste, oh-la-la-la-la-la
All on my tongue, I want it''')   

    seventh = Song("Leave The Door Open", "Silk Sonic", '''
    [Intro: Bruno Mars]
Say baby, say baby, say baby

[Verse 1: Anderson .Paak & Bruno Mars]
What you doin'? (What you doin'?)
Where you at? (Where you at?)
Oh, you got plans? (You got plans)
Don't say that (Shut your trap)
I'm sippin' wine (Sip, sip) in a robe (Drip, drip)
I look too good (Look too good)
To be alone (Woo, woo)
My house clean (House clean), my pool warm (Pool warm)
Just shaved, smooth like a newborn
We should be dancin', romancin'
In the east wing and the west wing
Of this mansion, what's happenin'?

[Pre-Chorus: Bruno Mars]
I ain't playin' no games
Every word that I say is coming straight from the heart
So if you tryna lay in these arms

[Chorus: Bruno Mars]
I'ma leave the door open
(I'ma leave the door open)
I'ma leave the door open, girl
(I'ma leave the door open, hopin')
That you feel the way I feel
And you want me like I want you tonight, baby
(Tell me that you're comin' through)
[Verse 2: Anderson .Paak & Bruno Mars]
Ooh, you're so sweet (So sweet), so tight (So tight)
I won't bite (Uh-uh), unless you like (Unless you like)
If you smoke (What you smoke?), I got the haze (Purple haze)
And if you're hungry, girl, I got filets (Woo)
Ooh, baby, don't keep me waitin'
There's so much love we could be makin' (Shamone!)
I'm talkin' kissin', cuddlin'
Rose petals in the bathtub
Girl, let's jump in, it's bubblin'

[Pre-Chorus: Bruno Mars]
I ain't playin' no games
Every word that I say is coming straight from the heart
So if you tryna lay in these arms (If you tryna lay in these arms)

[Chorus: Bruno Mars]
I'ma leave the door open
(I'ma leave the door open)
I'ma leave the door open, girl
(I'ma leave the door open, hopin')
That you feel the way I feel
And you want me like I want you tonight, baby
Tell me that you're comin' through (Come on, girl)

[Bridge: Bruno Mars & Anderson .Paak]
La-la-la-la-la-la-la (I need you, baby)
La-la-la-la-la-la-la (I got to see you, baby)
La-la-la-la-la-la-la (Girl, I'm tryna give you this, ah)
[Chorus: Bruno Mars]
Hey, hey, I'ma leave my door open, baby
(I'ma leave the door open)
I'ma leave, I'ma leave my door open, girl
(I'ma leave the door open, hopin')
And I'm hopin', hopin'
That you feel the way I feel
And you want me like I want you tonight, baby
Tell me that you're comin' through (Woo!)

[Outro: Bruno Mars & Anderson .Paak]
La-la-la-la-la-la-la (Tell me)
Tell me that you're comin' through
(Woo-woo-woo-woo, woo-woo-woo, woo-woo-woo)
(Woo-woo-woo-woo, woo-woo-woo, woo-woo)
La-la-la-la-la-la-la (La-la-la-la-la)
Tell me that you're comin' through
Girl, I'm here just waitin' for you (Oh!)
Come on over, I'll adore you (I gotta know!)
La-la-la-la-la-la-la (I'm waitin', waitin', waitin')
Tell me that you're comin' through (For you)
Girl, I'm here just waitin' for you
Come on over, I'll adore you
La-la-la-la-la-la-la (La-la-la-la)''')   

    eight = Song("Drivers License", "Olivia Rodrigo", '''
    [Verse 1]
I got my driver's license last week
Just like we always talked about
'Cause you were so excited for me
To finally drive up to your house
But today, I drove through the suburbs
Crying 'cause you weren't around

[Verse 2]
And you're probably with that blonde girl
Who always made me doubt
She's so much older than me
She's everything I'm insecure about
Yeah, today, I drove through the suburbs
'Cause how could I ever love someone else?

[Chorus]
And I know we weren't perfect
But I've never felt this way for no one
And I just can't imagine
How you could be so okay now that I'm gone
Guess you didn't mean what you wrote in that song about me
'Cause you said forever, now I drive alone past your street

[Verse 3]
And all my friends are tired
Of hearing how much I miss you, but
I kinda feel sorry for them
'Cause they'll never know you the way that I do
Yeah, today, I drove through the suburbs
And pictured I was driving home to you
[Chorus]
And I know we weren't perfect
But I've never felt this way for no one, oh
And I just can't imagine
How you could be so okay now that I'm gone
I guess you didn't mean what you wrote in that song about me
'Cause you said forever, now I drive alone past your street

[Bridge]
Red lights, stop signs
I still see your face in the white cars, front yards
Can't drive past the places we used to go to
'Cause I still fuckin' love you, babe (Ooh, ooh-ooh, ooh, ooh-ooh)
Sidewalks we crossed
I still hear your voice in the traffic, we're laughing
Over all the noise
God, I'm so blue, know we're through
But I still fuckin' love you, babe (Ooh, ooh-ooh, ooh, ooh-ooh)

[Chorus]
I know we weren't perfect
But I've never felt this way for no one
And I just can't imagine
How you could be so okay now that I'm gone
Guess you didn't mean what you wrote in that song about me
'Cause you said forever, now I drive alone past your street
[Outro]
Yeah, you said forever, now I drive alone past your street''')   

    ninth = Song("Montero(Call Me By Your Name)", "Lil Nas X", """
    I caught it bad yesterday
You hit me with a call to your place
Ain't been out in a while anyway
Was hopin' I could catch you throwin' smiles in my face
Romantic talkin'? You don't even have to try
You're cute enough to fuck with me tonight
Lookin' at the table, all I see is weed and white
Baby, you livin' the life, but nigga, you ain't livin' right

[Pre-Chorus]
Cocaine and drinkin' with your friends
You live in the dark, boy, I cannot pretend
I'm not fazed, only here to sin
If Eve ain't in your garden, you know that you can

[Chorus]
Call me when you want, call me when you need
Call me in the morning, I'll be on the way
Call me when you want, call me when you need
Call me out by your name, I'll be on the way like

[Post-Chorus]
Mmm, mmm, mmm
Mmm, mmm, mmm
[Verse 2]
Ayy, ayy
I wanna sell what you're buyin'
I wanna feel on your ass in Hawaii
I want that jet lag from fuckin' and flyin'
Shoot a child in your mouth while I'm ridin'
Oh, oh, oh, why me?
A sign of the times every time that I speak
A dime and a nine, it was mine every week
What a time, an incline, God was shinin' on me
Now I can't leave
And now I'm actin' hella elite
Never want the niggas that's in my league
I wanna fuck the ones I envy, I envy

[Pre-Chorus]
Cocaine and drinkin' with your friends
You live in the dark, boy, I cannot pretend
I'm not fazed, only here to sin
If Eve ain't in your garden, you know that you can

[Chorus]
Call me when you want, call me when you need
Call me in the morning, I'll be on the way
Call me when you want, call me when you need
Call me out by your name, I'll be on the way like
[Post-Chorus]
Oh, call me by your name (Mmm, mmm, mmm)
Tell me you love me in private
Call me by your name (Mmm, mmm, mmm)
I do not care if you're lyin'""")  

    tenth = Song("Peaches", "Justin Bieber", '''
    [Chorus: Justin Bieber]
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
I get my light right from the source, yeah (Yeah, that’s it)

[Verse 1: Justin Bieber]
And I say, oh (Oh)
The way I breathe you in (In)
It's the texture of your skin
I wanna wrap my arms around you, baby
Never let you go, oh
And I say, oh
There's nothing like your touch
It’s the way you lift me up, yeah
And I'll be right here with you 'til the end of time

[Chorus: Justin Bieber]
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
I get my light right from the source, yeah (Yeah, that's it)

[Verse 2: Daniel Caesar]
You ain't sure yet
But I'm for ya
All I can want, all I can wish for
Nights alone that we miss more
And days we save as souvenirs
There's no time, I wanna make more time
And give you my whole life
I left my girl, I’m in Mallorca
Hate to leave her, call it torture
Remember when I couldn’t hold her
Left her baggage for Rimowa
[Chorus: Justin Bieber]
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
I get my light right from the source, yeah (Yeah, that’s it)

[Verse 3: GIVĒON]
I get the feeling, so I'm sure (Sure)
Hand in my hand because I'm yours, I can't
I can’t pretend, I can't ignore, you're right for me
Don't think you wanna know just where I've been, oh
Done bein' distracted
The one I need is right in my arms (Oh)
Your kisses taste the sweetest with mine
And I'll be right here with you 'til the end of time

[Chorus: Justin Bieber]
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
I get my light right from the source, yeah (Yeah, that's it)
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
(I get my light right from the source, yeah, yeah, that's it)
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
I get my light right from the source, yeah (Yeah, that's it)
I got my peaches out in Georgia (Oh, yeah, shit)
I get my weed from California (That's that shit)
I took my chick up to the North, yeah (Badass bitch)
I get my light right from the source, yeah (Yeah, that's it)''')   
    # print(my_dict)
        
    def show_songs(self):   
        print("Welcome, please select a select a song from the top 10 songs of 2021:\r\n")
        # print(my_dict)
        for key,value in my_dict.items():
            for keyitem,valueitem in value.items():
                print(f"{keyitem} by {key}")
        self.show_lyrics()      
          
    def show_lyrics(self):            
        selection = input("\r\nEnter artist name followed by song name separated by a dash and a space OR Enter an artist name to choose from their songs:\r\n").title() 
        selection_list = selection.split('- ')
        if len(selection_list) == 2:
            if selection_list[0] in my_dict.keys():
                if selection_list[1] in my_dict[selection_list[0]]:
                    print(f"You chose {selection_list[1]} by {selection_list[0]}. Here you go:\r\n{my_dict[selection_list[0]][selection_list[1]]}")
        elif len(selection_list) == 1:
            if selection_list[0] in my_dict.keys():
                print(f"\r\nHere are songs by {selection_list[0]}:")
                for i in my_dict[selection_list[0]].keys():
                    print(f"{i}")
                selection = input("\r\nEnter the name of the song you want lyrics to:\r\n").title() 
                if selection in my_dict[selection_list[0]]:
                    print(f"You chose {selection} by {selection_list[0]}. Here you go:\r\n{my_dict[selection_list[0]][selection]}")
        while True:            
            star = input("Press * to choose again or e to exit:\r\n").lower()
            if star == '*':
                self.show_songs()
                self.show_lyrics()
                break
            elif star == 'e':
                break    


a = MusicPlayer()
a.show_songs()            



