# PPII «Projet Pluridisciplinaire d'Informatique Intégrative» (2020-2021)

Sébastien Da Silva <<sebastien.dasilva@telecomnancy.eu>>  
Gérald Oster <<gerald.oster@telecomnancy.eu>>  


## Préliminaires 

Cette année, le projet porte sur les données du concours Mines-Telecom. Durant ce projet, vous aurez l'occasion de travailler sur des données réelles anonymisées et de réaliser des traitements sur ces données. 

En seconde partie du projet, nous vous proposons d'étudier un problème ouvert sur ces données : **DEVOILÉ ULTÉRIEUREMENT**


### Objectifs et Attendus

- Conception et mise en œuvre d’une base de données relationnelle
- Réalisations de plusieurs composants logiciels informatiques dans les langages de programmation C, Java et/ou Python
- Réalisation d'une étude bibliographique
- Recherche de solution à un problème ouvert
- Évaluation de la qualité des solutions proposées et des résultats obtenus 
- Mise en oeuvre d'une gestion de projet

### Modalités

Ce projet est à réaliser en groupe (la constitution du groupe étant imposée). 

Vos livrables seront composés :
- des codes sources de vos développements logiciels ; 
- des documentations nécessaires à la compréhension (conception, notes de développement), l'installation, la compilation, l'exécution, la validations de vos réalisations ;
- de **tous les éléments de gestion de projet** que vous aurez produits (fiche de projet, comptes-rendus de réunion, planification et répartition des tâches, analyse post-mortem des efforts individuels et de l'atteinte des objectifs, etc.)

L'ensemble de ces livrables seront déposés sur le dépôt git qui est dédié à votre groupe de travail (sous-projet du projet https://gitlab.telecomnancy.univ-lorraine.fr/ppii-2k21) 


**Nota Bene.** Ne trichez pas ! Ne copiez pas ! Ne plagiez pas ! Si vous le faites, vous serez lourdement sanctionnés. Nous ne ferons pas de distinction entre copieur et copié. Vous n’avez pas de (bonnes) raisons de copier. De même, vous ne devez pas utiliser un produit clé en main trouvé sur internet.



## Base de données relationnelle

### Objectifs généraux

- Concevoir un schéma de base de données relationnelle stockant des données du concours Mines-Telecom
- Implémenter ce schéma relationnel dans un système de gestion de base de données (SGBD)
- Élaborer des requêtes SQL sur le schéma relationnel 
- Développer des scripts d'importation de fichiers de données de différents formats (`.csv`, `.xlsx`).

### Attendus

Il est attendu :
- la conception d'**un schéma relationnel** pour intégrer les données mentionnées précédemment
  - ce schéma devra dans un premier temps être en **3ème forme normale**, vous pourrez *dénormaliser* ce schéma si nécessaire en argumentant sur ce point
  - vous identifierez les **contraintes d'intégrité** du modèle de données
- la transposition de ce modèle dans **une base de données relationnelle** sur un SGBD (SQLite, PostgreSQL, MySQL, MariaDB) 
- l'**importation (automatisée) des données** dans la base proposée (un nettoyage des données sera peut-être nécessaire, une vérification de la cohérence des données sera **obligatoire**).
- la réalisation d'un certain nombre de **requêtes SQL** démontrant la viabilité du modèle proposé.

**Attention**: Votre rendu devra permettre d'initialiser une base de données vide puis d'y importer les données depuis des fichiers. Un utilisateur doit pouvoir importer d'autres données (par exemple, l'ensemble des données non-anonymisées) en fournissant simplement d'autres fichiers de données (par exemple un autre répertoire où l'on peut trouver ces données).

### Base de données à votre disposition

L'école ne mettra pas à votre disposition de serveur de bases de données. Nous vous conseillons donc d'utiliser un serveur local à vos machines de développement. Le plus simple est d'utiliser SQLite. Ce n'est pas une obligation mais cela sera beaucoup plus simple pour automatiser l'exécution de vos programmes sur un autre ordinateur (par exemple, l'ordinateur des enseignants devant évaluer votre projet).

