import random
import pygame

class Pokemon:

    def __init__(self,name,type1,type2,Hp,Attack,Defense,Special_attack,Special_Defense,Speed):

        self.name=name
        self.types=[type1] if type2 is None else [type1,type2]
        self.hitpoints=Hp 
        self.attack=Attack
        self.spattack=Special_attack
        self.defense=Defense
        self.spdefense=Special_Defense
        self.speed=Speed
        self.currenthp=self.hitpoints
        self.move=[]
        self.HpPercent=100


    def Passiveinfo(self):
        print(f"pokemon:\"{self.name}\" types: \"{"/".join(self.types)}\" hp:\"{self.hitpoints}\" attack:\"{self.attack}\" spattack:\"{self.spattack}\" defense:\"{self.defense}\" spdefense:\"{self.spdefense}\" speed:\"{self.speed}\"")
        return ""
    

    def Activeinfo(self):
        print(f"pokemon:\"{self.name}\" types: \"{"/".join(self.types)}\" hp:\"{self.currenthp}\" attack:\"{self.attack}\" spattack:\"{self.spattack}\" defense:\"{self.defense}\" spdefense:\"{self.spdefense}\" speed:\"{self.speed}\"")
        return ""
    
    
    def Damage_Taken(self,Damage,):                             #for calculating remaining hp after taking some damage
        self.currenthp-=Damage
        if self.currenthp<=0:
            self.currenthp=0
        self.HpPercent=(self.currenthp/self.hitpoints)*100
        
        


    def Check_Status(self):
        return self.currenthp <=0




class Moves:
    def __init__(self,Name,Power,Type,Category,Accuracy):
        self.Name=Name
        self.Power=Power
        self.Type=Type
        self.Category=Category
        self.Accuracy=Accuracy





Move_Library = {

    "Iron Tail": Moves("Iron Tail",100,"Steel","Physical",75),
    "Tackle": Moves("Tackle",40,"Normal","Physical",100),
    "Thunder": Moves("Thunder",110,"Electric","Special",70),
    "Thunderbolt": Moves("Thunderbolt",90,"Electric","Special",100),
    "Icy Wind": Moves("Icy Wind",55,"Ice","Special",95),
    "Hydro Pump": Moves("Hydro Pump",110,"Water","Special",80),
    "Water Pulse": Moves("Water Pulse",60,"Water","Special",100),
    "Rock Slide": Moves("Rock Slide",75,"Rock","Physical",90),
    "Sludge Bomb": Moves("Sludge Bomb",90,"Poison","Special",100),
    "Power Whip": Moves("Power Whip",120,"Grass","Physical",85),
    "Seed Bomb": Moves("Seed Bomb",80,"Grass","Physical",100),
    "Earth Power": Moves("Earth Power",90,"Ground","Physical",100),
    "Dragon Claw": Moves("Dragon Claw",80,"Dragon","Physical",100),
    "Flamethrower": Moves("Flamethrower",90,"Fire","Special",100),
    "Shadow Claw": Moves("Shadow Claw",70,"Ghost","Special",100),
    "Hurricane": Moves("Hurricane",110,"Flying","Special",70),
    "Dark Pulse": Moves("Dark Pulse",80,"Dark","Special",100),
    "Brick Break": Moves("Brick Break",75,"Fighting","Physical",100),
    "Psychic": Moves("Psychic",90,"Psychic","Special",100),
    "Ice Beam": Moves("Ice Beam",90,"Ice","Special",100),
    "Shadow Ball": Moves("Shadow Ball",80,"Ghost","Special",100),
    "Aura Sphere": Moves("Aura Sphere",80,"Fighting","Special",100),
    "Iron Head": Moves("Iron Head",80,"Steel","Physical",100),
    "Crunch": Moves("Crunch",80,"Dark","Physical",100),
    "X-Scissor": Moves("X-Scissor",80,"Bug","Physical",100),
    "Bug Buzz": Moves("Bug Buzz",90,"Bug","Special",100),
    "Air Slash": Moves("Air Slash",75,"Flying","Special",95),
    "Waterfall": Moves("Waterfall",80,"Water","Physical",100),
    "Aqua Tail": Moves("Aqua Tail",90,"Water","Physical",90),
    "Dragon Pulse": Moves("Dragon Pulse",85,"Dragon","Special",100),
    "Play Rough": Moves("Play Rough",90,"Fairy","Physical",90),
    "Leaf Blade": Moves("Leaf Blade",90,"Grass","Physical",100),
    "Ice Punch": Moves("Ice Punch",75,"Ice","Physical",100),
    "Thunder Punch": Moves("Thunder Punch",75,"Electric","Physical",100),
    "Drain Punch": Moves("Drain Punch",75,"Fighting","Physical",100),  
    "Night Slash": Moves("Night Slash",70,"Dark","Physical",100),
    "Heat Wave": Moves("Heat Wave",95,"Fire","Special",90),
    "Flash Cannon": Moves("Flash Cannon",80,"Steel","Special",100),
    "Body Slam": Moves("Body Slam",85,"Normal","Physical",100),
    "Liquidation": Moves("Liquidation",85,"Water","Physical",100),
    "Hyper Voice": Moves("Hyper Voice",90,"Normal","Special",100),
    "Energy Ball": Moves("Energy Ball",90,"Grass","Special",100),
    "Stone Edge": Moves("Stone Edge",90,"Rock","Physical",80)


}


    
    

