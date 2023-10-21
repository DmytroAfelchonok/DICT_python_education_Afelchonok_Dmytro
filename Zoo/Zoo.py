"""The Zoo project"""

print("""I love animals!
Let's check out the animals...
The deer looks fine.
The lion looks healthy.""")

camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that!"""

lion = r"""
The lion habitat...
                                               ,w. 
                                             ,YWMMw  ,M  , 
                        _.---.._   ..---._.'MMMMMw,wMWmW, 
                   _.-""        '''           YP"WMMMMMMMMMb, 
                .-' .'                   .'     MMMMW^WMMMM;     
            _, .'.-'"; ,       /     .--""      :MMM[==MWMW^; 
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\ 
,MM:.    .'.-'   .'     ;     \    ;     ,     MMMMMMMW "=./-, 
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_} 
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; |            
          /   .'            ; ;         )  )`{  \ `"^W^`,   \  :           
          /  .'             /  (       .'  /     Ww._     `.  `" 
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,         
         (--, )                `,_ / `) \/"")      ^"      `-, -;"\: 

The lion is roaring!"""

deer = r"""
The deer habitat...
   /|       |\
`__\\       //'__'
    ||      ||
 \__`\      |'__/
   `_\\    //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""

goose = r"""
The goose habitat...
                                _,-"" "". 
                              ,'  ____   `. 
                            ,'  ,'    `.   `._ 
   (`.         _..--.._   ,'  ,'        \     \ 
  (`-.\    .-""        ""'   /          (  d _ b 
 (`._  `-"" ,._             (            `-(    \  
 <_  `     (  <`<            \              `-._\   
 <`-       (< <            :    
 (          (_<_<          ; 
 `------------------------------------------ 
Beautiful!"""

bat = r"""
The bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It's doing fine."""

rabbit = r"""
The rabbit habitat...
                      /|      
                     / |   ,-~ /             
                    Y :|  //  /       
                    | jj /( .^     
                    >-"~"-v"           
                   /       Y
                  jo  o    |     
                 ( ~T~     j    
                  >._-' _./      
               /| ;-"~ _  l
              / l/ ,-"~    \   
              \//\/      .- \
               Y        /    Y
               l       I     !
               ]\      _\    /"\
              (" ~----( ~   Y.  )
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]
print("Please enter the number of the habitat you would like to view:")

while True:
    answer = input()
    if answer.isdigit():
        answer = int(answer)
        if 1 <= answer <= len(animals):
            print(animals[int(answer) - 1])
            print("Please enter the number of the habitat you would like to view:")
        else:
            print("Please enter a correct number or 'exit' to exit.")
    elif answer == "exit":
        print("See you later!")
        break
    else:
        print("Please enter a correct number or 'exit' to exit.")
