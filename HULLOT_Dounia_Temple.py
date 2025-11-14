import maya.cmds as cmds
import math

# Création du socle principal du temple
socle_temple = cmds.polyCube(w=20, d=15, h=1, n="Socle_Temple")[0]
cmds.move(0, 0.5, 0, socle_temple)

# Colonnes de support du temple
# Positions : (x, z, rayon) - Les colonnes aux coins ont un rayon plus grand
positions_colonnes = [
    (-6, -4.5, 0.5), (6, -4.5, 0.5), (-6, 4.5, 0.5), (6, 4.5, 0.5),  # Colonnes d'angle
    (-6, 0, 0), (6, 0, 0),  # Colonnes latérales
    (0, -4.5, 0.5), (0, 4.5, 0.5)   # Colonnes centrales
]
for x, z, rayon_colonne in positions_colonnes:
    colonne = cmds.polyCylinder(r=rayon_colonne, h=6, n="Colonne_Support")[0]
    cmds.move(x, 3.5, z, colonne)

# Corps du temple
corps = cmds.polyCube(w=12, d=8, h=6, n="Corps")[0]
cmds.move(0, 3.5, 0, corps)

porte = cmds.polyCube(w=3, d=4, h=5, n="porte1")[0]
cmds.move(-3.5, 4, 3.5, porte)
corps2 = cmds.polyBoolOp(corps, porte, op=2, n="corps2")[0]

porte2 = cmds.polyCube(w=3, d=4, h=5, n="porte2")[0]
cmds.move(0, 4, 3.5, porte2)
corps3 = cmds.polyBoolOp(corps2, porte2, op=2, n="corps3")[0]

porte3 = cmds.polyCube(w=3, d=4, h=5, n="porte3")[0]
cmds.move(3.5, 4, 3.5, porte3)
corps4 = cmds.polyBoolOp(corps3, porte3, op=2, n="corps4")[0]

# Balustrades autour du socle
balustrades_pos = [
    (0, -7.2, 18, 0.3),   # avant
    (0, 7.2, 18, 0.3),    # arrière
    (-9.5, 0, 0.3, 13),   # gauche
    (9.5, 0, 0.3, 13)     # droite
]
for x, z, w, d in balustrades_pos:
    bal = cmds.polyCube(w=w, d=d, h=0.6, n="Balustrade")[0]
    cmds.move(x, 1.2, z, bal)

# Toit principal
toit = cmds.polyCube(w=14, d=10, h=0.5, n="Toit")[0]
cmds.move(0, 7, 0, toit)
# Extrusion vers le haut
cmds.select(toit + ".f[1]")
cmds.polyExtrudeFacet(ltz=1, ls=(1.3, 1.5, 1))

cmds.rotate(0,0,180, toit)
# Deuxième étage du toit
toit2 = cmds.polyCube(w=12.6, d=6, h=1, n="Toit_Sup")[0]
cmds.move(0, 7.5, 0, toit2)

# Extrusion du toit supérieur
cmds.select(toit2 + ".f[1]")
cmds.polyExtrudeFacet(ltz=0.8, ls=(1.2, 1.2, 1))

# Opérations booléennes pour arrondir le toit du haut
cylindre_toit = cmds.polyCylinder(n="Cylindre_Toit", r=3.5,h=15,sa=3)[0]
cmds.move(0, 10.5, 0, cylindre_toit)
cmds.rotate(0,0,90, cylindre_toit)

# Sphère pour découper le haut du toit et créer l'arrondi
sphereDecoupe_h = cmds.polySphere(r=17, n="sphereDecoupe_h")[0]
cmds.move(0, 28, 0, sphereDecoupe_h)
toit_arrondi_haut = cmds.polyBoolOp(cylindre_toit, sphereDecoupe_h, op=2, n="Toit_Arrondi_Haut")[0]

# Sphères pour découper les côtés du toit et créer les arrondis latéraux
sphereDecoupe_g = cmds.polySphere(r=5, n="sphereDecoupe_g")[0]
cmds.move(-10, 11.5, 0, sphereDecoupe_g)
toit_arrondi_lateral1 = cmds.polyBoolOp(toit_arrondi_haut, sphereDecoupe_g, op=2, n="Toit_Arrondi_Lateral1")[0]

sphereDecoupe_d = cmds.polySphere(r=5, n="sphereDecoupe_d")[0]
cmds.move(10, 11.5, 0, sphereDecoupe_d)
toit_arrondi_lateral2 = cmds.polyBoolOp(toit_arrondi_lateral1, sphereDecoupe_d, op=2, n="Toit_Arrondi_Lateral2")[0]

# Opération booléenne pour faire effet courbé vers le haut sur le toit
test= cmds.polyCube(w=14, d=10, h=0.5, n="test")[0]
cmds.move(0, 6, 0, test)
cmds.scale(1.3, 1, 1.5, test)

bout = cmds.polySphere(r=9.6, n="bout")[0]
cmds.move(0, 10.5, 0, bout)
cmds.scale(1.3, 1, 1.5, bout)
teste = cmds.polyBoolOp(test, bout, op=2, n="teste")[0]