Dans tous les cas, vous documenterez la procédure pour installer/exécuter/initialiser votre base de données.


### À propos de données fournies

L'ensemble des données à intégrer à votre base sont disponibles sous différents formats (`.xlsx`, `.csv`) dans le répertoire `data/public/` du dépôt git disponible à l'adresse suivante : https://gitlab.telecomnancy.univ-lorraine.fr/ppii2k21/dow


Dans les sous-sections suivantes vous trouverez une description rapide des données fournies. Cette description devrait être suffisante pour vous permettre d'établir un lien entre les données, de définir les types des données manipulées et les contraintes sur ces données. Si toutefois, une question subsistait n'hésitez pas à contacter l'équipe pédagogique à ce sujet.

Les données ont été partiellement anonymisées tout en maintenant leur cohérence (mais nous ne sommes pas à l'abri d'une erreur lors du processus d'anonymisation).


#### La structure des fichiers ADMISSIBLE_..., ADMIS_..., Ecrit_... et Oral_...

Chaque fichier correspond aux candidats présents à la phase d'admission et/ou admis au concours. Chaque candidat est inscrit dans une filière (MP, PC, PSI, PT, TSI).

- `ADMIS_MP-SPE.xls`, `ADMIS_MP.xls`,
 `ADMIS_PC-SPE.xls`, `ADMIS_PC.xls`,
 `ADMIS_PSI-SPE.xls`, `ADMIS_PSI.xls`,
 `ADMIS_PT-SPE.xls`, `ADMIS_PT.xls`,
 `ADMIS_TSI-SPE.xls`, `ADMIS_TSI.xls`,
 `ADMIS_ATS.xls`

- `ADMISSIBLE_MP-SPE.xls`, `ADMISSIBLE_MP.xls`,
 `ADMISSIBLE_PC-SPE.xls`, `ADMISSIBLE_PC.xls`,
 `ADMISSIBLE_PSI-SPE.xls`, `ADMISSIBLE_PSI.xls`,
 `ADMISSIBLE_PT-SPE.xls`, `ADMISSIBLE_PT.xls`,
 `ADMISSIBLE_TSI-SPE.xls`, `ADMISSIBLE_TSI.xls`,

- `Ecrit_MP.xls`, `Ecrit_PC.xls`, `Ecrit_PSI.xls`, `Ecrit_PT.xls` et `Ecrit_TSI.xls`
- `Oral_MP.xls`, `Oral_PC.xls`, `Oral_PSI.xls`, `Oral_PT.xls` et `Oral_TSI.xls`

Les fichiers `ADMIS-` doivent contenir un sous ensemble des `ADMISSIBLES-`.

Les fichiers `-SPE` contiennent des candidats supplémentaires par rapport aux autres fichiers.

Les fichiers `Ecrit_` et `Oral_` contiennent respectivement les classements à la suite des épreuves écrites et orales des candidats. 


Les fichiers ont pour entête la liste des valeurs : 

`; Can _cod, Civ _lib, Nom, Prenom, Can _ad 1, Can _ad 2, Can _cod _pos, Can _com, Can _pay _adr, Can _mel, Can _tel, Can _por, rang`


| Champs         | Description           | Domaine                               | Nul |
|----------------|:----------------------|:--------------------------------------|:---:|
| Can _cod       | code candidat         | [0-9]{2,5} doit être unique           |     |
| Civ _lib       | civilité              | `M.`, `Mme`                           |     |
| Nom	           | nom                   | nom (uppercase)                       |     |
| Prenom	       | prénom                | prénom (tiret/espace) (capitalized)   |     |
| Can _ad 1	     | adresse               | numéro, rue, nom (avec virgules)      |     |
| Can _ad 2	     | complément adresse    | `chez ...`, `App XX`,                 | X   |
| Can _cod _pos	 | code postal           | valeur entière                        |     |
| Can _com	     | commune, ville        | ville (capitalized)                   |     |
| Can _pay _adr	 | pays                  | `France`, `Maroc`, `Monaco`           |     |
| Can _mel	     | email                 |                                       |     |
| Can _tel	     | téléphone fixe        | numéro avec préfix éventuel (212)XXXX | X   |
| Can _por	     | téléphone mobile      | numéro avec préfix éventuel (212)XXXX | X   |
| rang           | rang sur le concours  | nombre (pas obligatoirement unique)   |     |


#### La structure des fichiers liste...

Ces fichiers sont liés aux voeux des candidats :
- `listeEcoles.xls` et `listeEtablissements.xls`
contiennent la liste des établissements d'où sont originaires les candidats et la liste des écoles auxquelles les élèves ont postulé ;
- `listeEtatsReponsesAppel.xls` contient la signification des états des réponses aux voeux formulés ;  
- `listeVoeux_MP.xls`, `listeVoeux_PC.xls`, `listeVoeux_PSI.xls`, `listeVoeux_PT.xls`, `listeVoeux_TSI.xls` et `listeVoeux_ATS.xls` 
contiennent les voeux formulés par les candidats. Ces fichiers ont pour entête la liste des valeurs : `; Can _cod, Voe _ran, Voe _ord, Eco _cod`

| Champs   | Description                                              |
|----------|:---------------------------------------------------------|
| Can _cod | code candidat                                            |
| Voe _ran | rang d'admission du candidat                             |
| Voe _ord | ordre de priorité dans le voeux formulés par le candidat |
| Eco _cod | code de l'école choisie                                  |

#### La structure des fichiers CMT_Oraux_...

Ces fichiers contiennent les notes des candidats aux épreuves orales, le centre où se sont déroulées les épreuves et la constitution du jury.

`; Numéro d'inscription	Centre, Jury, S.I., Maths, Entretien, Anglais`

#### La structures des fichiers Classes_..._CMT_spe_YYYY_SCEI et Classes_..._CMT_spe_YYYY.xls

Ces fichiers contiennent les résultats finaux des élèves aux épreuves. Le fichier `.csv` ne devrait être qu'une vue partielle des données présentes dans le fichier `.xls`.


#### La structure des fichiers ResultatOral_DD_MM_YYYY_ATS et ResultatEcrit_DD_MM_YYYY_ATS

Ces fichiers contiennent les résultats des élèves ATS à leurs épreuves orales et écrites. Vous noterez qu'il y a beaucoup plus de résultats pour les épreuves d'écrit que de candidats inscrits. Vous pourrez donc ignorer le résultats des candidats inconnus (non inscrits).


#### La structure du fichier Inscription.xlsx

Ce fichier contient des informations supplémentaires concernant les élèves inscrits.

#### Informations additionnelles non fournies

En plus de ces données, vous supposerez qu'il est possible de vous fournir sous forme d'un fichier la liste des élèves qui ont définitivement intégré une école. L'information peut ne pas être disponible pour tous les élèves. Il peut y avoir de nouvelles filières à l'avenir.



## Applications de consultation des données

### Objectifs généraux

- Concevoir une application permettant de consulter et d'interroger les données de la base.
- Construire des visualisations
- Générer des rapports au format HTML

### Attendus

Vous réaliserez une ou plusieurs applications permettant de consulter et d'interroger les données de votre base de données.
Vous pouvez utiliser le ou les langages de votre choix (Python, C, Java) pour réaliser ces applications. 


Vos applications devront permettre de réaliser un rapport au format HTML (voir même en format PDF) du résultat de ces interrogations.

### Quelques exemples de requêtes et visualisations pertinentes

Nous compléterons cette section d'ici quelques jours. Nous vous indiquerons quelques requêtes qui nous semblent pertinentes à pouvoir réaliser sur les données et des exemples d'informations que nous souhaiterions visualiser.

**COMPLETÉE ULTÉRIEUREMENT**


## Problème ouvert

**DEVOILÉ ULTÉRIEUREMENT**
