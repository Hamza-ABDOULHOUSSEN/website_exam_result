# Consigne

## La structure des fichiers ADMISSIBLE_..., ADMIS_..., Ecrit_... et Oral_

| Champs         | Description           | Domaine                               | Nul |
|----------------|:----------------------|:--------------------------------------|:---:|
| Can _cod       | code candidat         | [0-9]{2,5} doit être unique           |     |
| Civ _lib       | civilité              | `M.`, `Mme`                           |     |
| Nom	           | nom                   | nom (uppercase)                     |     |
| Prenom	       | prénom                | prénom (tiret/espace) (capitalized) |     |
| Can _ad 1	     | adresse               | numéro, rue, nom (avec virgules)      |     |
| Can _ad 2	     | complément adresse    | `chez ...`, `App XX`,                 | X   |
| Can _cod _pos	 | code postal           | valeur entière                        |     |
| Can _com	     | commune, ville        | ville (capitalized)                   |     |
| Can _pay _adr	 | pays                  | `France`, `Maroc`, `Monaco`           |     |
| Can _mel	     | email                 |                                       |     |
| Can _tel	     | téléphone fixe        | numéro avec préfix éventuel (212)XXXX | X   |
| Can _por	     | téléphone mobile      | numéro avec préfix éventuel (212)XXXX | X   |
| rang           | rang sur le concours  | nombre (pas obligatoirement unique)   |     |

## La structure des fichiers liste

| Champs   | Description                                              |
|----------|:---------------------------------------------------------|
| Can _cod | code candidat                                            |
| Voe _ran | rang d'admission du candidat                             |
| Voe _ord | ordre de priorité dans le voeux formulés par le candidat |
| Eco _cod | code de l'école choisie                                  |

## La structure des fichiers CMT_Oraux_

Ces fichiers contiennent les notes des candidats aux épreuves orales, le centre où se sont déroulées les épreuves et la constitution du jury.

`; Numéro d'inscription	Centre, Jury, S.I., Maths, Entretien, Anglais`

## La structures des fichiers Classes_..._CMT_spe_YYYY_SCEI et Classes_..._CMT_spe_YYYY.xls

Ces fichiers contiennent les résultats finaux des élèves aux épreuves. Le fichier `.csv` ne devrait être qu'une vue partielle des données présentes dans le fichier `.xls`.

## La structure des fichiers ResultatOral_DD_MM_YYYY_ATS et ResultatEcrit_DD_MM_YYYY_ATS

Ces fichiers contiennent les résultats des élèves ATS à leurs épreuves orales et écrites. Vous noterez qu'il y a beaucoup plus de résultats pour les épreuves d'écrit que de candidats inscrits. Vous pourrez donc ignorer le résultats des candidats inconnus (non inscrits).

## La structure du fichier Inscription.xlsx

Ce fichier contient des informations supplémentaires concernant les élèves inscrits.

# Bases de données

## Candidat

| Clé | Champs         | Description           | Domaine                                                                                  | Nul |
|-----|----------------|:----------------------|:-----------------------------------------------------------------------------------------|:---:|
| X   | Can _cod       | code candidat         | [0-9]{2,5} doit être unique                                                              |     |
|     | Civ _lib       | civilité              | `M.`, `Mme`                                                                              |     |
|     | Nom	           | nom                   | nom (uppercase)                                                                          |     |
|     | Prenom	       | prénom                | prénom (tiret/espace) (capitalized)                                                      |     |
|     | Filière        | filière               | `MP-SPE`, `MP`, `PC-SPE`, `PC`, `PSI-SPE`, `PSI`, `PT-SPE`, `PT`, `TSI-SPE`,`TSI`, `ATS` |     |
|     | Puissance      | année du candidat     | `3/2`, `5/2`                                                                             |     |
|     | rang           | code candidat         | nombre                                                                                   |     |

## Coordonnées

| Clé | Champs         | Description           | Domaine                               | Nul |
|-----|----------------|:----------------------|:--------------------------------------|:---:|
| X   | Can _cod       | code candidat         | [0-9]{2,5} doit être unique           |     |
|     | Can _ad 1	   | adresse               | numéro, rue, nom (avec virgules)      |     |
|     | Can _ad 2	   | complément adresse    | `chez ...`, `App XX`,                 | X   |
|     | Can _cod _pos  | code postal           | valeur entière                        |     |
|     | Can _com	   | commune, ville        | ville (capitalized)                   |     |
|     | Code_pays      | code du pays          | code [0-9]^+                          |     |
|     | Can _pay _adr  | pays                  | `France`, `Maroc`, `Monaco`           |     |
|     | Can _mel	   | email                 |                                       |     |
|     | Can _tel	   | téléphone fixe        | numéro avec préfix éventuel (212)XXXX | X   |
|     | Can _por	   | téléphone mobile      | numéro avec préfix éventuel (212)XXXX | X   |