#Pokemon DataBase



Venusaur   =Pokemon("Venusaur","Grass","Poison",270,169,171,205,205,165)
Charizard  =Pokemon("Charizard","Fire","Flying",266,173,161,223,175,205)
Blastoise  =Pokemon("Blastoise","Water",None,268,171,205,175,215,161)
Pikachu    =Pokemon("Pikachu","Electric",None,180,230,85,210,105,279)
Gengar     =Pokemon("Gengar","Ghost","Poison",230,135,125,265,155,225)
Snorlax    =Pokemon("Snorlax","Normal",None,430,225,135,135,225,65)
Gyarados   =Pokemon("Gyarados","Water","Flying",300,255,163,125,205,167)
Alakazam   =Pokemon("Alakazam","Psychic",None,220,105,95,275,195,245)
Blissey    =Pokemon("Blissey","Normal",None,620,25,25,155,275,115)
Heracross  =Pokemon("Heracross","Bug","Fighting",270,255,155,85,195,175)
Blaziken   =Pokemon("Blaziken","Fire","Fighting",270,245,145,225,145,165)
Swampert   =Pokemon("Swampert","Water","Ground",310,225,185,175,185,125)
Lucario    =Pokemon("Lucario","Fighting","Steel",250,225,145,235,145,185)
Togekiss   =Pokemon("Togekiss","Fairy","Flying",280,105,195,245,235,165)
Volcarona  =Pokemon("Volcarona","Bug","Fire",280,125,135,275,215,205)
Chandelure =Pokemon("Chandelure","Ghost","Fire",230,115,185,295,185,165)
Haxorus    =Pokemon("Haxorus","Dragon",None,262,299,185,125,145,199)
Greninja   =Pokemon("Greninja","Water","Dark",254,195,139,211,147,249)
Aegislash  =Pokemon("Aegislash","Steel","Ghost",230,105,305,105,305,125)
Decidueye  =Pokemon("Decidueye","Grass","Ghost",266,219,155,205,205,145)

availablepokemons=[Venusaur,Charizard,Blastoise,Pikachu,Gengar,Snorlax,Gyarados,Alakazam,Blissey,Heracross,Blaziken,Swampert,Lucario,Togekiss,Volcarona,Chandelure,Haxorus,Greninja,Aegislash,Decidueye]


#Pokemon Movesets:

Venusaur.move=[
    Move_Library["Sludge Bomb"],
    Move_Library["Power Whip"],
    Move_Library["Seed Bomb"],
    Move_Library["Earth Power"]
]

Charizard.move=[
    Move_Library["Dragon Claw"],
    Move_Library["Flamethrower"],
    Move_Library["Shadow Claw"],
    Move_Library["Hurricane"]
]

Blastoise.move=[
    Move_Library["Hydro Pump"],
    Move_Library["Water Pulse"],
    Move_Library["Rock Slide"],
    Move_Library["Icy Wind"]
]

Pikachu.move=[
    Move_Library["Thunder"],
    Move_Library["Thunderbolt"],
    Move_Library["Tackle"],
    Move_Library["Iron Tail"]
]

Gengar.move=[
    Move_Library["Brick Break"],
    Move_Library["Dark Pulse"],
    Move_Library["Shadow Claw"],
    Move_Library["Sludge Bomb"]
]

Snorlax.move = [
    Move_Library["Body Slam"],
    Move_Library["Crunch"],
    Move_Library["Earth Power"],
    Move_Library["Ice Punch"]
]