# Au-dessus du toit supérieur
test2 = cmds.polyCube(w=12.6, d=6, h=0.5, n="test2")[0]
cmds.move(0, 9, 0, test2)
cmds.scale(1.2, 1, 1.2, test2)

bout2 = cmds.polySphere(r=7.8, n="bout2")[0]
cmds.move(0, 12.5, 0, bout2)
cmds.scale(1.2, 1, 1.2, bout2)
teste2 = cmds.polyBoolOp(test2, bout2, op=2, n="teste2")[0]

#Escalier devant le temple
escalier0 = cmds.polyCube(w=20, d=15, h=1, n="escalier0")[0]
cmds.move(0, 0.5, 8, escalier0)
cmds.scale(0.7, 0.8, 0.16, escalier0)

escalier1 = cmds.polyCube(w=20, d=15, h=1, n="escalier1")[0]
cmds.move(0, 0.35, 8, escalier1)
cmds.scale(0.8, 0.5, 0.3, escalier1)

escalier2 = cmds.polyCube(w=20, d=15, h=0.3, n="escalier2")[0]
cmds.move(0, 0.15, 9, escalier2)
cmds.scale(0.9, 1, 0.3, escalier2)

# Cube décoratif sur les marches
cube_marche = cmds.polyCube(w=1, d=1, h=1, n="cube_marche")[0]
cmds.move(0, 0.5, 10.5, cube_marche)
cmds.rotate(16.5, 0, 0, cube_marche)
cmds.scale(4.2, 0.2, 2.4, cube_marche)

# Décorations sur les côtés du temple
cube_deco1= cmds.polyCube(sx=3, sy=3, sz=3, w=3, d=2.8, h=2, n="cube_deco1")[0]
cmds.move(7.5,1, 10, cube_deco1)

cmds.select(cube_deco1 + ".f[4]", cube_deco1 + ".f[40]")
cmds.polyExtrudeFacet(ltz=-0.8, kft=True)

cmds.select(cube_deco1)
cmds.polyMirrorFace()

# Sphères pour la décoration droite
sphere_coin3 = cmds.polySphere(r=0.2, n="sphereDroite_1")[0]
cmds.move(6.5, 2.1, 11, sphere_coin3)

sphere_coin4 = cmds.polySphere(r=0.2, n="sphereDroite_2")[0]
cmds.move(8.5, 2.1, 11, sphere_coin4)

# Sphères pour la décoration gauche
sphere_coin7 = cmds.polySphere(r=0.2, n="sphereGauche_1")[0] 
cmds.move(-6.5, 2.1, 11, sphere_coin7)

sphere_coin8 = cmds.polySphere(r=0.2, n="sphereGauche_2")[0]
cmds.move(-8.5, 2.1, 11, sphere_coin8)

# Création des dragons
# Paramètres de la courbe sinusoïdale
Longueur = 6
amplitude = 1.0
nb_v = 1.8
nb_p = 1000
hauteur = 8.5
pts_courbe = []

# Suppression des anciens dragons s'ils existent
if cmds.objExists("dragon_tube"):
    cmds.delete("dragon_tube")
if cmds.objExists("dragon_tube2"):
    cmds.delete("dragon_tube2")

# Génération de la courbe
for i in range(nb_p + 1):
    u = float(i)/nb_p
    X = u * Longueur
    Z = math.cos(u * 2 * math.pi * nb_v) * amplitude
    Y = hauteur
    pts_courbe.append((X, Y, Z))

# Création de la courbe
if cmds.objExists("dragon"):
    cmds.delete("dragon")
chemin_dragon = cmds.curve(p=pts_courbe, d=3, n="dragon")

cmds.move(1.5, 12, 6, chemin_dragon, absolute=True)
cmds.rotate(-90, 0, 10, chemin_dragon, absolute=True)
cmds.scale(0.7, 0.7, 0.7, chemin_dragon)

# Création d'un profil circulaire pour donner du volume au dragon
profil_dragon = cmds.circle(nr=(0, 0, 1), c=(0, 0, 0), r=0.15, n="profil_dragon")[0]

# Extrusion du profil le long de la courbe pour créer un tube
dragon_geometrie = cmds.extrude(profil_dragon, chemin_dragon, 
                               ch=True, rn=False, po=1, et=2, ucp=1, 
                               fpt=True, upn=1, rotation=0, scale=1, 
                               rsp=1, n="dragon_tube")[0]

# Supprimer le profil temporaire
cmds.delete(profil_dragon)

# Dupliquer pour dragon 2
dragon_miroir = cmds.duplicate(chemin_dragon, n="dragon_miroir")[0]

# Transformations dragon 2
cmds.move(-1.5, 12, 6, dragon_miroir, absolute=True)
cmds.rotate(-90, 180, -10, dragon_miroir, absolute=True)
cmds.scale(0.7, -0.7, 0.7, dragon_miroir)