## Informations

| Clé | Champs                | Description                          | Domaine                     | Nul |
|-----|-----------------------|:----------------------|:-------------------------------------------|:---:|
| X   | Can _cod              | code candidat                        | [0-9]{2,5} doit être unique |     |
|     | Autres_prenoms        | Autres prénoms                       | Prénoms                     | X   |
|     | Date_naissance        | Date de naissance                    | [0-9]{2}/[0-9]{2}/[0-9]{4}  |     |
|     | Ville_naissance       | Ville naissance                      | ville                       |     |
|     | Code_pays_naissance   | code pays naissance                  | code [0-9]^+                |     |
|     | Code_pays_nationalite | code pays nationalité                | code [0-9]^+                |     |
|     | CSP_pere              | catégorie socio professionnelle père | [0-9]{2,3}                  | X   | 
|     | CSP_mere              | catégorie socio professionnelle mère | [0-9]{2,3}                  | X   | 
|     | Num_INE               | numéro étudiant                      | chiffres puis lettre        | X   |
|     | handicap              | handicapé                            | rien ou 1                   | X   |
|     | boursier              | boursier                             | rien ou 1                   | X   |
|     | TIPE                  | sujet choisi pour le TIPE            | chaine de caractères        |     | 

## Voeux

Chaque candidat peut faire plusieurs voeux dans plusieurs écoles s'il le souhaite
| Clé | Champs   | Description                                              | Domaine       |
|-----|----------|:---------------------------------------------------------|---------------|
|     | Can _cod | code candidat                                            | nombre unique |
|     | Voe _ran | rang d'admission du candidat à ce voeu                   | nombre        |
|     | Voe _ord | ordre de priorité dans le voeux formulés par le candidat | nombre        |
|     | Eco _cod | code de l'école choisie                                  | nombre        |

## Notes oraux

| Clé | Champs    | Description                                              | Domaine                   | Nul |
|-----|-----------|:---------------------------------------------------------|---------------------------|-----|
| X   | Can _cod  | code candidat                                            | nombre unique             |     |
|     | Centre    | nom du centre de passage                                 | chaine de caractères      |     |
|     | Jury      | nom du jury                                              | nom (capitalized), prénom |     |
|     | SI        | note en SI                                               | nombre dans [0,20]        | X   |
|     | Physique  | note en Physique                                         | nombre dans [0,20]        | X   |
|     | Maths     | note en Maths                                            | nombre dans [0,20]        |     |
|     | Entretien | note d'entretien                                         | nombre dans [0,100]       |     |
|     | Anglais   | note en Anglais                                          | nombre dans [0,20]        |     |

## Notes écrits 

Voir en fonction des filières


## Codes pays

| Clé | Champs         | Description           | Domaine                               | Nul |
|-----|----------------|:----------------------|:--------------------------------------|:---:|
| X   | Code_pays      | code pays             | code [0-9]^+                          |     |
|     | Pays           | pays                  | pays (capitalized)                    |     |

## Catégorie socio professionnelle (CSP)

| Clé | Champs         | Description           | Domaine                               | Nul |
|-----|----------------|:----------------------|:--------------------------------------|:---:|
| X   | CSP            | code de la catégorie socio professionnelle | code [0-9]^+     |     |
|     | CSP_intitule   | intitulé de la catégorie | chaine de caractères               |     |

## Codes écoles

| Clé | Champs         | Description           | Domaine                               | Nul |
|-----|----------------|:----------------------|:--------------------------------------|:---:|
| X   | Code_école     | code école            | code [0-9]^+                          |     |
|     | Nom_ecole      | Nom de l'école        | chaîne de caractères                  |     |

## Liste établissement

Voir la liste des établissements

# Relations entre les bases

| Base 1       | Base 2       | Cardinalité (1->2 / 2->1) | Clé(s) liante(s) |
|:-------------|:-------------|:--------------------------|------------------|
| Candidat     | Coordonnées  | 1:1/1:1                   | Code candidat    |
| Candidat     | Informations | 1:1/1:1                   | Code candidat    |
| Informations | Coordonnées  | 1:1/1:1                   | Code candidat    |
| Informations | CSP          | 2:2/1:1                   | CSP              |
| Coordonnées  | Pays         | 2:2/1:1                   | Code pays        |
| Candidat     | Voeux        | 1:n/1:1                   | Code candidat    |
| Voeux        | Ecoles       | 1:1/1:n                   | Code école       |
| Candidat     | Notes        | 1:1/1:1                   | Code candidat    |
| Candidat     | Notes orales | 1:1/1:1                   | Code candidat    |