Gyarados.move = [
    Move_Library["Waterfall"],
    Move_Library["Crunch"],
    Move_Library["Ice Beam"],
    Move_Library["Stone Edge"]
]

Alakazam.move = [
    Move_Library["Psychic"],
    Move_Library["Shadow Ball"],
    Move_Library["Energy Ball"],
    Move_Library["Aura Sphere"]
]

Blissey.move = [
    Move_Library["Hyper Voice"],
    Move_Library["Ice Beam"],
    Move_Library["Flamethrower"],
    Move_Library["Thunderbolt"]
]

Heracross.move = [
    Move_Library["Brick Break"],
    Move_Library["X-Scissor"],
    Move_Library["Night Slash"],
    Move_Library["Rock Slide"]
]

Blaziken.move = [
    Move_Library["Flamethrower"],
    Move_Library["Brick Break"],
    Move_Library["Thunder Punch"],
    Move_Library["Stone Edge"]
]

Swampert.move = [
    Move_Library["Waterfall"],
    Move_Library["Earth Power"],
    Move_Library["Ice Beam"],
    Move_Library["Rock Slide"]
]

Lucario.move = [
    Move_Library["Aura Sphere"],
    Move_Library["Flash Cannon"],
    Move_Library["Crunch"],
    Move_Library["Dragon Pulse"]
]

Togekiss.move = [
    Move_Library["Air Slash"],
    Move_Library["Play Rough"],
    Move_Library["Flamethrower"],
    Move_Library["Shadow Ball"]
]

Volcarona.move = [
    Move_Library["Bug Buzz"],
    Move_Library["Heat Wave"],
    Move_Library["Air Slash"],
    Move_Library["Energy Ball"]
]

Chandelure.move = [
    Move_Library["Shadow Ball"],
    Move_Library["Heat Wave"],
    Move_Library["Energy Ball"],
    Move_Library["Psychic"]
]

Haxorus.move = [
    Move_Library["Dragon Claw"],
    Move_Library["Iron Head"],
    Move_Library["Night Slash"],
    Move_Library["Earth Power"]
]

Greninja.move = [
    Move_Library["Waterfall"],
    Move_Library["Dark Pulse"],
    Move_Library["Ice Beam"],
    Move_Library["Night Slash"]
]

Aegislash.move = [
    Move_Library["Flash Cannon"],
    Move_Library["Shadow Ball"],
    Move_Library["Iron Head"],
    Move_Library["Night Slash"]
]

Decidueye.move = [
    Move_Library["Leaf Blade"],
    Move_Library["Shadow Claw"],
    Move_Library["Night Slash"],
    Move_Library["Air Slash"]
]



