import time

replay_lyrics = [
      'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Remember the first time we met', 'You was at the mall with your friends', 'I was scared to approach ya', 'But then you came closer', 'Hopin\' you would give me a chance', 'Who would have ever knew', 'That we would ever be more than friends', 'We\'re real worldwide', 'breakin all the rules', 'She like a song played again and again', 'That girl', 'like somethin off a poster', 'That girl', 'is a dime they say', 'That girl', 'is a gun to my holster', 'She\'s runnin through my mind all day', 'ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'See you been all around the globe', 'Not once did you leave my mind', 'We talk on the phone', 'from night til the morn', 'Girl you really change my life', 'Doin things I never do', 'I\'m in the kitchen cookin things she likes', 'We\'re real worldwide', 'breakin all the rules', 'Someday I wanna make you my wife', 'That girl', 'like somethin off a poster', 'That girl', 'is a dime they say', 'That girl', 'is the gun to my holster', 'She\'s runnin through my mind all day', 'ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'I can be your melody, A girl that could write you a symphony', 'The one that could fill your fantasies', 'So come baby girl let\'s sing with me', 'Ay', 'I can be your melody', 'A girl that could write you a symphony', 'The one that could fill your fantasies', 'So come baby girl let\'s sing with me', 'Ay', 'na na na na na na na', 'Na na na na na na', 'Shawty got me singin', 'Na na na na na na na', 'Na na na na na na na', 'Now she got me singin', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay'
    ]

print('Microsoft Windows [Version 10.0.17763.1217]\n(c) 2018 Microsoft Corporation. All rights reserved.\n\n')

while True:
    answer = input('C:\\Users\\gavin>')

    # Shawty Command
    if answer == 'run shawty':
        for i in replay_lyrics:
            print(i)
            time.sleep(1.5)

    # cd Command
    elif answer == 'cd':
        print('C:\\Users\\gavin\n')

    # cmd Command
    elif answer == 'cmd':
        print('Microsoft Windows [Version 10.0.17763.1217]\n(c) 2018 Microsoft Corporation. All rights reserved.\n')

    # does absolutley nothing if you just give no input
    elif answer.strip() == '':
        pass

    # cd Command
    elif answer == 'fuck off':
        print('no u')


    # breaks while loop
    elif answer == 'close':
        break

    # error message
    else:
        print(f'\'{answer}\' is not recognized as an internal or external command,\noperable program or batch file.\n')