# Création du second tube pour le dragon miroir
profil_dragon2 = cmds.circle(nr=(0, 0, 1), c=(0, 0, 0), r=0.15, n="profil_dragon2")[0]
dragon_geometrie2 = cmds.extrude(profil_dragon2, dragon_miroir, 
                                ch=True, rn=False, po=1, et=2, ucp=1, 
                                fpt=True, upn=1, rotation=0, scale=1, 
                                rsp=1, n="dragon_tube2")[0]
cmds.delete(profil_dragon2)

# Petite pagode au sommet
nb_etages = 6
hauteur_actuelle = 11.2
largeur_base = 1.2
objets_pagode = []

for i in range(nb_etages):
    largeur = largeur_base - i*0.15
    
    # Toit de l'étage
    toit_etage = cmds.polyCube(w=largeur, d=largeur, h=0.08, n="pagode_toit_" + str(i))[0]
    cmds.move(0, hauteur_actuelle, 0, toit_etage)
    cmds.select(toit_etage + ".f[1]")
    cmds.polyExtrudeFacet(ltz=0.12, ls=(1.3, 1.3, 1))
    objets_pagode.append(toit_etage)
    
    hauteur_actuelle += 0.24
    
    # Corps cylindrique de l'étage
    corps_etage = cmds.polyCylinder(r=largeur*0.25, h=0.32, n="pagode_corps_" + str(i))[0]
    cmds.move(0, hauteur_actuelle, 0, corps_etage)
    objets_pagode.append(corps_etage)
    
    hauteur_actuelle += 0.24

# Flèche au sommet
fleche = cmds.polyCone(r=0.16, h=0.48, n="pagode_fleche")[0]
cmds.move(0, hauteur_actuelle, 0, fleche)
objets_pagode.append(fleche)

# Combiner en un seul objet
pagode_complete = cmds.polyUnite(objets_pagode, n="Pagode")[0]
cmds.delete(pagode_complete, ch=True)

#---------------------------------------------------------------------------------------

# Création des matériaux avec shaders Lambert
materiau_pierre = cmds.shadingNode('lambert', asShader=True, n='Materiau_Pierre')
cmds.setAttr(materiau_pierre + '.color', 0.7, 0.65, 0.6, type='double3')  # Gris pierre

materiau_toit = cmds.shadingNode('lambert', asShader=True, n='Materiau_Toit')
cmds.setAttr(materiau_toit + '.color', 0.8, 0.2, 0.1, type='double3')  # Rouge tuile

materiau_or = cmds.shadingNode('lambert', asShader=True, n='Materiau_Or')
cmds.setAttr(materiau_or + '.color', 0.9, 0.7, 0.2, type='double3')  # Or

materiau_dragon = cmds.shadingNode('lambert', asShader=True, n='Materiau_Dragon')
cmds.setAttr(materiau_dragon + '.color', 0.9, 0.8, 0.3, type='double3')  # Or clair

materiau_escalier = cmds.shadingNode('lambert', asShader=True, n='Materiau_Escalier')
cmds.setAttr(materiau_escalier + '.color', 0.5, 0.5, 0.5, type='double3')  # Gris escalier

# Création des groupes de shading
sg_pierre = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, n='SG_Pierre')
sg_toit = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, n='SG_Toit')
sg_or = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, n='SG_Or')
sg_dragon = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, n='SG_Dragon')
sg_escalier = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, n='SG_Escalier')

# Connexion des matériaux aux groupes de shading
cmds.connectAttr(materiau_pierre + '.outColor', sg_pierre + '.surfaceShader')
cmds.connectAttr(materiau_toit + '.outColor', sg_toit + '.surfaceShader')
cmds.connectAttr(materiau_or + '.outColor', sg_or + '.surfaceShader')
cmds.connectAttr(materiau_dragon + '.outColor', sg_dragon + '.surfaceShader')
cmds.connectAttr(materiau_escalier + '.outColor', sg_escalier + '.surfaceShader')


# Application des matériaux aux différents éléments du temple
def appliquer_materiau_si_existe(nom_objet, groupe_shading):
    """Applique un matériau à un objet s'il existe"""
    if cmds.objExists(nom_objet):
        cmds.sets(nom_objet, e=True, forceElement=groupe_shading)

# Socle et fondations (pierre)
appliquer_materiau_si_existe('Socle_Temple', sg_pierre)
appliquer_materiau_si_existe('Balustrade_Decorative*', sg_pierre)

# Colonnes (rouge tuile)
appliquer_materiau_si_existe('Colonne_Support*', sg_toit)

# Toits (rouge tuile)
appliquer_materiau_si_existe('Toit', sg_toit)
appliquer_materiau_si_existe('Toit_Sup', sg_toit)
appliquer_materiau_si_existe('Toit_Arrondi_Final', sg_toit)

# Pagode (or)
appliquer_materiau_si_existe('Pagode', sg_or)

# Dragons (or clair)
appliquer_materiau_si_existe('dragon_tube*', sg_dragon)

# Escaliers (gris pierre)
appliquer_materiau_si_existe('escalier*', sg_escalier)
appliquer_materiau_si_existe('cube_marche', sg_escalier)

# Décorations (rouge tuile)
appliquer_materiau_si_existe('cube_deco*', sg_toit)