# LuTOOL

Le but the LuTOOL est/était de fournir un ensemble d'outils pour les luthiers. Je publie le premier outil qui fonction, à savoir le générateur de diapason. 
Le générateur peut fabriquer un fichier vectoriel de diapason pour toute longueur de diapason donnée en millimètres ou en pouces. 
Le fichier vectoriel (un SVG) peut être utilisé ensuite pour découper le diapason (découpe laser, fraisage, etc.)
attention, Le code couleur utilisé est celui de notre service [Link](http://www.damengo.com) : rouge pour la découpe, vert pour la gravure (au trait).
Les caractéristiques des diapasons sont largement inspirées de ceux publiés par [Link](https://www.lutherie-amateur.com/Forum/index.php). Un grand merci à eux !



## Installation 

utiliser [pip](https://pip.pypa.io/en/stable/) pour installer les dépendances de LuTOOL

```bash
pip install requirements.txt
```

et exécuter :

```bash
python LuTOOL.py
```

ou télécharger une des (futures) releases...

## License 

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Avertissements 

Vous pouvez/devriez vérifier que le diapason est conforme (par exemple en l'ouvrant dans inkscape et en mesurant la distance entre les frettes). Je décline toute responsabilité !
Le code est moche mais je n'ai pas le temps de l'améliorer :)
