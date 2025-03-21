Editor de Paytable - Documentação
Índice
Lista de Controles e Suas Funções
Botões (PushButtons)
ComboBoxes e Seletores
Sliders
Botões Adicionais
Tabs
Funcionalidades Extras
Thumb Templates
Dimensões e Propriedades Padrão
Elementos Componentes
Regras de Criação e Distribuição
Relação de Distância e Posicionamento

Lista de Controles e Suas Funções
Botões (PushButtons)

pushButton1:  ( cor das fontes )  abre um diálogo para escolher a cor do texto
pushButton2: Habilita o modo de edição de texto - permite adicionar novos elementos de texto na cena
pushButton3: Formata o texto selecionado como negrito (bold)
pushButton4: Remove toda a formatação do texto selecionado
pushButton5: Aplica sublinhado (underline) ao texto selecionado
pushButton6: Aplica itálico ao texto selecionado
pushButton7: Alinha dois ou mais objetos selecionados pela “Esquerda”
pushButton8: Alinha dois ou mais objetos selecionados pelo “ Centro” 
pushButton9: Alinha diis ou mais objetos selecionados pela “ Direita” 
pushButton10: Justifica o texto selecionado (distribui o texto uniformemente)
pushButton11: Alinha texto selecionado à esquerda
pushButton12: Alinha texto selecionado ao centro
pushButton13: Alinha texto selecionado à direita
pushButton14: Cria um frame ( linha )  ao redor de um item de texto selecionado. Alterna a exibição( True/False) cada vez que o botão é clicado. O frame é criado por “default” com 1px.
pushButton15: Aplica uma cor de fundo ao frame criado por “pushButton 14” (background color)
pushButton16: Remove a cor de fundo do frame criado por “pushButton14”
pushButton17: Alterna a exibição de réguas na interface ( True/False )

A régua é exibida no topo e na lateral esquerda da área de trabalho ( graphicsView) 
A regua dever ter a medida de 1920 x 1080
A nossa area de trabalho ( graphicsView1) esta em tamanho (1350 x 732 ) porem representa uma tela full HD do mundo real. ( 1920 x 1080 ) 
A régua deve possibilitar puxar a partir do topo ou da esquerda  linhas tracejadas para qualquer parte da tela, para ajudar o usuário a alinhar componentes na tela

pushButton18: Alterna a funcionalidade de snap (alinhamento automático ao grid)
pushButton19: Alinha itens selecionados pela borda inferior
pushButton20: Alinha itens selecionados pela borda superior
pushButton21: Distribui horizontalmente os itens selecionados com espaçamento igual
pushButton22: Distribui verticalmente os itens selecionados com espaçamento igual
pushButton23: Abre um seletor de cor para o contorno do frame

THUMB TEMPLATE e THUMB PRIZE
 # Sequência de pastas de p01 a p18
 
    folder_sequence = [
        os.path.join("p01", "anim")
        os.path.join("p02", "anim"),
        os.path.join("p03", "anim"),
        os.path.join("p04", "anim"),
        os.path.join("p05", "anim"),
        os.path.join("p06", "anim"),
        os.path.join("p07", "anim"),
        os.path.join("p08", "anim"),
        os.path.join("p09_royal_a", "anim"),
        os.path.join("p10_royal_k", "anim"),
        os.path.join("p11_royal_q", "anim"),
        os.path.join("p12_royal_j", "anim"),
        os.path.join("p13_royal_10", "anim"),
        os.path.join("p14_royal_9", "anim"),
        os.path.join("p15", "anim"),
        os.path.join("p16", "anim"),
        os.path.join("p17", "anim"),
        os.path.join("p18", "anim")
        os.path.join("p19", "anim")
    ]
    # O source já usa p01; as duplicatas usarão a partir de p02.
    next_folder_index = 1
    base_dir = os.path.join("resources", "pj_00", "g00", "_master", "generative", "animations", "symbols")

pushButton24: Cria um novo template de thumb (miniatura para paytable) chamado: “Thumb Template”
pushButton25: Duplica os “Thumb Template “ (cria prêmios baseados no template original) chamados “ Thumb Prizes “
pushButton26: Remove os thumb prizes (remove ambos os grupos) ( p01 a p08 ) e ( p09 a p14 ) 
pushButton27: Duplica templates de” Thumb Template” criando “Thumb Prizes”  limitado (só usa p02 a p08)  ( p01 já esta no “Thumb Template”)
pushButton28: Cria novos thumb prizes (usando p09 a p14 - royals)
pushButton29: Altera a cor de fundo da área de edição geral ( componente “graphcisView1)
pushButton30: Recarrega as imagens dos thumbs ( atualização )
pushButton31: Cria novos “thumb Prizes”( usando p15 a p19 ) 
P19 é o unico simbolo que não tem “ thumb template”. Ao ser adicionado na tela, aparece apenas a “imagem”. Sem frame ou template de design.
ComboBoxes e Seletores
fontComboBox: Seletor de fonte - permite escolher a família da fonte
comboBox1: Seletor de tamanho de fonte - permite escolher o tamanho do texto
language_combo: Seletor de idioma - permite escolher entre os idiomas disponíveis (ENG, ESP, POR)
Sliders
horizontalSlider1: Controla o arredondamento dos cantos do frame (0-100%)
horizontalSlider2: Controla a espessura da linha do frame (1-10px)


