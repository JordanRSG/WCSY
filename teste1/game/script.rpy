define e = Character("Eleanora")
define p = Character("[pc_name]", color="#993399")
default pc_name = "...."

image bgPark = "bgpark.jpg"
image bgRuas = "ruas.jpg"

image eleanora = "minazinha1-1.png"
image eleanoracorando = "minazinha2-1.png"

    
# O jogo inicia aqui

label start:

    $cont = 0
    
    scene bgPark

   
    play music "simple.mp3"
    

    # Linhas de dialogo
    
    "Escolha um genero"
    
    menu:
        "Masculino":
            jump conversaM
        "Feminino":
            jump conversaF
            
label conversaM:
    
    "Você está andando pelo parque..."
    
    "..."
    
     
    show eleanora

    e "Olá, qual é seu nome?"
    
    $pc_name = renpy.input("Qual é meu nome?")
    $pc_name = pc_name.strip()
    
    p "Meu nome é [pc_name]"
    
    hide eleanora
    
    show eleanoracorando
    
    e "Prazer em te conhecer [pc_name]!"
    
    hide eleanoracorando
    
    show eleanora
    
    e "Você é novo na cidade? Nunca te vi por aqui!"
    
    menu:
        "Sim(continua)":
            jump cExplica
        "Não(acaba o teste)":
            jump cFinal

        
label conversaF:
    
    "Você está andando pelo parque..."
    
    "..."
    
     
    show eleanora

    e "Olá, qual é seu nome?"
    
    $pc_name = renpy.input("Qual é meu nome?")
    $pc_name = pc_name.strip()
    
    p "Meu nome é [pc_name]"
    
    hide eleanora
    
    show eleanoracorando
    
    e "Prazer em te conhecer [pc_name]!"
    
    hide eleanoracorando
    
    show eleanora
    
    e "Você é nova na cidade? Nunca te vi por aqui!"
    
    menu:
        "Sim(continua)":
            jump cExplica
        "Não(acaba o teste)":
            jump cFinal
    
label cExplica:
    
    $cont += 1
    
    scene bgRuas
    with fade
    
    show eleanora
    with dissolve
    
    e "Esse jogo é feito com uma IDE chamada ren'py"
    e "e está sendo utilizado para criar nosso projeto de tcc"
    
    if cont == 5:
        e "Uau você está realmente querendo saber sobre o jogo não é?"
           
    if cont >= 7:
        e "Sério não precisa mais ler isso, você ja leu %(cont)d vezes"
    
    menu:
        "Repitir?":
            jump cExplica
        "Acabar?":
            jump cFinal
    
label cFinal:
    
    hide eleanora
    
    show eleanoracorando at right
    e "Obrigada por jogar!"
    
    # O jogo acaba no return
    

    return