type_chart = {
    "Normal": {"Rock": 0.5, "Ghost": 0, "Steel": 0.5},
    "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Ice": 2, "Bug": 2, "Rock": 0.5, "Dragon": 0.5, "Steel": 2},
    "Water": {"Fire": 2, "Water": 0.5, "Grass": 0.5, "Ground": 2, "Rock": 2, "Dragon": 0.5},
    "Electric": {"Water": 2, "Electric": 0.5, "Grass": 0.5, "Ground": 0, "Flying": 2, "Dragon": 0.5},
    "Grass": {"Fire": 0.5, "Water": 2, "Grass": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Bug": 0.5, "Rock": 2, "Dragon": 0.5, "Steel": 0.5},
    "Ice": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Ice": 0.5, "Ground": 2, "Flying": 2, "Dragon": 2, "Steel": 0.5},
    "Fighting": {"Normal": 2, "Ice": 2, "Rock": 2, "Dark": 2, "Steel": 2, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Fairy": 0.5, "Ghost": 0},
    "Poison": {"Grass": 2, "Fairy": 2, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0},
    "Ground": {"Fire": 2, "Electric": 2, "Grass": 0.5, "Poison": 2, "Flying": 0, "Bug": 0.5, "Rock": 2, "Steel": 2},
    "Flying": {"Electric": 0.5, "Grass": 2, "Fighting": 2, "Bug": 2, "Rock": 0.5, "Steel": 0.5},
    "Psychic": {"Fighting": 2, "Poison": 2, "Psychic": 0.5, "Steel": 0.5, "Dark": 0},
    "Bug": {"Fire": 0.5, "Grass": 2, "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Psychic": 2, "Ghost": 0.5, "Dark": 2, "Steel": 0.5, "Fairy": 0.5},
    "Rock": {"Fire": 2, "Ice": 2, "Fighting": 0.5, "Ground": 0.5, "Flying": 2, "Bug": 2, "Steel": 0.5},
    "Ghost": {"Normal": 0, "Psychic": 2, "Ghost": 2, "Dark": 0.5},
    "Dragon": {"Dragon": 2, "Steel": 0.5, "Fairy": 0},
    "Dark": {"Fighting": 0.5, "Psychic": 2, "Ghost": 2, "Dark": 0.5, "Fairy": 0.5},
    "Steel": {"Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Ice": 2, "Rock": 2, "Fairy": 2, "Steel": 0.5},
    "Fairy": {"Fire": 0.5, "Fighting": 2, "Poison": 0.5, "Dragon": 2, "Dark": 2, "Steel": 0.5}
}





def Damage_Calculator(Attacker,Defender,Move):

    AccuracyCheck=random.randint(1,100)
    if AccuracyCheck > Move.Accuracy:
        print(f"{Attacker.name} missed")
        return 0
    else:


    #TYPE CHART & STAB(FUTURE) METHOD

        STAB=1

        EFFECTIVENESS=1
        for Defendertypes in Defender.types:

            EFFECTIVENESS*=type_chart.get(Move.Type,{}).get(Defendertypes,1)


        Modifier=STAB*EFFECTIVENESS


        if EFFECTIVENESS>1:
            print(f"{Attacker.name}'s Move Was Super Effective!")
        elif EFFECTIVENESS==0:
            print(f"{Defender.name} is immune to {Move.Name}")
        elif EFFECTIVENESS<1:
            print(f"{Attacker.name}'s Move Was Not Very Effective!")



        if Move.Category == "Physical":
            DamageCalced=Modifier*(2+((42*Move.Power*Attacker.attack)/(50*Defender.defense)))      
        else:
            DamageCalced=Modifier*(2+((42*Move.Power*Attacker.spattack)/(50*Defender.spdefense)))
        return DamageCalced
    
        

def Half_Turn(Attacker, Defender, Move):
    print(f"{Attacker.name} Used {Move.Name}!")
    dmg = Damage_Calculator(Attacker, Defender, Move)
    return dmg




pygame.init()
Game = pygame.display.set_mode((1000,559))
pygame.display.set_caption('Pokemon Battle Simulator')


#pokemonSprites

SpriteSize = (96,96)  

PokemonSpritesPlayer = {}

for p in availablepokemons:
    imgp = pygame.image.load(f"Sprites/PlayerPokemons/{p.name}back.png").convert_alpha()
    imgp = pygame.transform.smoothscale(imgp, (450,450))
    PokemonSpritesPlayer[p.name] = imgp

PokemonSpritesOpponent = {}

for p in availablepokemons:
    imgo = pygame.image.load(f"Sprites/OpponentPokemons/{p.name}front.png").convert_alpha()
    imgo = pygame.transform.smoothscale(imgo, (450,450))
    PokemonSpritesOpponent[p.name] = imgo

Clock=pygame.time.Clock()


Title=pygame.font.Font('Sprites/PokeFont.ttf',59)
Availpoke=pygame.font.Font('Sprites/PokeFont.ttf',35)
background=pygame.image.load('Sprites/background.webp')



YourPokemonName=pygame.font.Font('Sprites/PokeFont.ttf',25)
YourPokemonStat=pygame.font.Font('Sprites/PokeFont.ttf',20)
OpponentPokemonName=pygame.font.Font('Sprites/PokeFont.ttf',25)
OpponentPokemonStat=pygame.font.Font('Sprites/PokeFont.ttf',20)

PokemonMoveDisplay=pygame.font.Font('Sprites/PokeFont.ttf',15)
PokemonInfoInBox=pygame.font.Font('Sprites/PokeFont.ttf',20)

Game_State='PokemonChoose'
PlayerPokemon=None
OpponentPokemon=None
PlayerPokemonMove=None
OpponentPokemonMove=None

DisplayBelow=True

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and Game_State=='PokemonChoose':
            MouseHoverLocation=event.pos
            Rects=globals().get('SelectedRectangle',[])

            for Rect,Index in Rects:
                if Rect.collidepoint(MouseHoverLocation):
                    PlayerPokemon=availablepokemons[Index]
                    OpponentPokemon=random.choice([p for p in availablepokemons if p !=PlayerPokemon])

                    PlayerPokemon.currenthp = PlayerPokemon.hitpoints
                    PlayerPokemon.HpPercent = 100
                    OpponentPokemon.currenthp = OpponentPokemon.hitpoints
                    OpponentPokemon.HpPercent = 100
                    PlayerPokemonMove = PlayerPokemon.move[0]
                    OpponentPokemonMove = OpponentPokemon.move[0]

                    Game_State='MoveChoose'
                    MovePhase='Intro'


        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

            if Game_State == 'MoveChoose' and MovePhase == 'Intro':
                MovePhase = 'Select'


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and Game_State == 'MoveChoose' and MovePhase == 'Select':

            mx, my = event.pos
            move_positions = [(90,434), (415,434), (90,494), (415,494)]

            for idx, pos in enumerate(move_positions):
                surf = PokemonMoveDisplay.render(f"{PlayerPokemon.move[idx].Name}    {PlayerPokemon.move[idx].Power}    {PlayerPokemon.move[idx].Type}", False, 'Black')
                rect = surf.get_rect(topleft=pos)
                click_rect = pygame.Rect(rect.x - 6, rect.y - 6, rect.width + 12, rect.height + 30)
                if click_rect.collidepoint(mx, my):
                    PlayerPokemonMove = PlayerPokemon.move[idx]
                    OpponentPokemonMove = OpponentPokemon.move[random.randint(0,3)]
                    Game_State = 'BattleStart'
                    break


    if Game_State=='PokemonChoose':
        PokemonChooseScreen=pygame.draw.rect(Game,(128,128,128),(0,0,1000,559))
        PokemonChooseScreenBorder=pygame.draw.rect(Game,(108,108,108),(0,0,1000,559),20)
        Title_Surface=Title.render("Choose Your Pokemon",False,'Black')
        Game.blit(Title_Surface,(40,20))
    

        SelectedRectangle = []

        XLeftCoords=50
        XRightCoords=560
        YCoords=100
        TextHeight=40

        MouseHoverLocation=pygame.mouse.get_pos()


        for i in range(0,10):
            LeftIndex=i
            Availpokeselect=Availpoke.render(f"{LeftIndex+1}). {availablepokemons[LeftIndex].name}", False, 'Black')
            LeftRectangle = Availpokeselect.get_rect(topleft=(XLeftCoords, YCoords + (TextHeight * i)))
            ClickableLeftRectangle = pygame.Rect(LeftRectangle.x - 6, LeftRectangle.y - 4, LeftRectangle.width + 12, LeftRectangle.height + 8)


            if ClickableLeftRectangle.collidepoint(MouseHoverLocation):
                pygame.draw.rect(Game, (200, 200, 200), ClickableLeftRectangle)
            Game.blit(Availpokeselect, LeftRectangle)
            SelectedRectangle.append((ClickableLeftRectangle, LeftIndex))
        

        for i in range(0,10):
            RightIndex=i+10
            Availpokeselect=Availpoke.render(f"{RightIndex+1}). {availablepokemons[RightIndex].name}", False, 'Black')
            RightRectangle = Availpokeselect.get_rect(topleft=(XRightCoords, YCoords + (TextHeight * i)))
            ClickableRightRectangle = pygame.Rect(RightRectangle.x - 6, RightRectangle.y - 4, RightRectangle.width + 12, RightRectangle.height + 8)

            
            if ClickableRightRectangle.collidepoint(MouseHoverLocation):
                pygame.draw.rect(Game, (200, 200, 200), ClickableRightRectangle)
            Game.blit(Availpokeselect, RightRectangle)
            SelectedRectangle.append((ClickableRightRectangle, RightIndex))



        globals()['SelectedRectangle']=SelectedRectangle


        
    elif Game_State=='MoveChoose':
        Game.blit(background,(0,0))

        PlayerPokemonMoves=PlayerPokemon.move
        SelectedPlayerMove = []
        MouseHoverLocation=pygame.mouse.get_pos()
        


        #POKEMON SPRITE
        player_sprite = getattr(PlayerPokemon, "sprite", PokemonSpritesPlayer.get(PlayerPokemon.name))
        opponent_sprite = getattr(OpponentPokemon, "sprite", PokemonSpritesOpponent.get(OpponentPokemon.name))


        if player_sprite:
            Game.blit(player_sprite, (10,100))
        if opponent_sprite:
            Game.blit(opponent_sprite, (520,20))


        #INFO BOX
        pygame.draw.rect(Game,(195,195,195),(0,409,1000,150))
        pygame.draw.rect(Game,(180,180,180),(0,409,1000,150),15)


        #HEALTHBAR
        YourPokemonDeadHealthBar=pygame.draw.rect(Game,(255,20,50),(20,130,300,25))
        YourPokemonHealthBar=pygame.draw.rect(Game,(10,255,10),(20,130,3*PlayerPokemon.HpPercent,25))
        OpponentPokemonDeadHealthBar=pygame.draw.rect(Game,(255,20,50),(660,70,300,25))
        OpponentPokemonHealthBar=pygame.draw.rect(Game,(10,255,10),(660,70,3*OpponentPokemon.HpPercent,25))

        #NAMES
        YourPokemonNameDisplay=YourPokemonName.render(f"{PlayerPokemon.name}     Lv100",False,'Black')
        YourPokemonDisplayStat=YourPokemonStat.render(f"{PlayerPokemon.types}",False,'Black')
        OpponentPokemonNameDisplay=OpponentPokemonName.render(f"{OpponentPokemon.name}     Lv100",False,'Black')
        OpponentPokemonDisplayStat=OpponentPokemonStat.render(f"{OpponentPokemon.types}",False,'Black')
        
        #BLITTIN
        Game.blit(YourPokemonNameDisplay,(20,70))
        Game.blit(YourPokemonDisplayStat,(20,100))
        Game.blit(OpponentPokemonNameDisplay,(660,10))
        Game.blit(OpponentPokemonDisplayStat,(660,40))


        
        if MovePhase== 'Intro':
            ChosenPokemonPlay=PokemonInfoInBox.render(f"You Chose {PlayerPokemon.name}!",False,'Black')
            ChosenPokemonOpp=PokemonInfoInBox.render(f"Your Opponent Chose {OpponentPokemon.name}!",False,'Black')
            Game.blit(ChosenPokemonPlay,(30,439))
            Game.blit(ChosenPokemonOpp,(30,479))
            Proceed=PokemonInfoInBox.render("Click Enter to Proceed",False,'Black')
            Game.blit(Proceed,(330,519))


        elif MovePhase== 'Select':

            Move1Coords=(90,434)
            MoveextraCoords1=(90,454)
            Move2Coords=(415,434)
            MoveextraCoords2=(415,454)
            Move3Coords=(90,494)
            MoveextraCoords3=(90,514)
            Move4Coords=(415,494)
            MoveextraCoords4=(415,514)

            Move_Coords=[(90,434),(415,434),(90,494),(415,494),(90,454),(415,454),(90,514),(415,514)]

            for i in range(0,4):
                MoveIndex=i
                MoveOption=PokemonMoveDisplay.render(f"{PlayerPokemonMoves[i].Name}    {PlayerPokemonMoves[i].Power}    {PlayerPokemonMoves[i].Type}",False,'Black')
                MoveOptionStat=PokemonMoveDisplay.render(f"{PlayerPokemonMoves[i].Category}    {PlayerPokemonMoves[i].Accuracy}",False,'Black')

                Game.blit(MoveOption,Move_Coords[i])
                Game.blit(MoveOptionStat,Move_Coords[i+4])

                ClickRectangleMove=MoveOption.get_rect(topleft=(Move_Coords[i]))
                ClickableRectangleMove=pygame.Rect(ClickRectangleMove.x-6,ClickRectangleMove.y-6,ClickRectangleMove.width+12,ClickRectangleMove.height+30)


                if ClickableRectangleMove.collidepoint(MouseHoverLocation):
                    pygame.draw.rect(Game, (145, 145, 145), ClickableRectangleMove)
                    Game.blit(MoveOption,Move_Coords[i])
                    Game.blit(MoveOptionStat,Move_Coords[i+4])

                SelectedPlayerMove.append((ClickableRectangleMove, MoveIndex))


        globals()['SelectedPlayerMove']=SelectedPlayerMove


        pygame.display.update()


    elif Game_State=='BattleStart':

       

        if PlayerPokemon.speed > OpponentPokemon.speed:
            Order = [
                (PlayerPokemon, OpponentPokemon, PlayerPokemonMove),
                (OpponentPokemon, PlayerPokemon, OpponentPokemonMove),
            ]
        else:
            Order = [
                (OpponentPokemon, PlayerPokemon, OpponentPokemonMove),
                (PlayerPokemon, OpponentPokemon, PlayerPokemonMove),
            ]


        SomeoneFainted = False
        for Attacker, Defender, Move in Order:
            if Move is None:
                continue

            Dmg = Half_Turn(Attacker, Defender, Move)

            Effectiveness = 1
            for T in Defender.types:
                Effectiveness *= type_chart.get(Move.Type, {}).get(T, 1)

            if Effectiveness > 1:
                Eff = f"{Move.Name} Was Super Effective!"
            elif Effectiveness == 0:
                Eff = f"{Defender.name} Is Immune To {Move.Name}"
            elif Effectiveness < 1:
                Eff = f"{Move.Name} Was Not Very Effective"
            else:
                Eff = ""

            WhatHappened = PokemonInfoInBox.render(f"{Attacker.name} Used {Move.Name}", False, 'Black')
            WhatHappenedMore = PokemonInfoInBox.render(Eff, False, 'Black')
            Proceed = PokemonInfoInBox.render("Press Enter to continue", False, 'Black')

            #Start of Redraw because text overlapping issue

            Game.blit(background, (0,0))

            PlayerSprite = getattr(PlayerPokemon, "sprite", PokemonSpritesPlayer.get(PlayerPokemon.name))
            OpponentSprite = getattr(OpponentPokemon, "sprite", PokemonSpritesOpponent.get(OpponentPokemon.name))
            if PlayerSprite:
                Game.blit(PlayerSprite, (10,100))
            if OpponentSprite:
                Game.blit(OpponentSprite, (520,20))

            
            pygame.draw.rect(Game, (195,195,195), (0,409,1000,150))
            pygame.draw.rect(Game, (180,180,180), (0,409,1000,150), 15)

            pygame.draw.rect(Game, (255,20,50), (20,130,300,25))
            pygame.draw.rect(Game, (10,255,10), (20,130,3 * PlayerPokemon.HpPercent, 25))
            pygame.draw.rect(Game, (255,20,50), (660,70,300,25))
            pygame.draw.rect(Game, (10,255,10), (660,70,3 * OpponentPokemon.HpPercent, 25))

            YourPokemonNameDisplay = YourPokemonName.render(f"{PlayerPokemon.name}     Lv100", False, 'Black')
            YourPokemonDisplayStat = YourPokemonStat.render(f"{PlayerPokemon.types}", False, 'Black')
            OpponentPokemonNameDisplay = OpponentPokemonName.render(f"{OpponentPokemon.name}     Lv100", False, 'Black')
            OpponentPokemonDisplayStat = OpponentPokemonStat.render(f"{OpponentPokemon.types}", False, 'Black')

            Game.blit(YourPokemonNameDisplay, (20,70))
            Game.blit(YourPokemonDisplayStat, (20,100))
            Game.blit(OpponentPokemonNameDisplay, (660,10))
            Game.blit(OpponentPokemonDisplayStat, (660,40))

            Game.blit(WhatHappened, (30,439))
            Game.blit(WhatHappenedMore, (30,479))
            Game.blit(Proceed, (330,519))
            pygame.display.update()

            #end of redrawing

            if Dmg == 0:
                Waiting = True
                while Waiting:
                    for Ev in pygame.event.get():
                        if Ev.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if Ev.type == pygame.KEYDOWN and Ev.key == pygame.K_RETURN:
                            Waiting = False
                continue

            HpBefore = Defender.currenthp
            HpAfter = HpBefore - Dmg
            if HpAfter <= 0:
                Defender.currenthp = 0
            else:
                Defender.currenthp = HpAfter
            Defender.HpPercent = (Defender.currenthp / Defender.hitpoints) * 100


            #REDRAW AGAIN RAHHH
            Game.blit(background, (0,0))
            PlayerSprite = getattr(PlayerPokemon, "sprite", PokemonSpritesPlayer.get(PlayerPokemon.name))
            OpponentSprite = getattr(OpponentPokemon, "sprite", PokemonSpritesOpponent.get(OpponentPokemon.name))
            if PlayerSprite:
                Game.blit(PlayerSprite, (10,100))
            if OpponentSprite:
                Game.blit(OpponentSprite, (520,20))

            pygame.draw.rect(Game, (195,195,195), (0,409,1000,150))
            pygame.draw.rect(Game, (180,180,180), (0,409,1000,150), 15)

            pygame.draw.rect(Game, (255,20,50), (20,130,300,25))
            pygame.draw.rect(Game, (10,255,10), (20,130,3 * PlayerPokemon.HpPercent, 25))
            pygame.draw.rect(Game, (255,20,50), (660,70,300,25))
            pygame.draw.rect(Game, (10,255,10), (660,70,3 * OpponentPokemon.HpPercent, 25))

            YourPokemonNameDisplay = YourPokemonName.render(f"{PlayerPokemon.name}     Lv100", False, 'Black')
            YourPokemonDisplayStat = YourPokemonStat.render(f"{PlayerPokemon.types}", False, 'Black')
            OpponentPokemonNameDisplay = OpponentPokemonName.render(f"{OpponentPokemon.name}     Lv100", False, 'Black')
            OpponentPokemonDisplayStat = OpponentPokemonStat.render(f"{OpponentPokemon.types}", False, 'Black')

            Game.blit(YourPokemonNameDisplay, (20,70))
            Game.blit(YourPokemonDisplayStat, (20,100))
            Game.blit(OpponentPokemonNameDisplay, (660,10))
            Game.blit(OpponentPokemonDisplayStat, (660,40))

            Game.blit(WhatHappened, (30,439))
            Game.blit(WhatHappenedMore, (30,479))
            Game.blit(Proceed, (330,519))
            pygame.display.update()


            if Defender.Check_Status():
                #ReDRaw Freaking Again
                Game.blit(background, (0,0))

                PlayerSprite = getattr(PlayerPokemon, "sprite", PokemonSpritesPlayer.get(PlayerPokemon.name))
                OpponentSprite = getattr(OpponentPokemon, "sprite", PokemonSpritesOpponent.get(OpponentPokemon.name))
                if PlayerSprite:
                    Game.blit(PlayerSprite, (10,100))
                if OpponentSprite:
                    Game.blit(OpponentSprite, (520,20))

                pygame.draw.rect(Game, (255,20,50), (20,130,300,25))
                pygame.draw.rect(Game, (10,255,10), (20,130,3 * PlayerPokemon.HpPercent, 25))
                pygame.draw.rect(Game, (255,20,50), (660,70,300,25))
                pygame.draw.rect(Game, (10,255,10), (660,70,3 * OpponentPokemon.HpPercent, 25))

                YourPokemonNameDisplay = YourPokemonName.render(f"{PlayerPokemon.name}     Lv100", False, 'Black')
                YourPokemonDisplayStat = YourPokemonStat.render(f"{PlayerPokemon.types}", False, 'Black')
                OpponentPokemonNameDisplay = OpponentPokemonName.render(f"{OpponentPokemon.name}     Lv100", False, 'Black')
                OpponentPokemonDisplayStat = OpponentPokemonStat.render(f"{OpponentPokemon.types}", False, 'Black')

                Game.blit(YourPokemonNameDisplay, (20,70))
                Game.blit(YourPokemonDisplayStat, (20,100))
                Game.blit(OpponentPokemonNameDisplay, (660,10))
                Game.blit(OpponentPokemonDisplayStat, (660,40))

                pygame.draw.rect(Game, (195,195,195), (0,409,1000,150))
                pygame.draw.rect(Game, (180,180,180), (0,409,1000,150), 15)

                FaintMsg = PokemonInfoInBox.render(f"{Defender.name} has Fainted!", False, 'Black')
                Game.blit(FaintMsg, (30,439))

                if PlayerPokemon.Check_Status():
                    FaintMsgDetail = PokemonInfoInBox.render("You Lose!",False,'Black')
                elif OpponentPokemon.Check_Status():
                    FaintMsgDetail = PokemonInfoInBox.render("You Win!",False,'Black')
                Game.blit(FaintMsgDetail,(30,480))
                pygame.display.update()

                Waiting = True
                while Waiting:
                    for Ev in pygame.event.get():
                        if Ev.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if Ev.type == pygame.KEYDOWN and Ev.key == pygame.K_RETURN:
                            Waiting = False
                SomeoneFainted = True
                break


            Waiting = True
            while Waiting:
                for Ev in pygame.event.get():
                    if Ev.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if Ev.type == pygame.KEYDOWN and Ev.key == pygame.K_RETURN:
                        Waiting = False


        if SomeoneFainted:
            if PlayerPokemon.Check_Status():
                Game_State = 'End'
                print(f"Your {PlayerPokemon.name} has Fainted!")
            elif OpponentPokemon.Check_Status():
                Game_State = 'End'
                print(f"Opponent's {OpponentPokemon.name} has Fainted!")
        else:
            Game_State = 'MoveChoose'


    pygame.display.update()
    Clock.tick(60)

#Will later add STAB multiplier and also polish this game a bit later