Funcionalidades Extras
Redimensionamento de Texto: Os elementos de texto podem ser redimensionados arrastando a borda direita
Redimensionamento de Thumb Templates: Os templates podem ser redimensionados arrastando as bordas
Duplicação via Ctrl+D: Os itens selecionados podem ser duplicados pressionando Ctrl+D e copiam todas as características do componente original.
Seleção Múltipla: Permite selecionar e manipular vários itens simultaneamente
4.1 - Ao selecionar a lateral direita , canto esquerdo inferior , ou lateral inferior de um “thumb template” ou “thumb prize” e escalonar, todos os outros componentes devem escalonar simultaneamente.
4.2 -  Para os componente “ thumb template” e “ thumb prizes” os demais componentes não precisam ser selecionados. 
4.3 - A codigo devera indetificar a familiar “ Thumb template” e “ thumb prizes” para aplicar a manipulação sumultanea
4.4 - O texto interno dos componentes” thumb template” e “ thumb prizes” não são afetados simultaneamente. Cada text box tem o seu proprio texto.
Suporte Multilíngue: Sistema para gerenciar traduções entre diferentes idiomas (ENG, ESP, POR) que deverão ser salvos em json na base do app.
Frames com Arredondamento: Possibilidade de adicionar frames com cantos arredondados
Controle de Alinhamento de Texto: Para cada idioma, o alinhamento é o mesmo e deve ser salvo para todos.
Save/Load de Estados: Funcionalidade para salvar e carregar o estado da tela automaticamente no json e os dados são recuperados ao reiniciar o app.


A seguir, os push Buttons mantendo seus nomes originais, mas agrupando-os por funcionalidades similares.
Reorganização dos controles por grupos funcionais

Grupo 1: Formatação de Texto
pushButton1: Cor das fontes
pushButton2: Modo de edição de texto
pushButton3: Texto em negrito
pushButton4: Remove formatação
pushButton5: Sublinhado
pushButton6: Itálico
fontComboBox: Seletor de fonte
comboBox1: Tamanho de fonte

Grupo 2: Alinhamento de Texto
pushButton10: Justifica texto
pushButton11: Alinha texto à esquerda
pushButton12: Alinha texto ao centro
pushButton13: Alinha texto à direita

Grupo 3: Frames e Bordas dos textos
pushButton14: Cria/remove frame
pushButton15: Cor de fundo do frame
pushButton16: Remove cor de fundo
pushButton23: Cor do contorno do frame
horizontalSlider1: Arredondamento dos cantos
horizontalSlider2: Espessura da linha

Grupo 4: Alinhamento de Objetos
pushButton7: Alinha objetos pela esquerda
pushButton8: Alinha objetos pelo centro
pushButton9: Alinha objetos pela direita
pushButton19: Alinha pela borda inferior
pushButton20: Alinha pela borda superior
pushButton21: Distribui horizontalmente
pushButton22: Distribui verticalmente

Grupo 5: Ferramentas de Ajuda Visual
pushButton17: Exibe/oculta réguas
pushButton18: Ativa/desativa snap ao grid
pushButton29: Muda cor de fundo da área de edição

Grupo 6: Gerenciamento de Thumb Templates
pushButton24: Cria novo Thumb Template
pushButton25: Duplica templates (cria Thumb Prizes completos)
pushButton26: Remove Thumb Prizes
pushButton27: Duplica templates limitados (p02-p08)
pushButton28: Cria novos Thumb Prizes (p09-p14 - royals)
pushButton30: Recarrega imagens dos thumbs
pushButton31: Cria novos Thumb Prizes (p15-p19)


pushButton32 - adiciona um frame no " thumb_template" 
pushButton33 - adiciona cor ao frame
pushButton34 - Adicionar cor ao bg
pushButton35 - remove a cor do bg do frame
horizontalSlider3 - cria bordas arredondadas no frame do "thumb_template"
label3 - mostra a porcentagem de arredondamento do frame  - intervalo de ( 0 - 100% )
horizontalSlider4 - controla expessura do frame  - intervalo de 1 a 10 px
label4 - mostra os valores da expessura do frame com intervalo de "1 - 10 px " 


Adicional - escalonamento do thumb_template
- A borda lateral direita  do "thumb_template" deve ser expansivel
- Ao mover a borda lateral direita do "thumb_template", a caixa/frame deve expandir para direita.


- A borda inferior do "thumb_template" deve ser expansivel
- Ao mover a borda inferior do "thumb_template", a caixa/frame deve expandir para baixo.


- A quina inferior do "thumb_template" deve ser expansivel
- Ao mover a quina inferior do "thumb_template", a caixa/frame deve expandir para baixo e para a direita.


- A imagem interna deve escalonar proporcionalmete a área disponivel no thumb_template.


Grupo 7: Idiomas
language_combo: Selector de idioma default (ENG, ESP, POR)




