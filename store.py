
def store(names):
    #TODO : Log Entry Exits Seperately.

    per_name = ' '
    
    for name in names:
        if per_name != name:
            if name != 'Unknown' or name != 'Suspect':
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                try:
                    os.mkdir('faces/' + name + '/' + str(datetime.date.today()))
                except:
                    pass
                dest = 'faces/' + name + '/' + str(datetime.date.today()) + '/' + str(current_time) + '.avi'
                shutil.copyfile('output.avi',dest)
            else: #save unknown entries...
                 now = datetime.datetime.now()
                 current_time = now.strftime("%H:%M:%S")
                 dest = 'unknownDetected/' + str(datetime.date.today()) + '_' +  str(current_time) + '.avi'
    
                 shutil.copyfile('output.avi',dest)
            print('\n\t' + name + ' Video Logged...')
        per_name = name

    print('All names ',*names)

    #TODO : Create a new log for unknown persons with their respective video file name.'Enhancement #1'


