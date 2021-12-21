импорт  ОС
 случайный импорт
импортный  шутил
req_main  =  ''
req  =  ''
sec_req  =  ''

мусор  =  len ( os . getcwd ())
user_dir_lock  =  мусор
мусор  =  0
opeSys  =  os . название

def  separating_reqest ( запрос ):
    глобальный  req_main
    глобальный  запрос
    глобальный  sec_req
    req_array  = []
    запрос  =  запрос . lstrip ()
    fname  =  запрос . сплит ( '"' )
    req_array  =  запрос . разделить ( '' )
    печать ( имя_файла )
    если  len ( req_array ) ==  2 :
        req_main  =  req_array [ 0 ]
        req  =  req_array [ 1 ]
        печать ( req_array )
        печать ( req_main , req )
    elif  len ( req_array ) ==  1 :
        req_main  =  req_array [ 0 ]
        печать ( req_main )
    elif  len ( req_array ) ==  3 :
        req_main  =  req_array [ 0 ]
        req  =  req_array [ 1 ]
        sec_req  =  req_array [ 2 ]
        печать ( req_array )
        печать ( req_main , req , sec_req )
    elif  len ( req_array ) > =  4 :
        req_main  =  req_array [ 0 ]
        req  =  req_array [ 1 ]
        sec_req  =  имя_файла [ 1 ]
        печать ( sec_req )
def  cur_dir ():
    full_path  =  os . getcwd ()
    cur_path  =  полный_путь . разделить ( ' \\ ' )
    pwd  =  cur_path [ len ( cur_path ) - 1 ]
    печать ( pwd , ' \ n ' )
def  dir_rem ( dir_name ):
    os . rmdir ( имя_каталога )
    print ( f'Файл { dir_name } удален ' , ' \ n ' )
def  mkdir_py ( dir_name ):
    если  не  os . путь . isdir ( dir_name ):
        os . маска ( 0 )
        os . mkdir ( dir_name , 0o777 )
def  F_list ( dir_name ):
    Список  =  os . listdir ()
    для  i  в  диапазоне ( len ( Список )):
        печать ( Список [ i ])
    печать ( ' \ п ' )
    печать ( Список )
     список возврата
def  touch ( имя_файла ):
    глобальная  операционная система
    если  opeSys  ==  'posix' :
        os . система ( открыть ( имя_файла ))
    elif  opeSys  ! =  'posix' :
        если  не  os . путь . isfile ( имя_файла ):
            text_file  =  open ( имя_файла , 'w +' )
            текстовый_файл . написать ( '' )
            имя_файла  + =  '.txt'
            # os.startfile (имя_файла)
def  open_file ( имя_файла ):
    с  open ( имя_файла , 'r' , encoding = 'utf-8' ) как  файл :
        печать ( * файл )
def  переименовать ( old_Fname , new_Fanme ):
    os . переименовать ( old_Fname , new_Fanme )
    print ( f'Файл { old_Fname } переименован { new_Fanme } ! ' )
def  rm ( имя_файла ):
    os . удалить ( имя_файла )
    #print (f'Файл с именем {file_name} - удалён ')
def  moveto ( имя_файла , имя_каталога ):
    os . replace ( имя_файла , f ' { dir_name } / { file_name } ' )
    print ( f'Файл {{ file_name } был отправлен по пути { dir_name } ! ' )
def  chdir ( dir_name ):
    глобальный  user_dir_lock
    если  dir_name  ! =  'back'  и  len ( os . getcwd ()) > =  user_dir_lock :
        os . chdir ( dir_name )
        print ( f'Рабочая директория изменена на { dir_name } . ' )
    elif  dir_name  ==  'back'  и  len ( os . getcwd ()) >  user_dir_lock :
        os . chdir ( '..' )
        print ( 'Возврат к предыдущему файлу' )
    еще :
        print ( 'Выход за перделы рабочей директории не возможен!' )
def  copy_file ( имя_файла , второй_файл ):
    шутил . copyfile ( имя_файла , второй_файл )
    print ( f'Файл { file_name } скопирован ' )
def  copy_folder ( имя_файла , имя_каталога ):
    шутил . копия ( имя_файла , имя_каталога )
    print ( f'Файл { file_name } скопирован в директорию { dir_name } ' )
def  man ():
    открытый_файл ( 'manual.txt' )
def  edit_file ( имя_файла , содержимое_файла ):
    если  os . путь . существует ( str ( os . curdir ) + '/' + имя_файла ):
        file_name  =  имя_файла
        file  =  open ( имя_файла , 'w +' )
        файл . написать ( file_content )
        файл . Закрыть
    еще :
        print ( f'Файла с именнем { file_name } не существует ' )
Requ  =  input ( 'Введите запрос:' )
рек . нижний ()
в то время как  len ( Requ ) ! =  '' :
    exit_check  =  Requ . нижний ()
    если  exit_check  ==  'exit' :
        а  =  целое ( случайное . случайное () *  100 )
        если  % 5 == 0 :    
            print ( ' \ n Увидимся в следующий раз!' )
        еще :
            print ( ' \ n Завершение работы ...' )
            выход ()
    еще :
        попробуйте :
            separating_reqest ( реквизиты )
            если  req_main  ==  'mkdir' :
                mkdir_py ( REQ )
            если  req_main  ==  'remdir' :
                dir_rem ( REQ )
            если  req_main  ==  'pwd' :
                cur_dir ()
            если  req_main  ==  'ls' :
                F_list ( REQ )
            если  req_main  ==  'touch' :
                если  sec_req  ! =  '' :
                    имя_файла  =  req + '' + sec_req
                    коснитесь ( имя_файла )
                еще :
                    коснуться ( требуется )
            если  req_main  ==  'rm' :
                rm ( требуется )
            если  req_main  ==  'moveto' :
                moveto ( req , sec_req )
            если  req_main  ==  'переименовать' :
                переименовать ( req , sec_req )
            если  req_main  ==  'open' :
                open_file ( REQ )
            если  req_main  ==  'chdir' :
                chdir ( требуется )
            если  req_main  ==  'edit' :
                edit_file ( REQ )
            если  req_main  ==  'copyFile' :
                copy_file ( req , sec_req )
            если  req_main  ==  'copyto' :
                copy_folder ( req , sec_req )
            если  req_main  ==  'man' :
                мужчина ()
            если  req_main  ==  'nano' :
                file_content  =  input ( 'Введите текст файла:' )
                edit_file ( req , файл_контент )
            user_input  =  str ( os . getcwd ()) +  ':'
        кроме :
            Продолжать
        наконец :
            Requ  =  input ( user_input )
print ( 'Запрос:' , req_main )
если  req  ! =  '' :
    print ( 'Параметр запроса:' , req )
